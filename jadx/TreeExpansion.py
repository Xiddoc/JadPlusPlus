"""
A tree expansion in the source code tree panel.
"""
from dataclasses import dataclass
from typing import List, Union, Dict

from jadx.ProjectComponent import ProjectComponent


@dataclass
class TreeExpansion(ProjectComponent):
    tree: List[str]

    @staticmethod
    def from_json(parsed_json: List[str]) -> "TreeExpansion":
        return TreeExpansion(
            tree=parsed_json
        )

    def to_primitives(self) -> Union[Dict, List]:
        return self.tree
