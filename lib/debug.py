#!/usr/bin/env python3

from config import CONN, CURSOR
from song import Song

def main():
    Song.create_table()

    blinding_lights = Song("Blinding Lights", "After Hours")
    blinding_lights.save()

    hello = Song("Hello", "25")
    hello.save()

    print("Songs saved successfully!")

if __name__ == '__main__':
    main()

