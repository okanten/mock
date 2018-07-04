import sys

def main(args):
    input = list(args.lower())
    result = ""
    for i, letter in enumerate(input):
        if i % 2 == 0:
            result = result + letter.upper()
        else:
            result = result + letter
    print (result)

main(sys.argv[1])
