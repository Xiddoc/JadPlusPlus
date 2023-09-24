"""
The JadX project's code data.

This includes most of the relevant project work, such as comments and renames.
"""
from dataclasses import dataclass
from typing import List, Any, Dict

from jadx.ProjectComponent import ProjectComponent


@dataclass
class ProjectCodeData(ProjectComponent):
    comments: List[Any]
    renames: List[Any]

    @staticmethod
    def from_json(parsed_json: Dict[str, Any]) -> "ProjectCodeData":
        pass

    def to_json(self) -> str:
        pass
