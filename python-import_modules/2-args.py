#!/usr/bin/python3
import sys

if __name__ == "__main__":
    i = "Hello Welcome To The Best School"
    words = i.split()

    count = len(words)
    if count == 0:
        print("0 argument.")
    elif count == 1:
        print("1 argument:")
    else:
        print(f"{count} arguments:")

    for index, word in enumerate(words, start=1):
        print(f"{index}: {word}")
