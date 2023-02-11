# swytchswatch

Python library to change the color theme - everywhere.

This project was written by the author for himself, so use at your own risk.

**THIS IS A WORK IN PROGRESS. IT DOES NOT YET WORK. SUGGESTIONS ARE WELCOME.**
## Supported applications

### Desktop

* [Alacritty](https://)
* [Zathura](https://)
* [vifm](https://)
* [qutebrowser](https://)
* [neovim](https://)
* [xmonad](https://)
* [xmobar](https://)
* [gedit](https://)
* [tmux](https://)
* [Starship](https://)

### Browser Extensions

.

## Adding applications and rules

Rules are simply Python functions defining how to change a given configuration.
Examples are shown in `./examples/user_rules`, with the corresponding
configuration in `./examples/example_user_config.toml`, which is declared in the
`.env` file in the same directory.
