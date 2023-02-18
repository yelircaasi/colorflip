import re
from textwrap import wrap
from typing import Iterable, Tuple, Union

CodeType = Union[str, Iterable]
NonstringType = Union[list, tuple]


class ColorCode:
    def __init__(self, code: CodeType) -> None:
        self.code = code
        self.opacity = None
        if isinstance(code, NonstringType):
            if len(code) == 3:
                self.rgb = tuple(code)
            elif len(code) == 4:
                self.opacity = code[-1]
                self.rgb = tuple(code[:3])
            else:
                raise ValueError("Color code tuple/list must have length 3 or 4")
        elif isinstance(code, str):
            self.rgb = self._parse_string(code)
        else:
            raise TypeError(
                "Invalid format encountered while parsing color code.\nValid types include `str`, `tuple`, and `list`."
            )
        if not all(map(lambda x: x in range(256), self.rgb)):
            raise ValueError("Color values must be between 0 and 255 (both inclusive).")
        self.r, self.g, self.b = self.rgb

    @staticmethod
    def _parse_string(code: str) -> Tuple[int, int, int]:
        code = code.strip()
        if not code:
            raise ValueError("Empty color codes are not valid.")
        for start in ["#", "0x", ""]:
            if re.match(start or "[0-9A-Fa-f]", code):
                regexpr = re.compile(f"{start}[0-9A-Fa-f]{{6}}")
                if not re.match(regexpr, code):
                    raise ValueError(
                        f"Color code beginning with '{start or 'H'}' must be of the form '{start}HHHHHH', where 'H' is a hexadecimal digit."
                    )
                code = re.split("[Xx#]", code)[-1]
                return tuple(map(lambda h: int(h, base=16), wrap(code, width=2)))
        else:
            raise ValueError("Color code beginning with '{code[0]}' is not valid.")

    @staticmethod
    def _to_hex(decimal_triplet, prefix, uppercase):
        code = prefix + "".join(map(lambda i: hex(i)[2:].zfill(2), decimal_triplet))
        return code.upper() if uppercase else code.lower()

    def as_0x(self, uppercase=True) -> str:
        return self._to_hex(self.rgb, "0x", uppercase)

    def as_html(self, uppercase=True) -> str:
        return self._to_hex(self.rgb, "#", uppercase)

    def as_rgb(self, return_type: Union[str, tuple] = str, with_opacity=False) -> Union[str, tuple]:
        if with_opacity:
            return return_type((*self.rgb, 1 if self.opacity is None else self.opacity))
        return return_type(self.rgb)

    def as_hsl():
        ...

    def as_cmyk():
        ...
