import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="Enable verbose mode", action="store_true")
args = parser.parse_args()

if args.verbose:
    print("Verbose mode is on.")
else:
    print("Verbose mode is off.")
