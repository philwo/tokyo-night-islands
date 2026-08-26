import pathlib

root = pathlib.Path.home() / "src/tokyo-night-islands/src/main/resources/themes"

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


def substitute(text, mapping):
    for old, new in mapping.items():
        text = text.replace(old, new)
        text = text.replace(old.upper(), new)
    return text


for suffix, name, mapping in [("storm", "Storm", storm), ("moon", "Moon", moon)]:
    json_src = (root / "tokyo-night.theme.json").read_text()
    json_out = substitute(json_src, mapping)
    json_out = json_out.replace('"name": "Tokyo Night"', f'"name": "Tokyo Night {name}"')
    json_out = json_out.replace(
        '"editorScheme": "/themes/tokyo-night.xml"',
        f'"editorScheme": "/themes/tokyo-night-{suffix}.xml"',
    )
    (root / f"tokyo-night-{suffix}.theme.json").write_text(json_out)

    xml_src = (root / "tokyo-night.xml").read_text()
    xml_out = substitute(xml_src, mapping)
    xml_out = xml_out.replace(
        '<scheme name="Tokyo Night"', f'<scheme name="Tokyo Night {name}"'
    )
    if suffix == "moon":
        xml_out = xml_out.replace(
            '<option name="TEXT">\n      <value>\n        <option name="FOREGROUND" value="828bb8"/>',
            '<option name="TEXT">\n      <value>\n        <option name="FOREGROUND" value="c8d3f5"/>',
        )
    (root / f"tokyo-night-{suffix}.xml").write_text(xml_out)

print("generated")
