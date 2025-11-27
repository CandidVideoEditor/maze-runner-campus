"""
Converts ASCII map text into a Python list usable by the game.
"""
import sys

def convert(infile, outfile):
    with open(infile, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    py_list = "[" + ",".join([repr(row) for row in lines]) + "]"

    with open(outfile, "w") as f:
        f.write(py_list)

    print("Converted:", infile, "→", outfile)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python convert_map.py input.txt output.py")
        sys.exit(1)

    convert(sys.argv[1], sys.argv[2])
