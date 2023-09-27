from typing import List

from jadx.JadxProject import JadxProject
from jadx.OpenTab import OpenTab
from jadx.ProjectCodeData import ProjectCodeData
from jadx.TreeExpansion import TreeExpansion


def merge_project_version(projects: List[JadxProject]) -> int:
    return max(prj.project_version for prj in projects)


def merge_files(projects: List[JadxProject]) -> List[str]:
    return [file for project in projects for file in project.files]


def merge_tree_expansions(projects: List[JadxProject]) -> List[TreeExpansion]:
    return [tree for project in projects for tree in project.tree_expansions]


def merge_code_data(projects: List[JadxProject]) -> ProjectCodeData:
    merged_code_data = projects[0].code_data

    return merged_code_data


def merge_open_tabs(projects: List[JadxProject]) -> List[OpenTab]:
    return [file for project in projects for file in project.open_tabs]


def merge_active_tab(projects: List[JadxProject]) -> int:
    return min(prj.active_tab for prj in projects)


def merge_cache_dir(projects: List[JadxProject]) -> str:
    """
    Return the first cache directory found.
    Worst case, JadX will regenerate the cache on re-opening the project.
    """
    first_project, _ = projects
    first_project: JadxProject

    return first_project.cache_dir


def merge_enable_live_reload(projects: List[JadxProject]) -> bool:
    return all(prj.enable_live_reload for prj in projects)


def merge_search_history(projects: List[JadxProject]) -> List[str]:
    return [search_history for project in projects for search_history in project.search_history]


def merge_projects(projects: List[JadxProject]) -> JadxProject:
    """
    Converges a few JadX projects into one project.
    """
    return JadxProject(
        project_version=merge_project_version(projects),

        files=merge_files(projects),
        tree_expansions=merge_tree_expansions(projects),
        code_data=merge_code_data(projects),
        open_tabs=merge_open_tabs(projects),

        active_tab=merge_active_tab(projects),
        cache_dir=merge_cache_dir(projects),
        enable_live_reload=merge_enable_live_reload(projects),
        search_history=merge_search_history(projects)
    )
