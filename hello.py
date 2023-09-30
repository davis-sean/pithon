#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='Echo back what was typed on the command line.')
parser.add_argument('response', metavar='Input', help='Tell me what to say')

args = parser.parse_args()

response =  args.response

print (f"{response}")