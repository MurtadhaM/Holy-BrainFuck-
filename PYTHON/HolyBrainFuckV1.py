"""
Author: Murtadha Marzouq
Description: Python BrainFuck Interpreter to experement with Dynamically typed langauges
"""


import os
import sys
import argparse


def BrainFuckInterpreter(code):
    tape = [0] * 30000
    pointer = 0
    output = ""

    i = 0
    while i < len(code):
        c = code[i]

        if c == ">":
            pointer += 1
        elif c == "<":
            pointer -= 1
        elif c == "+":
            tape[pointer] += 1
        elif c == "-":
            tape[pointer] -= 1
        elif c == ".":
            output += chr(tape[pointer])
        elif c == ",":
            tape[pointer] = ord(input())
        elif c == "[":
            if tape[pointer] == 0:
                loop_count = 1
                while loop_count > 0:
                    i += 1
                    if code[i] == "[":
                        loop_count += 1
                    elif code[i] == "]":
                        loop_count -= 1
        elif c == "]":
            loop_count = 1
            while loop_count > 0:
                i -= 1
                if code[i] == "[":
                    loop_count -= 1
                elif code[i] == "]":
                    loop_count += 1
            i -= 1

        i += 1

    return output


def BrainFuckInterpreterToAscii(code):
    output = BrainFuckInterpreter(code)
    ascii_output = ""
    for char in output:
        ascii_output += str(ord(char)) + " "
    return ascii_output


def setup():
    parser = argparse.ArgumentParser(description='BrainFuck Interpreter')
    parser.add_argument('-f', '--file', type=str,
                        help='BrainFuck file to interpret')
    parser.add_argument('-i', '--interactive',
                        action='store_true', help='Interactive mode')
    return parser.parse_args()


def print_banner():
    with open('./banner.txt', 'r') as f:
        print(f.read())


def main(args):
    if args.interactive:
        print_banner()
        while True:
            code = input('> ')
            interpreter = BrainFuckInterpreter(code)
            print(interpreter)
            sys.exit(0)
    elif args.file:
        with open(args.file, 'r') as f:
            code = f.read()
            interpreter = BrainFuckInterpreter(code)
            print(interpreter)

            sys.exit(0)
    else:
        print('Please provide a BrainFuck file or use interactive mode.')
        print("usage: python3 HolyBrainFuck.py -f <filename> | -i <interactive Mode>")


if __name__ == '__main__':
    args = setup()
    main(args)
