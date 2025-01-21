"""
TODO: Still need to implement the ability for a Player to add items to their inventory. 
"""

import dotenv
import os
from google import genai


detect_inventory_system_prompt = """
    You are an AI Game Assistant.
    Your job is to detect changes to a player's
    inventory based on the most recent story and game state.
    If a player picks up, or gains an item add it to the inventory
    with a positive change_amount.
    If a player loses an item remove it from their inventory
    with a negative change_amount.
    Given a player name, inventory and story, return a list of json update
    of the player's inventory in the following form.
    Only take items that it's clear the player (you) lost.
    Only give items that it's clear the player gained.
    Don't make any other item updates.
    If no items were changed return {"itemUpdates": []}
    and nothing else.

    Response must be in Valid JSON
    Don't add items that were already added in the inventory

    Inventory Updates:
    {
        "itemUpdates": [
            {"name": <ITEM NAME>,
            "change_amount": <CHANGE AMOUNT>}...
        ]
    }
"""

# TODO: Need a better way to inject the LLM.
_ = dotenv.load_dotenv(override=False)
INVENTORY_LLM_NAME = os.getenv("INVENTORY_LLM_NAME")
assert INVENTORY_LLM_NAME is not None
API_KEY = os.getenv("GEMINI_API_KEY")
assert API_KEY is not None
INVENTORY_LLM_CLIENT = genai.Client(
    api_key=API_KEY,
    http_options={"api_version": "v1alpha"}
)


# def detect_inventory_changes(game_state, output):
#     inventory = game_state['inventory']
#     messages = [
#         {"role": "user", "content": f'Current Inventory: {str(inventory)}'},
#         {"role": "user", "content": f'Recent Story: {output}'},
#         {"role": "user", "content": 'Inventory Updates'}
#     ]
#     chat_completion = INVENTORY_LLM_CLIENT.models.generate_content(
#         model=INVENTORY_LLM_NAME,
#         contents=messages,
#         config=types.GenerateContentConfig(
#             system_instruction=detect_inventory_system_prompt,
#             temperature=0.0,
#             candidate_count=1,
#             max_output_tokens=512,
#             response_mime_type="application/json",
#         ),
#     )
#     response = chat_completion.choices[0].message.content
#     result = json.loads(response)
#     return result['itemUpdates']
def detect_inventory_changes(game_state, output):
    return []



def update_inventory(inventory, item_updates):
    update_msg = ''
    for update in item_updates:
        name = update['name']
        change_amount = update['change_amount']
        if change_amount > 0:
            if name not in inventory:
                inventory[name] = change_amount
            else:
                inventory[name] += change_amount
            update_msg += f'\nInventory: {name} +{change_amount}'
        elif name in inventory and change_amount < 0:
            inventory[name] += change_amount
            update_msg += f'\nInventory: {name} {change_amount}'
        if name in inventory and inventory[name] < 0:
            del inventory[name]
    return update_msg
