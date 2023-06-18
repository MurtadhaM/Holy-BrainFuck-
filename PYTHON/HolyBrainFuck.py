"""
Author: Murtadha Marzouq
Description: Python BrainFuck Interpreter to experement with Dynamically typed langauges
"""

import sys
import argparse


class Program():
    # Print out the banner.txt file to the console
    # Used to display the banner at the start of the script
    def print_banner(self):
        with open('./banner.txt', 'r') as f:
            print(f.read())

    # Initialize the interpreter. If a filename was passed in, read it.
    def __init__(self):
        self.filename = args.filename
        self.prgPos = 0
        self.mem = [0]
        self.memPos = 0
        if self.filename:
            self.prg = self.read_file()
        self.countOpened = 0

    # Read the Brainfuck program from a file
    def read_file(self):
        f = open(self.filename, "r")
        prg = f.read()
        f.close()
        return prg

    # Increment the value at the current memory position
    def increment(self):
        self.memPos += 1
        if len(self.mem) <= self.memPos:
            self.mem.append(0)

    # Decrement the value at the current memory position
    def decrement(self):
        self.memPos -= 1
        if self.memPos < 0:
            print("Error: Moved off tape!")
            sys.exit(0)

    # Subtract 1 from the value at the current memory position
    def subtract(self):
        self.mem[self.memPos] -= 1
        if self.mem[self.memPos] <= -1:
            self.mem[self.memPos] = 255

    # Add 1 to the value at the current memory position
    def add(self):
        self.mem[self.memPos] += 1
        if self.mem[self.memPos] > 255:
            self.mem[self.memPos] = 0

    # Print the ASCII character corresponding to the value at the current memory position
    def print_char(self):
        print(chr(self.mem[self.memPos]), end="")

    # Read a single character of input and store its ASCII value at the current memory position
    def read_input(self):
        inp = input("Input requested: ")
        self.mem[self.memPos] = ord(inp[0])

    # If the value at the current memory position is 0, skip to the matching ']' character
    def loop_start(self, prg):
        if self.mem[self.memPos] == 0:
            self.countOpened = 0
            self.prgPos += 1
            while self.prgPos < len(self.prg):
                if self.prg[self.prgPos] == "]" and self.countOpened == 0:
                    break
                elif self.prg[self.prgPos] == "[":
                    self.countOpened += 1
                elif self.prg[self.prgPos] == "]":
                    self.countOpened -= 1
                self.prgPos += 1
    # If the value at the current memory position is not 0, skip back to the matching '[' character

    def loop_stop(self, prg):
        if self.mem[self.memPos] != 0:
            countClosed = 0
            self.prgPos -= 1
            while self.prgPos >= 0:
                if prg[self.prgPos] == "[" and countClosed == 0:
                    break
                elif prg[self.prgPos] == "]":
                    countClosed += 1
                elif prg[self.prgPos] == "[":
                    countClosed -= 1
                self.prgPos -= 1

    # Interpret the Brainfuck program
    def interpret(self, prg):
        self.prg = prg
        while self.prgPos < len(prg):
            if self.prg[self.prgPos] == ">":
                self.increment()
            elif self.prg[self.prgPos] == "<":
                self.decrement()
            elif self.prg[self.prgPos] == "+":
                self.add()
            elif self.prg[self.prgPos] == "-":
                self.subtract()
            elif self.prg[self.prgPos] == ".":
                self.print_char()
            elif self.prg[self.prgPos] == ",":
                self.read_input()
            elif self.prg[self.prgPos] == "[":
                self.loop_start(self.prg)
            elif self.prg[self.prgPos] == "]":
                self.loop_stop(self.prg)
            self.prgPos += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Brainfuck interpreter')
    parser.add_argument('-f', '--filename', type=str,
                        help='Brainfuck file to interpret')
    parser.add_argument('-i', '--interactive',
                        action='store_true', help='Interactive mode')
    args = parser.parse_args()

    # If interactive mode is enabled, read the program from user input
    if args.interactive and not args.filename:
        program = Program()
        program.print_banner()
        print("Interactive mode enabled")
        prg = input("Enter Brainfuck code: ")
        program.interpret(prg)
    # If a filename is specified, read the program from the file
    else:
        if not args.filename:
            print("Error: No file specified")
            sys.exit(0)
        else:
            myProgram = Program()
            myProgram.print_banner()
            print('')
            prg = myProgram.read_file()
            myProgram.interpret(prg)
