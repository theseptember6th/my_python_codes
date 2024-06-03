# script.py
import argparse

def main():
    parser = argparse.ArgumentParser(description='A simple CLI for demonstration')
    parser.add_argument('number', type=int, help='A number to be doubled')
    
    args = parser.parse_args()
    
    result = args.number * 2
    print(result)

if __name__ == "__main__":
    main()
