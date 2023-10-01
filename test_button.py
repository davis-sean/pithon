#!/usr/bin/env python3

import argparse
from gpiozero import Button
from signal import pause

parser = argparse.ArgumentParser(description='Play MP3')
parser.add_argument('input', metavar='Input', help='File Name')

args = parser.parse_args()
response =  args.input

button = Button("GPIO17")

while True:
	button.wait_for_press()
	print(f"Button Detected")
