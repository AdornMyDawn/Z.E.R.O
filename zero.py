# the brains
import sys
from skills import math_tools, notes

def main():
    print("At your service, ma'am")
    while True: 
        command = input(">>>").lower()
        if command in ["quit exit q"]:
            print("Goodnight maam")
            sys.exit()

