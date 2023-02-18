from dynaconf import Dynaconf


class OverwriteCallable:
    def __init__(self, cfg: Dynaconf) -> None:
        ...
