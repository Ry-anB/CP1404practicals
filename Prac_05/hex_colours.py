""" CP1404 - Practical 05 - Hex Colours """

COLOUR_NAME_TO_HEX_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a",
                           "AliceBlue": "#f0f8ff", "Alizarin crimson": "#e32636",
                           "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc",
                           "AntiqueWhite": "#faebd7", "Apricot": "#fbceb1", "Aqua": "#00ffff"}
colour_name = input("Enter a colour name: ").title()
while colour_name != "":
    try:
        print(f"{colour_name} is equal to {COLOUR_NAME_TO_HEX_CODE[colour_name]}")
    except KeyError:
        print("Colour name is not listed")
    colour_name = input("Enter a colour name: ").title()
