import pathlib

root = pathlib.Path(__file__).resolve().parent.parent / "src/main/resources/themes"

storm = {
    "101014": "171a28",
    "1a1b26": "24283b",
    "16161e": "1f2335",
    "14141b": "1b1e2d",
    "15161e": "1d202f",
    "1e202e": "292e42",
    "283457": "2e3c64",
    "232433": "2b3047",
    "363b54": "3b4261",
    "20303b": "293a4c",
    "1f2231": "2d364e",
    "37222c": "342d3f",
}

moon = {
    "101014": "161726",
    "1a1b26": "222436",
    "16161e": "1e2030",
    "14141b": "191b29",
    "15161e": "1b1d2b",
    "1e202e": "2f334d",
    "292e42": "2f334d",
    "283457": "2d3f76",
    "232433": "2a2c45",
    "363b54": "3b4261",
    "787c99": "828bb8",
    "c0caf5": "c8d3f5",
    "a9b1d6": "828bb8",
    "565f89": "636da6",
    "414868": "444a73",
    "bb9af7": "c099ff",
    "7aa2f7": "82aaff",
    "9ece6a": "c3e88d",
    "e0af68": "ffc777",
    "ff9e64": "ff966c",
    "f7768e": "ff757f",
    "db4b4b": "c53b53",
    "7dcfff": "86e1fc",
    "2ac3de": "65bcff",
    "73daca": "4fd6be",
    "3d59a1": "3e68d7",
    "ff899d": "ff8d94",
    "9fe044": "c7fb6d",
    "faba4a": "ffd8ab",
    "8db0ff": "9ab8ff",
    "c7a9ff": "caabff",
    "a4daff": "b2ebff",
    "449dab": "b8db87",
    "6183bb": "7ca1f2",
    "914c54": "e26a75",
    "20303b": "333b45",
    "1f2231": "2f3652",
    "37222c": "3e2e3f",
    "42465d": "444a73",
}

day = {
    "101014": "d0d5e3",
    "1a1b26": "e1e2e7",
    "16161e": "d0d5e3",
    "14141b": "ffffff",
    "15161e": "b4b5b9",
    "1e202e": "d5d9e4",
    "292e42": "c4c8da",
    "283457": "b7c1e3",
    "232433": "d2d5e1",
    "363b54": "a8aecb",
    "787c99": "68709a",
    "42465d": "b7c1e3",
    "c0caf5": "3760bf",
    "a9b1d6": "6172b0",
    "565f89": "848cb5",
    "545c7e": "8990b3",
    "737aa2": "68709a",
    "3b4261": "a8aecb",
    "414868": "a1a6c5",
    "3d59a1": "7890dd",
    "394b70": "92a6d5",
    "7aa2f7": "2e7de9",
    "2ac3de": "188092",
    "0db9d7": "07879d",
    "89ddff": "006a83",
    "7dcfff": "007197",
    "bb9af7": "9854f1",
    "9ece6a": "587539",
    "73daca": "387068",
    "e0af68": "8c6c3e",
    "ff9e64": "b15c00",
    "f7768e": "f52a65",
    "db4b4b": "c64343",
    "ff899d": "ff4774",
    "9fe044": "5c8524",
    "faba4a": "a27629",
    "8db0ff": "358aff",
    "c7a9ff": "a463ff",
    "a4daff": "007ea8",
    "449dab": "4197a4",
    "6183bb": "506d9c",
    "914c54": "c47981",
    "20303b": "b7ced5",
    "1f2231": "d5d9e4",
    "37222c": "dababe",
}


def substitute(text, mapping):
    for old, new in mapping.items():
        text = text.replace(old, new)
        text = text.replace(old.upper(), new)
    return text


def moon_fixups(json_out, xml_out):
    xml_out = xml_out.replace(
        '<option name="TEXT">\n      <value>\n        <option name="FOREGROUND" value="828bb8"/>',
        '<option name="TEXT">\n      <value>\n        <option name="FOREGROUND" value="c8d3f5"/>',
    )
    return json_out, xml_out


def day_fixups(json_out, xml_out):
    json_out = json_out.replace('"dark": true', '"dark": false')
    json_out = json_out.replace(
        '"parentTheme": "Islands Dark"', '"parentTheme": "Islands Light"'
    )
    json_out = json_out.replace(
        '"Button.default.foreground": "fg"', '"Button.default.foreground": "#ffffff"'
    )
    xml_out = xml_out.replace('parent_scheme="Darcula"', 'parent_scheme="Default"')
    return json_out, xml_out


variants = [
    ("storm", "Storm", storm, None),
    ("moon", "Moon", moon, moon_fixups),
    ("day", "Day", day, day_fixups),
]

for suffix, name, mapping, fixups in variants:
    json_out = substitute((root / "tokyo-night.theme.json").read_text(), mapping)
    json_out = json_out.replace('"name": "Tokyo Night"', f'"name": "Tokyo Night {name}"')
    json_out = json_out.replace(
        '"editorScheme": "/themes/tokyo-night.xml"',
        f'"editorScheme": "/themes/tokyo-night-{suffix}.xml"',
    )
    xml_out = substitute((root / "tokyo-night.xml").read_text(), mapping)
    xml_out = xml_out.replace(
        '<scheme name="Tokyo Night"', f'<scheme name="Tokyo Night {name}"'
    )
    if fixups:
        json_out, xml_out = fixups(json_out, xml_out)
    (root / f"tokyo-night-{suffix}.theme.json").write_text(json_out)
    (root / f"tokyo-night-{suffix}.xml").write_text(xml_out)

print("generated")
