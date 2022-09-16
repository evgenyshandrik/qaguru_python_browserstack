"""
Class for work with files
"""
from pathlib import Path


def abs_path_from_project(relative_path: str):
    """
    Get absolute path
    """

    return (
        Path(__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
