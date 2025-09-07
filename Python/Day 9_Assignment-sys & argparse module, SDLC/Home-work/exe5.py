# Print the largest argument.
import argparse
parser = argparse.ArgumentParser(description="Print the largest argument")
parser.add_argument("args", nargs="+", type=float, help="List of numbers")
args = parser.parse_args()
print(f"The largest argument is: {max(args.args)}")

# to run this ---> python exe5.py 10 20 30 40 50