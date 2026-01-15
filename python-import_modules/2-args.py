#!/usr/bin/python3

if __name__ == "__main__":
    x = "Hello Welcome To The Best School"
    words = x.split()
    count = len(words)

    print(f"{count} argument{'s' if count != 1 else ''}:")

    for i in range(count):
        print(f"{i + 1}: {words[i]}")
