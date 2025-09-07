import argparse

parser=argparse.ArgumentParser(description="Greet the user")
parser.add_argument("name",help="user's name")
parser.add_argument("--age",type=int, help="user's age (optional)")
parser.add_argument("--shout",action="store_true",help="shout the greeting")

args=parser.parse_args()

greeting=f"Hello {args.name}!"

if args.age:
    greeting+=f" you are {args.age} years old."

if args.shout:
    greeting=greeting.upper()

print(greeting)

# to run this ---> python exe2.py Amit --age 21 --shout
