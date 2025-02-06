from rpg_world_engine import game
from rpg_world_engine import game_configuration
from rpg_world_engine import policy
import constants
import pytest

WORLD_MODEL = game_configuration.load_configuration_file(
    constants.WORLD_MODEL_PATH
)
GAME_SCENARIO = game_configuration.load_configuration_file(
    constants.GAME_SCENARIO_PATH
)


@pytest.fixture
def actual_world_model():
    return WORLD_MODEL


@pytest.fixture
def actual_game_scenario():
    return GAME_SCENARIO


def test_get_starting_game_state_happy_path(
    actual_world_model, actual_game_scenario
):
    """Verifies presence of expected properties."""
    game_state = game.get_starting_game_state(
        actual_world_model, actual_game_scenario
    )
    assert game_state is not None
    assert game_state["title"] == actual_game_scenario["title"]
    assert game_state["world"] == actual_world_model
    assert isinstance(game_state["player"]["name"], str)
    assert game_state["inventory"] is not None
    assert len(game_state["inventory"].keys()) == 0
    assert game_state["world"]["world"]["name"] in game_state["challenge"]
    assert game_state["world"]["player"]["name"] in game_state["challenge"]
    assert (
        game_state["age_appropriate_rating"]
        == policy.AgeAppropriateRating.EVERYONE_10_PLUS
    )


def test_get_starting_game_state_with_inventory(
    actual_world_model, actual_game_scenario
):
    """Verifies initialization of 'inventory'."""
    expected_item = "snub-nosed revolver"
    expected_quantity = 1
    expected_inventory = {expected_item: expected_quantity}
    game_state = game.get_starting_game_state(
        actual_world_model, actual_game_scenario, inventory=expected_inventory
    )
    assert expected_quantity == game_state["inventory"][expected_item]
