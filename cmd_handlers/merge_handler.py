"""
Perform the merge operation on 2 or more files.
"""
import argparse
from typing import TextIO, List

from jadx.JadxProject import JadxProject


def merge_handler(args: argparse.Namespace) -> None:
    """
    Merge 2 or more files.
    """
    files: List[TextIO] = args.project_files

    projects = [JadxProject.from_stringified_json(file.read())
                for file in files]

    print(projects)

    print(projects[0].to_primitives())
