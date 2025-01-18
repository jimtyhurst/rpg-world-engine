from rpg_world_engine import world_model
import constants

def test_load_model_expect_world_name():
    """Tests that file loads. Checks the presence of a few properties."""
    actual_world = world_model.load_world_model(constants.WORLD_MODEL_PATH)
    assert isinstance(actual_world["world"]["name"], str)
    assert isinstance(actual_world["regions"], list)
    assert isinstance(actual_world["player"]["name"], str)
    assert isinstance(actual_world["npcs"], list)


def test_load_model_expect_locale_region_matches_region_name():
    """locale has region attribute that refers back to its containing region."""
    actual_world = world_model.load_world_model(constants.WORLD_MODEL_PATH)
    actual_region = actual_world["regions"][0]
    for locale in actual_region["locales"]:
        assert locale["region"] == actual_region["name"]
