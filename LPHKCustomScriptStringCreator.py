
import pyperclip as pc

while True:
    script = input("Script: ")
    x = input("X: ")
    y = input("Y: ")
    r = input("R: ")
    g = input("G: ")
    b = input("B: ")

    s = "|"

    print()

    pc.copy(script+s+x+s+y+s+r+s+g+s+b)
    print("String has been copied to clipboard! Paste with CTRL+V!")

    print()