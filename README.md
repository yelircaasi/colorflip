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

* [Wikipedia](https://wikipedia.org)
* Github
* Stack Overflow
* Reddit
* Confluence
* Bitbucket
* Read the Docs
* Hugging Face
* PyPI
* .
* Jira
* Gitlab
* YouTube
* Twitter
* Goodreads
* [Notion](https://notion.com)
* [Google Drive](https://)
* Google Sheets
* Google Docs
* Microsoft Teams
* Dive into Deep Learning
* Rosetta Code
* Python Docs
* Julia Docs
* Rosetta Code
* The Algorithms
* Stanford Sites

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

Follow the webdriver installation instructions from Selenium. For example (version numbers will change,
but this is illustrates the overall process):

```sh
# browser drivers
cd /tmp
wget https://chromedriver.storage.googleapis.com/110.0.5481.77/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
mv chromedriver ~/.local/bin
wget https://github.com/mozilla/geckodriver/releases/download/v0.32.2/geckodriver-v0.32.2-linux64.tar.gz
tar -xf geckodriver-v0.32.2-linux64.tar.gz
mv geckodriver ~/.local/bin
wget https://msedgedriver.azureedge.net/110.0.1587.50/edgedriver_linux64.zip
unzip edgedriver_linux64.zip
mv msedgedriver ~/.local/bin
```

## Command-Line Usage

### Run full process end-to-end

```sh
colorflip flip [PATH_TO_CONFIG_TOML]
```

### Create new style sheets

```sh
colorflip generate [PATH_TO_CONFIG_TOML]
```

### Back up current configs, saving them in .colorflip/history folder (default under $HOME) for ease of reversion

```sh
colorflip backup [PATH_TO_CONFIG_TOML]
```

### Revert to earlier color scheme

```sh
colorflip revert [PATH_TO_CONFIG_TOML]
```

Each command has the option `--log LOG_LEVEL`

## Development Roadmap

1. write Installation section
2. define CLI
3. develop CLI up to imports of functionality code -> [link](https://realpython.com/python-typer-cli/)
   [link2](https://jrwalk.github.io/pages/projects/python-cli-utilities-poetry-typer)
   1. write script
   2. define script installation in TOML
   3. prototype selenium
