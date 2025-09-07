#Count total words in all arguments
import argparse
parser = argparse.ArgumentParser(description="Count total words in all arguments")
parser.add_argument("args", nargs="+", type=str, help="List of words")
args = parser.parse_args()
total_words = sum(len(arg.split()) for arg in args.args)
print(f"Total words in all arguments: {total_words}")

# to run this ---> python exe6.py "Hello world" "Python programming"