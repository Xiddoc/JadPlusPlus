"""
A tree expansion in the source code tree panel.
"""
from dataclasses import dataclass
from typing import Dict, Any

from jadx.ProjectComponent import ProjectComponent


@dataclass
class TreeExpansion(ProjectComponent):
    @staticmethod
    def from_json(parsed_json: Dict[str, Any]) -> "TreeExpansion":
        pass

    def to_json(self) -> str:
        pass
