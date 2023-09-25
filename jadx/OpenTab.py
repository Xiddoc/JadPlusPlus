"""
A tree expansion in the source code tree panel.
"""
from dataclasses import dataclass
from typing import Dict, Any, List, Union

from jadx.ProjectComponent import ProjectComponent


@dataclass
class TabViewPosition(ProjectComponent):
    x: int
    y: int

    @staticmethod
    def from_json(parsed_json: Dict[str, Any]) -> "TabViewPosition":
        return TabViewPosition(
            x=parsed_json["x"],
            y=parsed_json["y"]
        )

    def to_primitives(self) -> Union[Dict, List]:
        return {
            "x": self.x,
            "y": self.y,
        }


@dataclass
class OpenTab(ProjectComponent):
    type: str
    tab_path: str
    sub_path: str
    caret: int
    view: TabViewPosition

    @staticmethod
    def from_json(parsed_json: Dict[str, Any]) -> "OpenTab":
        return OpenTab(
            type=parsed_json["type"],
            tab_path=parsed_json["tabPath"],
            sub_path=parsed_json["subPath"],
            caret=parsed_json["caret"],
            view=TabViewPosition.from_json(parsed_json["view"]),
        )

    def to_primitives(self) -> Union[Dict, List]:
        return {
            "type": self.type,
            "tabPath": self.tab_path,
            "subPath": self.sub_path,
            "caret": self.caret,
            "view": self.view.to_primitives()
        }
