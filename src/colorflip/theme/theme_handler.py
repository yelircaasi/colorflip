"""
theme = ColorTheme(file)
theme.colors.
"""
import tomlkit

from colorflip.utils.color_format import ColorCode
from colorflip.utils.validation import validate_theme_dict

# https://github.com/andreyvpng/just-colors/tree/master/templates


# TODO: consider converting to dataclass
class ColorTheme:
    def __init__(self, theme_toml) -> None:
        with open(theme_toml) as f:
            toml = tomlkit.load(f)

        if not validate_theme_dict(toml):
            raise ValueError(f"{theme_toml} does not contain the required fields for a color theme.")

        self.__dict__.update({k: ColorCode(v) for k, v in toml.items()})

        # self.base00 = toml["base00"]
        # self.base01 = toml["base01"]
        # self.base02 = toml["base02"]
        # self.base03 = toml["base03"]
        # self.base04 = toml["base04"]
        # self.base05 = toml["base05"]
        # self.base06 = toml["base06"]
        # self.base07 = toml["base07"]
        # self.base08 = toml["base08"]
        # self.base09 = toml["base09"]
        # self.base0A = toml["base0A"]
        # self.base0B = toml["base0B"]
        # self.base0C = toml["base0C"]
        # self.base0D = toml["base0D"]
        # self.base0E = toml["base0E"]
        # self.base0F = toml["base0F"]
