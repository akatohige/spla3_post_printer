#!/bin/bash

python3 convert.py -i img/post.png
make

cp Joystick.hex mnt/Joystick.hex

#dfu-programmer atmega16u2 erase
#dfu-programmer atmega16u2 flash Joystick.hex
#dfu-programmer atmega16u2 reset