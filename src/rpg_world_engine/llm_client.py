"""
Defines an adapter for using an LLM model.
"""

from abc import abstractmethod
from collections.abc import Mapping

import logging
from rpg_world_engine import rpg_logging

logger = rpg_logging.get_logger(__name__)
logger.setLevel(logging.DEBUG)


class LLMClient:
    @abstractmethod
    def generate_content(prompt: Mapping) -> Mapping:
        pass


class MockLLMClient(LLMClient):
    def __init__(self, model_name: str, expected_content: Mapping):
        self.model_name = model_name
        self.expected_content = expected_content

    def generate_content(self, prompt: Mapping) -> Mapping:
        logger.info(f"{prompt=}")
        return self.expected_content
