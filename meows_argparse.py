import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n): 
    print("meow")


## you can run now like this to show help 
## py meow_argparse.py -h (or --help)

## to run it
## py meow_argparse.py -n 4