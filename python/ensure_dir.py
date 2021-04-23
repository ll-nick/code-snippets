from pathlib import Path
import os

"""
Script to check if a directory exists that creates it in case it doesn't.
"""

def ensure_dir(d):
    if not os.path.isdir(d):
        Path(d).mkdir(parents=True)  

def example():
    # Example path
    path = "/tmp/test/test2"

    ensure_dir(path)

if __name__=="__main__":
    example()