import typer

from colorflip import Switcher
from colorflip.config import settings

switcher = Switcher(settings)
app = typer.Typer()


@app.command()
def end2end():
    switcher.end2end()


@app.command()
def generate():
    switcher.generate()


@app.command()
def backup():
    switcher.backup()


@app.command()
def overwrite():
    switcher.overwrite()


@app.command()
def revert():
    switcher.revert()


def main():
    app()


if __name__ == "__name__":
    main()
