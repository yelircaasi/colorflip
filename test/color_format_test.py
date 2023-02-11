import pytest

from swytchswatch.utils.color_format import ColorCode


@pytest.mark.parametrize(
    "input_code,output_code",
    [
        ("defabc", "0xdefabc"),
        ("3f5d31", "0x3f5d31"),
        ("112233", "0x112233"),
        ("0xabcdef", "0xabcdef"),
        ("0xa1b2c3", "0xa1b2c3"),
        ("0x123456", "0x123456"),
        ("#12df34", "0x12df34"),
        ("#3ed421", "0x3ed421"),
        ("#adf780", "0xadf780"),
        ((0, 50, 100), "0x003264"),
        ((255, 255, 255), "0xffffff"),
        ((0, 0, 0), "0x000000"),
    ],
)
def test_colorcode_as_0x(input_code, output_code):
    cc = ColorCode(input_code)
    assert cc.as_0x() == output_code.upper()
    assert cc.as_0x(uppercase=False) == output_code.lower()


@pytest.mark.parametrize(
    "input_code,output_code",
    [
        ("defabc", "#defabc"),
        ("3f5d31", "#3f5d31"),
        ("112233", "#112233"),
        ("0xabcdef", "#abcdef"),
        ("0xa1b2c3", "#a1b2c3"),
        ("0x123456", "#123456"),
        ("#12df34", "#12df34"),
        ("#3ed421", "#3ed421"),
        ("#adf780", "#adf780"),
        ((0, 50, 100), "#003264"),
        ((255, 255, 255), "#ffffff"),
        ((0, 0, 0), "#000000"),
    ],
)
def test_colorcode_as_octo(input_code, output_code):
    cc = ColorCode(input_code)
    assert cc.as_octo() == output_code.upper()
    assert cc.as_octo(uppercase=False) == output_code.lower()


@pytest.mark.parametrize(
    "input_code,output_code",
    [
        ("defabc", (222, 250, 188)),
        ("3f5d31", (63, 93, 49)),
        ("112233", (17, 34, 51)),
        ("0xabcdef", (171, 205, 239)),
        ("0xa1b2c3", (161, 178, 195)),
        ("0x123456", (18, 52, 86)),
        ("#12df34", (18, 223, 52)),
        ("#3ed421", (62, 212, 33)),
        ("#adf780", (173, 247, 128)),
        ((0, 50, 100), (0, 50, 100)),
        ((255, 255, 255), (255, 255, 255)),
        ((0, 0, 0), (0, 0, 0)),
        ((0, 50, 100, 0.7), (0, 50, 100, 0.7)),
        ((255, 255, 255, 0), (255, 255, 255, 0)),
        ((0, 0, 0, 1), (0, 0, 0, 1)),
    ],
)
def test_colorcode_as_tuple(input_code, output_code):
    cc = ColorCode(input_code)
    assert cc.as_parens() == str(output_code[:3])
    assert cc.as_parens(return_type=tuple) == output_code[:3]
    assert cc.as_parens(with_opacity=True) == str(output_code if len(output_code) == 4 else (*output_code, 1))
    assert (
        cc.as_parens(return_type=tuple, with_opacity=True) == output_code
        if len(output_code) == 4
        else (*output_code, 1)
    )
