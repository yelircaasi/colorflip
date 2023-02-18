from dynaconf import Dynaconf

from .callable_builders import (
    BackupCallable,
    EditorCallable,
    OverwriteCallable,
    PreviewCallable,
    ReversionCallable,
)
from .rules_class import Rule


def build_rule(app_name: str, cfg_obj: Dynaconf):
    """ """
    backup_callable = BackupCallable(cfg_object)
    editor_callable = EditorCallable(cfg_object)
    preview_callable = PreviewCallable(cfg_object)
    overwrite_callable = OverwriteCallable(cfg_object)
    reversion_callable = ReversionCallable(cfg_object)
    tmp_root = cfg_object.paths.tmp_root

    return Rule(
        app_name, tmp_root, backup_callable, editor_callable, preview_callable, overwrite_callable, reversion_callable
    )
