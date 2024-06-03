import argparse
import sys

def calc(args):
    if args.o=="add":
        return args.x+args.y
    elif args.o=="sub":
        return args.x-args.y
    elif args.o=="mul":
        return args.x*args.y
    elif args.o=="div":
        return args.x/args.y
    else:
        return "something went wrong"

if __name__ == '__main__':
    parser=argparse.ArgumentParser('''
WELCOME TO COMMAND LINE INTERFACE
FOR CALCULATOR
write in command line: --x "number1" --y "number2" --o add
write in command line: --x "number1" --y "number2" --o sub
write in command line: --x "number1" --y "number2" --o mul
write in command line: --x "number1" --y "number2" --o div
                                ''')
    parser.add_argument('--x',type=float,default=1.0,
                        help='''Enter 1st number. This is utility for calculation. Please contact Kristal for more infos''')
    parser.add_argument('--y',type=float,default=3.0,
                        help='''Enter 2nd number. This is utility for calculation. Please contact Kristal for more infos''')
    parser.add_argument('--o',type=str,default="add",
                        help='''This is utility for calculation. Please contact Kristal for more infos''')
    
    args=parser.parse_args()
    sys.stdout.write(str(calc(args)))
    