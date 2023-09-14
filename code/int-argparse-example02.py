# https://docs.python.org/es/3/howto/argparse.html
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("freq", nargs='?', help="freq (int) of interim commits eg every 10 or 100 or 1000 rows", type=int, default=10000000)
args = parser.parse_args()
print(args.freq)
for i in range(0,100):
    if (i%args.freq==0):
        print(i)