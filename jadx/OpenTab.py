"""
A tree expansion in the source code tree panel.
"""
from dataclasses import dataclass
from typing import Dict, Any

from jadx.ProjectComponent import ProjectComponent


@dataclass
class OpenTab(ProjectComponent):
    @staticmethod
    def from_json(json: Dict[str, Any]) -> "ProjectComponent":
        pass

    def to_json(self) -> str:
        pass
