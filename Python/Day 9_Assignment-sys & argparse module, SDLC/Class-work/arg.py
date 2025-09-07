import argparse

parser=argparse.ArgumentParser(description="Greet the user")
parser.add_argument("name", help="nae of the user")
args=parser.parse_args()
print(f"Hello,{args.name}!")
