"""
The JadX project's code data.

This includes most of the relevant project work, such as comments and renames.
"""
from dataclasses import dataclass
from typing import List, Any, Dict, Union

from jadx.ProjectComponent import ProjectComponent


@dataclass
class ProjectCodeData(ProjectComponent):
    comments: List[Any]
    renames: List[Any]

    @staticmethod
    def from_json(parsed_json: Dict[str, Any]) -> "ProjectCodeData":
        return ProjectCodeData(
            comments=parsed_json["comments"],
            renames=parsed_json["renames"]
        )

    def to_primitives(self) -> Union[Dict, List]:
        return {
            "comments": self.comments,
            "renames": self.renames
        }
