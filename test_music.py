#!/usr/bin/env python3

import argparse
import pygame

parser = argparse.ArgumentParser(description='Play MP3')
parser.add_argument('input', metavar='Input', help='File Name')

args = parser.parse_args()
response =  args.input

pygame.mixer.init()
pygame.mixer.music.load(response)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy() == True:
	pass

