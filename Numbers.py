# There 3 types of nummbers in Python (version3)
# int, float, complex

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

import pynput
from pynput.keyboard import Key,Controller
keyboard = Controller()

import time

import random

# import subprocess module
import subprocess as sp

# integer
a = 1977
type(a)  # you can see the data type by using the type function
print()
print(a)
print(type(a))
print()

a  # To see the value of a, just type it and press enter
print(a)
print()


# Floats
# Floats are how decimal values are stored
b = 23.2323
type(b)  # To confirm that it's a float, look at its type
print(b)
print(type(b))
print()
 
# Complex Numbers
# A complex number has a real part and an imaginary part
# To create a complex, type in the real part and then the imaginary part followed by the letter j
c = 21- 4.5j
type(c)  # again confirm its a complex number by checking its type
print(c)
print(type(c))
print()
# you can also display its real and imaginary parts separately
# To access the real part you access the "real" property
c.real
print(c.real)
print()
# You can access the imaginary part through the property named "imag"
c.imag
print(c.imag)
print()

print()
# name program to open
programname = "Notepad.exe"

# now open 
sp.Popen(programname)

time.sleep(1)
sentence = "This is a short tutorial on Numbers in Python\n\nKey Takeaways:\nThere 3 types of numbers in Python: int, float, complex\nIntegers are like whole numbers, but they also include negative numbers\nFloats are how decimal values are stored\nA complex number has a real part and an imaginary part\n\n-[S3]RGE"

for c in sentence:
    keyboard.press(c)
    keyboard.release(c)
    delay = random.uniform(0,0.2)
    time.sleep(0.1)
