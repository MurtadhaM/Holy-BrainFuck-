"""
Author: Murtadha Marzouq
Description: Python BrainFuck Interpreter to experement with Dynamically typed langauges
Version: 2.0 Added Class Support
"""
import sys
import argparse

def print_banner():
    # Print out the banner.txt file to the console
    # Used to display the banner at the start of the script
    with open('./banner.txt', 'r') as f:
        print(f.read())

class Program():
    
    # Initialize the interpreter. If a filename was passed in, read it.
    def __init__(self):
            self.filename =  args.filename
            self.prgPos = 0
            self.mem = [0]
            self.memPos = 0
            if self.filename:
                self.prg = self.read_file()
            self.countOpened =0


    def read_file(self):
        f = open(self.filename, "r")
        prg = f.read()
        f.close()
        return prg

    def increment(self):
        self.memPos += 1
        if len(self.mem) <= self.memPos:
            self.mem.append(0)

    def decrement(self):
        self.memPos -= 1
        if self.memPos < 0:
            print("Error: Moved off tape!")
            sys.exit(0)

    def subtract(self):
        self.mem[self.memPos] -= 1
        if self.mem[self.memPos] <= -1:
            self.mem[self.memPos] = 255

    def add(self):
        self.mem[self.memPos] += 1
        if self.mem[self.memPos] > 255:
            self.mem[self.memPos] = 0

    def print_char(self):
        print(chr(self.mem[self.memPos]), end="")

    def read_input(self):
        inp = input("Input requested: ")
        self.mem[self.memPos] = ord(inp[0])

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

    def interpret(self , prg):
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
    print("")


    
parser = argparse.ArgumentParser(description='Brainfuck interpreter')
parser.add_argument('-f', '--filename', type=str, help='Brainfuck file to interpret')
parser.add_argument('-i', '--interactive', action='store_true', help='Interactive mode')
args = parser.parse_args()
print_banner()
if args.interactive and not args.filename:
    print("Interactive mode enabled")
    prg = input("Enter Brainfuck code: ")
    program = Program()
    program.interpret(prg)
else:
    if not args.filename:
        print("Error: No file specified")
        sys.exit(0)
    else:
        myProgram = Program()
        prg = myProgram.read_file()
        myProgram.interpret(prg)
        

