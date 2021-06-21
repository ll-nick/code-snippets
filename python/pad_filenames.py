import glob
import os
from pathlib import Path
import argparse

"""
A simple script to make sure all file names in a folder have a specified length.
This is useful for properly sorting files that would otherwise be sorted 0.txt - 1.txt - 10.txt etc.
"""

def main(dir, length):
    filenames = glob.glob("{}/*.png".format(dir)) 
    for f in filenames:
        path = Path(f)
        name = path.stem
        if len(name) < length:
            while len(name) < length:
                name = "0" + name
            os.rename(f, ps.path.join(str(path.parent, name + path.suffix))

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Helper script to pad filenames with leading zeros. Files should have only numbers as filenames.")
    parser.add_argument("-d", "--dir", type=str, required=True, help="Directory where filenames will be adjusted.")
    parser.add_argument("-l", "--length", type=int, default=3, help="How long the filenames should be.")

    args = parser.parse_args()

    main(args.dir, args.length)
