from colorflip import Switcher
from colorflip.config import settings


def main():
    switcher = Switcher(settings)
    switcher.switch_themes()
