"""
Holds the data for a JadX project.
"""
from typing import List

from dataclasses import dataclass

from jadx.OpenTab import OpenTab
from jadx.ProjectCodeData import ProjectCodeData
from jadx.TreeExpansion import TreeExpansion


@dataclass
class JadxProject:
    project_version: int

    files: List[str]
    tree_expansions: List[TreeExpansion]
    code_data: ProjectCodeData
    open_tabs: List[OpenTab]

    active_tab: int
    cache_dir: str
    enable_live_reload: bool
    search_history: List[str]

    def from_json(self, project_json: str) -> "JadxProject":
        pass
