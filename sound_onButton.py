#!/usr/bin/env python3

import argparse
import pygame
from gpiozero import Button
import os
import random
from time import sleep
import textwrap

parser = argparse.ArgumentParser(description='Directory for Sound Files')
parser.add_argument('path', metavar='Path', help='File Path')

args = parser.parse_args()
dirPath =  args.path

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
button = Button("GPIO17")
dirArray = []
previousSounds = [1 , 2 , 3]

print(f"Building file list...")

for root, dirs, files in os.walk(dirPath):
    for file in files:
        if file.endswith(".wav"):
            # filePath = "\'" + os.path.join(dirPath, file) + "\'"
            filePath = os.path.join(dirPath, file)
            dirArray.append(filePath)

arrayLength = int(len(dirArray))
print(f"{arrayLength} files discovered.")

if (arrayLength == 0):
    print(f"No Files Detected!")
    exit()

print(f"Watching for Button!")

while True:
    if button.is_pressed:
        print(f"Button Detected!")
        randomNum = random.randint(0, len(dirArray) - 1)
        if randomNum not in previousSounds:
            fileName = str(dirArray[randomNum])
            fileName.strip()
            previousSounds.insert(0, randomNum)
            previousSounds = previousSounds[:-1]
            print(f"Selected FireOnHigh for playback!")
            sound = pygame.mixer.Sound("/home/davis-admin/pithon/fire.wav")
            sound.play
            while sound.get_busy() == True:
                pass
    else:
        value = 1
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