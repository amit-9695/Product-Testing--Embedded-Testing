# Sort the numeric arguments ascending
import argparse
parser = argparse.ArgumentParser(description="Sort the numeric arguments in ascending order")
parser.add_argument("args", nargs="+", type=float, help="List of numbers")
args = parser.parse_args()
print(f"Sorted arguments: {sorted(args.args)}")


# to run this ---> python exe8.py 50 20 30 10 40