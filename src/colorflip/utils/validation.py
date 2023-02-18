from pathlib import Path
from typing import Union

from dynaconf import Dynaconf

# from .color_format import ColorCode

PathType = Union[str, Path]


def validate_theme(toml_file: PathType) -> bool:
    is_valid = True  # TODO: implement

    return is_valid


def validate_theme_dict(theme: dict) -> bool:
    is_valid = True

    return is_valid


def validate_app_rules(toml_file: PathType) -> bool:
    is_valid = True  # TODO: implement

    return is_valid


def validate_settings_obj(settings_obj: Dynaconf) -> bool:
    is_valid = True  # TODO: implement

    return is_valid
