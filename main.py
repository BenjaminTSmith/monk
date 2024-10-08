#!/usr/bin/python3.12

import tomllib
import sys

def main():
    try:
        file = open("monk.toml", "rb")
    except FileNotFoundError:
        print("error: monk.toml not found in current working directory")
        sys.exit()
    
    try:
        file = tomllib.load(file)
    except tomllib.TOMLDecodeError:
        print("error: invalid monk.toml document")
        sys.exit()

    targets = {}
    
    for target in file["targets"]:
        config = file["targets"][target]
        src = config.get("src")
        if type(src) != list:
            print(f"error: src is a {type(src)} not a list")
            sys.exit()
        if len(src) == 0:
            print("error: no source files provided")
            sys.exit()


if __name__ == "__main__":
    main()
