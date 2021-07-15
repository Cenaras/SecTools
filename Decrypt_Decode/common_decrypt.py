import sys


def errormessage(msg):
    print(msg)
    sys.exit()


if len(sys.argv) < 4: 
    print("Not enough arguments, use -h or --help to see usage")
    sys.exit()

dec_types = ['-rot13', '-base64']

if '--help' in sys.argv or '-h' in sys.argv: 
    errormessage("Usage: python common_decrypt.py [-s/-i] (string/inputfile), <decrypt type> \nUse -types to display possible decrypt types")
if '-types' in sys.argv: print('-rot13, -base64')

if sys.argv[1] == "-s" or sys.argv[1] == "-i":
    if sys.argv[1] == '-s': 
        string = sys.argv[2]
    elif sys.argv[1] == '-i':
        print("String = readfile of input")
else: errormessage("Invalid input, use -s or -i for string or file")

if sys.argv[3] not in dec_types:
  errormessage("Specified decryption type is not valid. Use '-types' to see available decryption types")


    



