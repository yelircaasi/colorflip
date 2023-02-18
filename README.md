# colorflip

Python library to change the color theme - everywhere.

This project was written by the author for himself, so use at your own risk.

**THIS IS A WORK IN PROGRESS. IT DOES NOT YET WORK. SUGGESTIONS ARE WELCOME.**

## Supported applications

### Desktop Applications

* [Alacritty](https://)
* [Zathura](https://)
* [vifm](https://)
* [qutebrowser](https://)
* [neovide](https://)
* [xmonad](https://)
* [xmobar](https://)
* [gedit](https://)
* [tmux](https://)
* [Starship](https://)

### Browsers

* [Qutebrowswer](https://)
* [Nyxt](https://)
* [Luakit](https://)
* [Chrome](https://)
* [Firefox](https://)
* [Edge](https://)

### Websites

.

### Terminal-Based Utilities

* [Neovim](https://)
* [Lynx](https://)
* .

### Others

* .

## Adding applications and rules

Rules are simply Python functions defining how to change a given configuration.
Examples are shown in `./examples/user_rules`, with the corresponding
configuration in `./examples/example_user_config.toml`, which is declared in the
`.env` file in the same directory.

## Installation

```sh

```

## Command-Line Usage

```sh
colorflip
```

## Development Roadmap

1. write Installation section
2. define CLI
3. develop CLI up to imports of functionality code -> [link](https://realpython.com/python-typer-cli/)
   [link2](https://jrwalk.github.io/pages/projects/python-cli-utilities-poetry-typer)
   1. write script
   2. define script installation in TOML
   3. .
