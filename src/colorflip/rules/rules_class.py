from pathlib import Path
from typing import Callable, Tuple


class Rule:
    def __init__(
        self,
        app_name,
        tmp_root,
        backup_callable: Callable,
        editor_callable: Callable,
        preview_callable: Callable,
        overwrite_callable: Callable,
        reversion_callable: Callable,
    ) -> None:
        """ """
        self.name = app_name
        self._make_backups = backup_callable
        self._edit_copy = editor_callable
        self._preview_copy = preview_callable
        self._overwrite_original = overwrite_callable
        self._revert = reversion_callable
        self.temp_location = Path(tmp_root) / self.name

    def __call__(self, preview=False):
        """ """
        backup_path, working_path = self.make_backups()
        self.edit_copy(working_path)
        if preview:
            self.preview_copy(working_path)
        self.overwrite_original()

    def make_backups(self) -> Tuple[Path, Path]:
        """ """
        return self._make_backups()

    def edit_copy(self, copy_path: Path) -> None:
        """ """
        self._edit_copy(copy_path)

    def preview_copy(self, copy_path: Path) -> None:
        """ """
        self._preview_copy(copy_path)

    def revert(self, copy_path: Path) -> None:
        """ """
        self._revert(copy_path)
