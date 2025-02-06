"""Enforces safety policy."""

from enum import Enum


class AgeAppropriateRating(Enum):
    """Ratings based on Entertainment Software Rating Board (https://www.esrb.org/ratings-guide/).

    TODO: Enhance the constructor, so that a value that does not match an existing Enum value results in UNDEFINED item.
    Currently, the constructor raises a ValueError for that condition.
    """

    EVERYONE = "EVERYONE"
    EVERYONE_10_PLUS = "EVERYONE_10_PLUS"
    TEEN = "TEEN"
    MATURE_17_PLUS = "MATURE_17_PLUS"
    ADULTS_ONLY_18_PLUS = "ADULTS_ONLY_18_PLUS"
    UNDEFINED = "UNDEFINED"


def is_safe(
    content, age_appropriate_rating=AgeAppropriateRating.UNDEFINED
) -> bool:
    """TODO: Implement a pipeline of classifiers.

    :returns: True if none of the evaluation criteria are triggered.
        is_off_topic
        is_hate_speech
        is_overtly_sexual
        is_excessively_violent
    """
    return True
