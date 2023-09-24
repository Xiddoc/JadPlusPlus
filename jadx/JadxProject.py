"""
Holds the data for a JadX project.
"""
import json
from dataclasses import dataclass
from typing import List, Dict, Any

from jadx.OpenTab import OpenTab
from jadx.ProjectCodeData import ProjectCodeData
from jadx.ProjectComponent import ProjectComponent
from jadx.TreeExpansion import TreeExpansion


@dataclass
class JadxProject(ProjectComponent):
    project_version: int

    files: List[str]
    tree_expansions: List[TreeExpansion]
    code_data: ProjectCodeData
    open_tabs: List[OpenTab]

    active_tab: int
    cache_dir: str
    enable_live_reload: bool
    search_history: List[str]

    @classmethod
    def from_stringified_json(cls, stringified_json: str) -> "ProjectComponent":
        return cls.from_json(json.loads(stringified_json))

    @staticmethod
    def from_json(parsed_json: Dict[str, Any]) -> "ProjectComponent":
        pass

    def to_json(self) -> str:
        pass
