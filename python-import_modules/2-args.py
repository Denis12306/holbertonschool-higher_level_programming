#!/usr/bin/python3
import sys

if __name__ == "__main__":
    i = "Hello Welcome To The Best School"
    words = i.split()
    print(f"{6} arguments:")

    for index, word in enumerate(words, start=1):
        print(f"{index}: {word}")
