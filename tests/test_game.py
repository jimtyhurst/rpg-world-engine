from rpg_world_engine import game
from rpg_world_engine import world_model
import constants


def test_get_starting_game_state():
    actual_world_model = world_model.load_world_model(constants.WORLD_MODEL_PATH)
    game_state = game.get_starting_game_state(actual_world_model)
    assert game_state is not None
    assert game_state["world"] == actual_world_model
