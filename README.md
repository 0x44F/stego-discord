# "Stego", A new Discord exploit.
This script uses steganography and a Discord client vulnerability in order to run javascript on all computers viewing a certain image within Discord.
Do not confuse this with my previous exploit (now patched) 'Otax', this is completely new and currently working. All you need is Python 3.7+ and an
image that is no bigger than 600x1200 pixels. 

## How does this work?
Simple, really, first you give the script a path to your target image (I have provided one) and then a one-liner JS script no bigger than 128 characters.
The program takes in a number of factors (Red, Green, Blue pixels) and modifies the image to contain a script that will be run after being saved to cache.

> ### Vulnerability overview
> ```
> Discovered: 29/8/2022
> Severity: Critical
> Public: 29/8/2022
> ```

### But what is the vulnerability?
The vulnerability is the fact that when you send an image over Discord inside of a channel, it checks for explicit imagery. By using the method described below, you can create an image 50% of the time that will trigger their explicit filters but not stop you from sending it. It is called 'silent detection' and has been used in the past to catch child predators.

Basically it causes Discord clients to instantly a `/science` request to Discord, and normally Discord would review and watch the content. When Discord sends a reply to the `/science` request, it contains certain instructions, which usually includes logging an 'epoch' (timestamp) and client update instructions. When the Discord server sees this image, the script has taken advantage of the system and uses steganography to cause Discord to implement a user-chosen script.

TL;DR - The script takes advantage of a silent alarm system within Discord to cause your script to be ran.

## Selecting an image
I recommend using the image provided inside of this repository, however if you are picky and want another image, heres what you need to do:
- Pick an image
- Go to [Lunapic](https://www12.lunapic.com/editor/?action=quality) and decrease quality to 35%
- Resize image to smaller than 600x1200 pixels (for example, 400x300 pixels)
- Reupload image to lunapic, decrease quality to 50%
- Download image
