from collections.abc import Mapping

from rpg_world_engine import llm_client, world_builder

import logging
from rpg_world_engine import rpg_logging

logger = rpg_logging.get_logger(__name__)
logger.setLevel(logging.DEBUG)


def get_world_specification() -> Mapping:
    # _ = dotenv.load_dotenv(override=False)
    # with open(os.environ.get("WORLD_SPECIFICATION_PATH")) as f:
    #     world_specification = json.load(f)
    # return world_specification
    world_specification = {
        "category_map": {
            "world": "city",
            "region": "neighborhood",
            "locale": "place",
        },
        "world_prompt": {
            "contents": "Provide a few paragraphs of fiction\nbased on the actual city of Chicago\nin the United States in the 1920s,\nusing a detective noir style.\nThe city has a corrupt government.\nGangsters on the South Side are making a lot of money\nfrom bootleg liquor during Prohibition.\nMrs. Lucille Robinson has hired Detective Harston Cooper\nto find her missing husband, Roland Robinson.\n",
            "system_instruction": 'You are a creative writer.\nProvide the response as JSON in this format:\n{\n"city": {"name": "<NAME>", "description": "<DESCrIPTION>", "atmosphere": "<ATMOSPHERE>", "mood": "<MOOD>"}\n}',
        },
    }
    return world_specification


def get_expected_world_state() -> Mapping:
    return {
        "world": {
            "name": "Chicago",
            "description": "The city was a beast of brick and steel, its heart pumping a rhythm of jazz and desperation.",
            "atmosphere": "The air was thick with a sense of unease, a feeling that something was always about to go wrong.",
            "mood": "The relentless pursuit of the dollar had hardened the city's inhabitants, leaving them suspicious and distrustful. Hope was a scarce commodity.",
        }
    }


def test_build_world_structure():
    mock_client = llm_client.MockLLMClient(
        "mock-client", get_expected_world_state()
    )
    world_specification = get_world_specification()
    logger.debug(f"{world_specification=}")
    actual_world = world_builder.build_world(mock_client, world_specification)
    logger.debug(f"{actual_world=}")
    assert isinstance(actual_world, Mapping)
    assert "world" in actual_world.keys()


def test_build_world_name():
    expected_name = "Chicago"
    mock_client = llm_client.MockLLMClient(
        "mock-client", get_expected_world_state()
    )
    actual_world = world_builder.build_world(
        mock_client, get_world_specification()
    )
    assert actual_world["world"]["name"] == expected_name
