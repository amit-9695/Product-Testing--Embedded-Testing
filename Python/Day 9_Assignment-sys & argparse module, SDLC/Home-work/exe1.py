# using type and default value

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("a", type=int, help="First number")
parser.add_argument("b", type=int, help="Second number")
parser.add_argument("--operation", choices=["add", "subtract"], default="add")

args = parser.parse_args()

if args.operation == "add":
    print(args.a + args.b)
else:
    print(args.a - args.b)
    

# to run this ---> python exe1.py 10 20 --operation add
