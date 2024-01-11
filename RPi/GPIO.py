#!/usr/bin/env python3
BOARD = 1
OUT = 1
IN = 0
HIGH = 1
LOW = 0
STATE = {}

def setmode(a):
    print(a)


def setup(a, b, initial='foo'):
    STATE[b] = initial
    pass


def output(a, b):
    STATE[a] = b
    pass


def cleanup():
    STATE = {}
    pass


def setwarnings(flag):
    pass

def main():
    global STATE
