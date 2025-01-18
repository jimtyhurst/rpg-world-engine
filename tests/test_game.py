from rpg_world_engine import game
from rpg_world_engine import world_model
import constants
import pytest

WORLD_MODEL = world_model.load_world_model(constants.WORLD_MODEL_PATH)

@pytest.fixture
def actual_world_model():
    return WORLD_MODEL


def test_get_starting_game_state_happy_path(actual_world_model):
    """Verifies presence of expected properties."""
    game_state = game.get_starting_game_state(actual_world_model)
    assert game_state is not None
    assert game_state["world"] == actual_world_model
    assert isinstance(game_state["player"]["name"], str)
    assert game_state["inventory"] is not None
    assert len(game_state["inventory"].keys()) == 0
    assert game_state["world"]["world"]["name"] in game_state["challenge"]
    assert game_state["world"]["player"]["name"] in game_state["challenge"]


def test_get_starting_game_state_with_inventory(actual_world_model):
    """Verifies initialization of 'inventory'."""
    expected_item = "snub-nosed revolver"
    expected_quantity = 1
    expected_inventory = {expected_item: expected_quantity}
    game_state = game.get_starting_game_state(actual_world_model, inventory=expected_inventory)
    assert expected_quantity == game_state["inventory"][expected_item]
