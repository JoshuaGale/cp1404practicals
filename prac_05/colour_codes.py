COLOUR_CODES = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "azure1": "#f0ffff",
                    "beige": "#f5f5dc", "bisque1": "#ffe4c4", "black": "#000000", "blanchedalmond": "#ffebcd",
                    "blue1": "#0000ff", "blueviolet": "#8a2be2", "brown": "#a52a2a"}


def main():
    color_name = input("Enter a color name: ")

    while color_name != "":

        if color_name in COLOUR_CODES:

            print("The code for {} is {}".format(color_name, COLOUR_CODES[color_name]))

        else:

            print("Invalid color name")

        color_name = input("Enter a color name: ")

main()
