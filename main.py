# Author: 0x44F

from __future__ import absolute_import, unicode_literals
from steganography.steganography import Steganography as stego

PAYLOAD     =   'alert(0);'      # Insert your payload here, example 'alert(0);'
CHARCODE    =   '\x00\x32\x38\xF1\xA3\xC7\xF4\x00\xFF\xFF\xFF'

MAX_LEN     =   128

if __name__ == '__main__':
    if(len(payload) > 128):
        quit("Payload too long!")
    
    target_image = input("Target Image Path > ")     # Grab target image (meow)
    output_path = input("Output Path > ")            # Get path to save image (e.g: C:\Documents\my_hacked_image.jpg)
    
    stego.encode(target_image, output_path, PAYLOAD + str(CHARCODE))
    print("Finished process! [READ TEXT TO SEE IF ITS CORRECT]")
    print("We found your payload! It was: {}".format(str(stego.decode(output_path))))
    
    print("If the above text is [incorrect] please try again using path you have access to.")
    return
