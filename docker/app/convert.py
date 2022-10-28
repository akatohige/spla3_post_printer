#!/bin/python

import sys, os, argparse
from PIL import Image

def parse_args():
    parser = argparse.ArgumentParser(description="Splatoon Post Printer")
    parser.add_argument("-i", "--image", help="binary image name")
    return parser.parse_args()

def main():
    args = parse_args()

    # Open an image
    image = Image.open(args.image)
    if not (image.size[0] == 320 and image.size[1] == 120):
        print("ERROR: Image size must be 320x120 pixel.")
        sys.exit()

    # Convert to bilevel image
    image = image.convert("1")
    image_data = image.load()

    rawdata = []
    for y in range(0, 120):
        for x in range(0, 320):
            rawdata.append(0 if image_data[x, y] == 255 else 1)

    # Append image data
    code_str = "#include <stdint.h>\n#include <avr/pgmspace.h>\n\nconst uint8_t image_data[4801] PROGMEM = {"
    for i in range(0, (320 * 120) // 8):
        value = 0
        for j in range(0, 8):
            value |= rawdata[(i * 8) + j] << j
        value = value & 0xFF
        code_str += hex(value) + ", "

    # Append End of bytes
    code_str += "0x00};\n"

    # Output an image data into image.c
    with open("image.c", "w") as f:       
        f.write(code_str)

if __name__ == "__main__":
    main()
