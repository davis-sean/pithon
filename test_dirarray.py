#!/usr/bin/env python3

import argparse
import os
import random

parser = argparse.ArgumentParser(description='Define Directory')
parser.add_argument('path', metavar='Path', help='Path')

args = parser.parse_args()
dirPath =  args.path
dirArray = []

print(f"Building file list...")

for root, dirs, files in os.walk(dirPath):
    for file in files:
        if file.endswith(".py"):
            filePath = "\"" + os.path.join(dirPath, file) + "\""
            print(filePath)
            dirArray.append(filePath)
            
print(f"The full file array is:")
print(dirArray)
print(f"The array length is:")
arrayLength = int(len(dirArray))
print(arrayLength)
randomNum = random.randint(0, len(dirArray) - 1)
print(f"A random number generated for 0 through {arrayLength}.")
print(randomNum)
print(f"Recall random value from array:")
print(dirArray[randomNum])