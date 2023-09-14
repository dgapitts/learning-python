# https://docs.python.org/es/3/howto/argparse.html
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", nargs='?', help="display a square of a given number", type=int, default=0)
#parser.add_argument("square", nargs='?', const=1, type=int, default=1)
#parser.add_argument("square", nargs='?', const=0, type=int, default=0)
#parser.add_argument("square", nargs='?', type=int, default=0)
#parser.add_argument("square", type=int, default=0)  # this FAILs without nargs
args = parser.parse_args()
print(args.square**2)