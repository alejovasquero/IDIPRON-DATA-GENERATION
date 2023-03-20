import argparse

from src.bundle.generate import generate_data

# create argument parser object
parser = argparse.ArgumentParser(description='Description of your script')

# add arguments
parser.add_argument('-r', '--rows', type=int, help='Rows count', required=True)
parser.add_argument('-f', '--file', type=str, help='Path to output file', required=False)

# parse arguments
args = parser.parse_args()

if __name__ == '__main__':
    print(list(generate_data(args.rows, args.file)))
