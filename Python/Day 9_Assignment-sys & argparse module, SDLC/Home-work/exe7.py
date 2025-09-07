# Reverse the characters of every argument.
import argparse
parser = argparse.ArgumentParser(description="Reverse the characters of every argument")
parser.add_argument("args", nargs="+", type=str, help="List of words")
args = parser.parse_args()
reversed_args = [arg[::-1] for arg in args.args]
print(f"Reversed arguments: {reversed_args}")

# to run this ---> python exe7.py "Hello" "World"