#!/usr/bin/env python3

import argparse
import pygame
from gpiozero import Button
from signal import pause

parser = argparse.ArgumentParser(description='Play MP3')
parser.add_argument('input', metavar='Input', help='File Name')

args = parser.parse_args()
response =  args.input

button = Button("GPIO2")

def playSound(file):
	pygame.mixer.init()
	pygame.mixer.music.load(file)
	pygame.mixer.music.play()

	while pygame.mixer.music.get_busy() == True:
		pass

button.wait_for_press()
playSound(response)
