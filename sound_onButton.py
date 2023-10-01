#!/usr/bin/env python3

import argparse
import pygame
from gpiozero import Button
from signal import pause
import os
import random

parser = argparse.ArgumentParser(description='Directory for Sound Files')
parser.add_argument('path', metavar='Path', help='File Path')

args = parser.parse_args()
response =  args.path

button = Button("GPIO17")
dirArray = []
previousSounds = [1 , 2 , 3]

print(f"Building file list...")

for root, dirs, files in os.walk(dirPath):
    for file in files:
        if file.endswith(".wave"):
            filePath = "\"" + os.path.join(dirPath, file) + "\""
            print(filePath)
            dirArray.append(filePath)

arrayLength = int(len(dirArray))
print(f"{arrayLength} files discovered.")

print(f"Watching for Button!")

while True:
	if button.is_pressed:
	    print(f"Button Detected!")
        randomNum = random.randint(0, len(dirArray) - 1)
        fileName = dirArray[randomNum]
        print(f"Selected {fileName} for playback!")
    else:
        # do nothing

    


#def playSound(file):
#	pygame.mixer.init()
#	pygame.mixer.music.load(file)
#	pygame.mixer.music.play()
#
#	while pygame.mixer.music.get_busy() == True:
#		pass
#
#button.wait_for_press()
#playSound(response)
#