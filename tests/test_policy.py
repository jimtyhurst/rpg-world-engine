from rpg_world_engine import policy
import pytest


def test_get_key():
    expected_rating_value = "EVERYONE_10_PLUS"
    actual_enum = policy.AgeAppropriateRating(expected_rating_value)
    assert actual_enum == policy.AgeAppropriateRating.EVERYONE_10_PLUS
    assert actual_enum.value == expected_rating_value


def expects_value_error():
    """TODO: Remove this test after AgeAppropriateRating() constructor has been enhanced."""
    expected_rating_value = "zzz-undefined-zzz"
    with pytest.raises(ValueError):
        policy.AgeAppropriateRating(expected_rating_value)


@pytest.mark.skip(reason="Not implemented yet!")
def expects_undefined_value():
    """TODO: Enhance the AgeAppropriateRating() constructor.
    Actual Behavior: Constructor raises ValueError.
    Expected Behavior: Value that does not match an existing Enum value results in UNDEFINED item.
    """
    expected_rating_value = "zzz-undefined-zzz"
    actual_enum = policy.AgeAppropriateRating(expected_rating_value)
    assert actual_enum == policy.AgeAppropriateRating.UNDEFINED
