from functools import partial

from dynaconf import Dynaconf
from funcy import lmap

from colorflip.rules import build_rule


class Switcher:
    def __init__(self, cfg: Dynaconf) -> None:
        self.cfg = cfg
        app_names = cfg.apps.keys()
        self.rules = lmap(partial(build_rule, cfg_object=cfg), app_names)
        print(app_names)

    def end2end(self):
        print("end2end")
        double_line = 40 * "="
        print(f"\n\n{double_line}\nGENERATE\n{double_line}")
        self.generate()
        print(f"\n\n{double_line}\nBACKUP\n{double_line}")
        self.backup()
        print(f"\n\n{double_line}\nOVERWRITE\n{double_line}")
        self.overwrite()
        print(f"\n\n{double_line}\n\n")
        # for rule in self.rules:
        #    rule(preview=self.cfg.preview)

    def generate(self):
        print("generate")

    def backup(self):
        print("backup")

    def overwrite(self):
        print("overwrite")

    def revert(self):
        print("revert")
