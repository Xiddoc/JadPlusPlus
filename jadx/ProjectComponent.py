"""
The base class for project components.
Includes parsing for loading projects and serialization for saving back to a file.
"""
from abc import ABCMeta, abstractmethod
from typing import Dict, Any


class ProjectComponent(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def from_json(json: Dict[str, Any]) -> "ProjectComponent":
        """
        Constructs a project component from a JSON object (dictionary).
        """

    @abstractmethod
    def to_json(self) -> str:
        """
        Serializes a project component to a JSON string.
        """
