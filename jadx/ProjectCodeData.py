"""
The JadX project's code data.

This includes most of the relevant project work, such as comments and renames.
"""
from dataclasses import dataclass
from typing import List, Any


@dataclass
class ProjectCodeData:
    comments: List[Any]
    renames: List[Any]
