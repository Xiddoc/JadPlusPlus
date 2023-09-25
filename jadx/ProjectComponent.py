"""
The base class for project components.
Includes parsing for loading projects and serialization for saving back to a file.
"""
import json
from abc import ABCMeta, abstractmethod
from typing import Dict, Any, List, Union

JSON_INDENTATION = 2


class ProjectComponent(metaclass=ABCMeta):

    @classmethod
    def from_stringified_json(cls, stringified_json: str) -> "ProjectComponent":
        return cls.from_json(json.loads(stringified_json))

    @staticmethod
    @abstractmethod
    def from_json(parsed_json: Dict[str, Any]) -> "ProjectComponent":
        """
        Constructs a project component from a JSON object (dictionary).
        """

    def to_stringified_json(self) -> str:
        return json.dumps(self.to_primitives(), indent=JSON_INDENTATION)

    @abstractmethod
    def to_primitives(self) -> Union[Dict, List]:
        """
        Serializes a project component to Python primitives.
        """
