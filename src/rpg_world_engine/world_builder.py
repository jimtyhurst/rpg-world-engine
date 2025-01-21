"""
Functions for building a hierarchical world model.

TODO: Make a sequence of calls to build the model: world, regions, locales, player, NPCs.
"""

from collections.abc import Mapping

from rpg_world_engine import llm_client


def build_world(
    client: llm_client.LLMClient, world_specification: Mapping
) -> Mapping:
    model_state = client.generate_content(world_specification)
    return model_state
