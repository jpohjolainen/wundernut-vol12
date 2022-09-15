#!python3
####
# Program to solve a puzzle of Wundernut vol. 12
#

import argparse
import wordninja

from PIL import Image
from pytesseract import image_to_string


def main():
    parser = argparse.ArgumentParser(description='Wondernut-vol12')
    parser.add_argument('imagefile')
    args = parser.parse_args()

    print(f"Reading '{args.imagefile}'...")
    im = Image.open(args.imagefile)

    width = im.size[0]
    height = im.size[1]

    print('Mangling colors...')
    bg = im.getpixel((0,0)) # background color from first pixel
    for x in range(0, width):
        for y in range(0, height):
            if bg == im.getpixel((x, y)): # Turn background color to white
                im.putpixel((x, y), (255, 255, 255))
            else: # If deviates from bg color, change to black
                im.putpixel((x, y), (0, 0, 0))

    print(f"Resizing {width}x{height} to {width//3}x{height//2}...")
    im_res = im.resize((width//3, height//2))
    im.close() # close original image

    print('Reading text from image...')
    conf = "--psm 6"
    encoded_text = image_to_string(im_res, config=conf)
    print('Text found:')
    print(encoded_text)

    print('Decoding...')
    # Scrolling through alphabet range and rotate each letter by the number
    # forward. wrap around alphabets: Z->A
    for x in range(27):
        decoded = ''
        for i in encoded_text:
            if i not in ['\n', '\r']:
                # Only circle around capital letters and not whole ascii table
                o = 65 + ((ord(i) + x) - 65) % 26
                decoded += chr(o)
        if 'THE' in decoded: # Find english text
            print(f"Using ROT{x} found a match:\n")
            sp = wordninja.split(decoded)
            # print in 10 words per line
            for i in range(0, len(sp), 10):
                print(' '.join(sp[i:i+10]))
            break


if __name__ == '__main__':
    main()
