from functools import partial

from dynaconf import Dynaconf
from funcy import lmap

from colorflip.rules import build_rule


class Switcher:
    def __init__(self, cfg: Dynaconf) -> None:
        self.cfg = cfg
        app_names = cfg.apps.keys()
        self.rules = lmap(partial(build_rule, cfg_obj=cfg), app_names)

    def switch_themes(self):
        for rule in self.rules:
            rule(preview=self.cfg.preview)
