"""
Holds the data for a JadX project.
"""
from dataclasses import dataclass
from typing import List, Dict, Any, Union

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
    def from_json(parsed_json: Dict[str, Any]) -> "JadxProject":
        return JadxProject(
            project_version=parsed_json["projectVersion"],

            files=parsed_json["files"],
            tree_expansions=[TreeExpansion.from_json(tree) for tree in parsed_json["treeExpansions"]],
            code_data=ProjectCodeData.from_json(parsed_json["codeData"]),
            open_tabs=[OpenTab.from_json(tab) for tab in parsed_json["openTabs"]],

            active_tab=parsed_json["activeTab"],
            cache_dir=parsed_json["cacheDir"],
            enable_live_reload=parsed_json["enableLiveReload"],
            search_history=parsed_json["searchHistory"]
        )

    def to_primitives(self) -> Union[Dict, List]:
        return {
            "projectVersion": self.project_version,

            "files": self.files,
            "treeExpansions": [tree.to_primitives() for tree in self.tree_expansions],
            "codeData": self.code_data.to_primitives(),
            "openTabs": [tab.to_primitives() for tab in self.open_tabs],

            "activeTab": self.active_tab,
            "cacheDir": self.cache_dir,
            "enableLiveReload": self.enable_live_reload,
            "searchHistory": self.search_history
        }
