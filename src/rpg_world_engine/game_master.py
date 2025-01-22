import dotenv
import os
from google import genai
from google.genai import types
import json
import gradio
from rpg_world_engine import game, game_configuration, inventory, policy
from rpg_world_engine import rpg_logging

import logging
logger = rpg_logging.get_logger(__name__)
logger.setLevel(logging.DEBUG)


# TODO: Need a better way to inject the LLM.
GAME_MASTER_LLM_NAME = os.getenv("GAME_MASTER_LLM_NAME")
assert GAME_MASTER_LLM_NAME is not None
API_KEY = os.getenv("GEMINI_API_KEY")
assert API_KEY is not None
GAME_MASTER_LLM_CLIENT = genai.Client(
    api_key=API_KEY,
    http_options={"api_version": "v1alpha"}
)


def run_action(user_prompt, history, game_state):
    if(user_prompt == 'start game'):
        return game_state['challenge']

    system_prompt = """
        You are the Game Master for a role playing game (RPG). \
        Your job is to write what happens next in a player's adventure game.\
        Instructions: \
        Write only a couple of sentences in response. \
        Always write in second person present tense. \
        For example, (You look north and see...) \
        Do not let the player use items they do not have in their inventory.
    """
    world = game_state["world"]['city']
    region = game_state["world"]['neighborhoods'][0]
    locale = game_state["world"]['neighborhoods'][0]["places"][0]
    world_info = f"""
        World: {world['name']}: {world['description']}
        Region: {region['name']}:{region['description']}
        Locale: {locale['name']}: {locale['description']}
        Your Character:  {game_state["world"]["player"]["name"]}
        Inventory: {json.dumps(game_state['inventory'])}
    """
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": world_info}
    ]
    for action in history:
        messages.append({"role": action["role"], "content": action["content"]})
        messages.append({"role": action["role"], "content": action["content"]})
    messages.append({"role": "user", "content": user_prompt})
    messages_as_text_parts = [types.Part.from_text(f"{message}") for message in messages]
    model_response = GAME_MASTER_LLM_CLIENT.models.generate_content(
        model=GAME_MASTER_LLM_NAME,
        contents=messages_as_text_parts,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=1.0,
            candidate_count=1,
            max_output_tokens=512,
            response_mime_type="application/json",
        ),
    )
    response_dict = json.loads(model_response.text)
    logger.debug(f"{response_dict=}")
    game_master_response = " ".join([f'{value}' for value in response_dict.values()])
    return game_master_response


def main_loop(user_prompt, history):
    logger.debug(f"{user_prompt=}")
    game_master_response = run_action(user_prompt, history, game_state)
    if not policy.is_safe(game_master_response, game_state["age_appropriate_rating"]):
        return f"Response is not appropriate for this game's rating of {game_state["age_appropriate_rating"]}."

    item_updates = inventory.detect_inventory_changes(game_state, game_master_response)
    update_msg = inventory.update_inventory(
        game_state['inventory'],
        item_updates
    )
    game_master_response += update_msg

    return game_master_response


def start_game(main_loop, game_state, share=False):
    """https://www.gradio.app/docs/gradio/chatinterface"""
    game_driver = gradio.ChatInterface(
        main_loop,
        multimodal=False,
        type="messages",
        chatbot=gradio.Chatbot(type="messages", height=250, placeholder="Type 'start game' to begin"),
        textbox=gradio.Textbox(placeholder="What do you do next?", container=False, scale=7),
        title=game_state["title"],
        description=game_state["challenge"],
        theme="soft",
        examples=["Look around", "Continue the story"],
        cache_examples=False,
        submit_btn=True,
        stop_btn=True,
    )
    game_driver.launch(share=share, server_name="0.0.0.0")


if __name__ == "__main__":
    _ = dotenv.load_dotenv(override=False)
    game_state = game.get_starting_game_state(
        game_configuration.load_configuration_file(os.getenv("WORLD_MODEL_PATH")),
        game_configuration.load_configuration_file(os.getenv("GAME_SCENARIO_PATH")),
    )
    start_game(main_loop, game_state, True)
