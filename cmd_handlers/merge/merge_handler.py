"""
Perform the merge operation on 2 or more files.
"""
import argparse
from typing import TextIO, List

from cmd_handlers.merge import merger
from jadx.JadxProject import JadxProject


def get_projects_from_args(args: argparse.Namespace) -> List[JadxProject]:
    files: List[TextIO] = args.project_files

    return [JadxProject.from_stringified_json(file.read())
            for file in files]


def write_merged_project(out_file: TextIO, merged_project: JadxProject) -> None:
    """
    Write the merged_project project to the output file.
    """
    out_file.write(merged_project.to_stringified_json())


def merge_handler(args: argparse.Namespace) -> None:
    """
    Merge 2 or more JadX projects to one, then write it to a file.
    """
    projects = get_projects_from_args(args)

    merged_project = merger.merge_projects(projects)

    write_merged_project(args.out_project_file, merged_project)
