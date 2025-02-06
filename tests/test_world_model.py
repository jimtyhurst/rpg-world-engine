from rpg_world_engine import game_configuration
import constants
import pytest

WORLD_MODEL = game_configuration.load_configuration_file(
    constants.WORLD_MODEL_PATH
)


@pytest.fixture
def actual_world_model():
    return WORLD_MODEL


def test_load_model_happy_path(actual_world_model):
    """Tests that file loads. Verifies the presence of a few properties."""
    assert isinstance(actual_world_model["world"]["name"], str)
    assert isinstance(actual_world_model["regions"], list)
    assert isinstance(actual_world_model["player"]["name"], str)
    assert isinstance(actual_world_model["npcs"], list)


def test_load_model_expect_locale_region_matches_region_name(
    actual_world_model,
):
    """locale has region property that refers back to the locale's containing region."""
    actual_region = actual_world_model["regions"][0]
    for locale in actual_region["locales"]:
        assert locale["region"] == actual_region["name"]
