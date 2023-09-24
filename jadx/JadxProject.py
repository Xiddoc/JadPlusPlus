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

    @staticmethod
    def from_json(parsed_json: Dict[str, Any]) -> "ProjectComponent":
        return JadxProject(
            project_version=parsed_json["projectVersion"],

            files=parsed_json["files"],
            tree_expansions=parsed_json["treeExpansions"],
            code_data=parsed_json["codeData"],
            open_tabs=parsed_json["openTabs"],

            active_tab=parsed_json["activeTab"],
            cache_dir=parsed_json["cacheDir"],
            enable_live_reload=parsed_json["enableLiveReload"],
            search_history=parsed_json["searchHistory"]
        )

    def to_json(self) -> str:
        pass
