#!/usr/bin/env python3
import sys, time, argparse, errno, os
from pathlib import Path

def print_file(file, speed):
    if not Path(file).is_file():
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file)
    else:
        with open(file, "r") as rfile:
            done = False
            while not done:
                pos = rfile.read(1)
                sys.stdout.write(pos)
                sys.stdout.flush()
                if not pos:
                    done = True
                time.sleep(speed)

def print_input(input, speed):
    for letter in input:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(speed)

parser = argparse.ArgumentParser()
parser.add_argument("input", help="string or name of file to be printed.")
parser.add_argument("-f", "--file", help="specifies that the input is a file. If not used, input is interpreted as string.", action='store_true')
parser.add_argument("-s", "--speed", help="delay between printing each character in seconds. defaults to 0.1 if not specified.", type=float)
args = parser.parse_args()
if not args.speed:
    args.speed = 0.1
if args.file:
    print_file(args.input, args.speed)
else:
    print_input(args.input, args.speed)



