# Finding arithmetic mean

import argparse

parser = argparse.ArgumentParser(description="Calculate the arithmetic mean")
parser.add_argument("numbers", nargs="+", type=float, help="List of numbers")
args = parser.parse_args()

mean = sum(args.numbers) / len(args.numbers)
print(f"The arithmetic mean is: {mean}")

# to run this ---> python exe4.py 10 20 30 40 50