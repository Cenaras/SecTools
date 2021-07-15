import sys
import base64

### Allow to specify own ROTx?
# Encrypt/Decrypt ROTx
# --all; runs all default "-types" on the string/file

def errormessage(msg):
    print(msg)
    sys.exit()

def rot13(msg):
    new_msg_number = []
    new_msg = []
    for c in msg:
        new_msg_number.append(ord(c) + 13)
    
    for i in new_msg_number:
        if i > 122:  #only use lower case letters
            i = i-26
        if i == 45: 
            new_msg.append(' ')
        else: 
            new_msg.append(chr(i))

    print(''.join(new_msg))


def base64enc(msg):
    byte_msg = msg.encode('ascii')
    base64_byte = base64.b64encode(byte_msg)
    print(base64_byte.decode('ascii'))

def base64dec(msg):
    base64_msg_byte = msg.encode('ascii')
    msg_byte = base64.b64decode(base64_msg_byte)
    print(msg_byte.decode('ascii'))

def all(msg):
    print("Do everything...")

dec_types = ['-rot13', '-base64enc', '-base64dec', '-a']

if '--help' in sys.argv or '-h' in sys.argv: 
    errormessage("Usage: python common_decrypt.py [-s/-i] (string/inputfile), <decrypt type> \nPlease use "" to specify strings with spaces\nUse -types to display possible decrypt types")
elif '-types' in sys.argv: 
    
    print("Allowed types are: " + ', '.join(dec_types))
    sys.exit()

if len(sys.argv) < 4: 
    print("Not enough arguments, use -h or --help to see usage")
    sys.exit()

elif sys.argv[1] == "-s" or sys.argv[1] == "-i":
    if sys.argv[1] == '-s': 
        string = sys.argv[2]
    
    elif sys.argv[1] == '-i': #Check if file exists first...
        f = open(sys.argv[2], 'r')
        string = f.read()

else: errormessage("Invalid input, use -s or -i for string or file")

command = sys.argv[3][1:] #Remove '-' to use eval for function call

if sys.argv[3] not in dec_types:
    print()
    errormessage("Specified conversion type is not valid. Use '-types' to see available decryption types")

#Call the correct function - i.e. the 3rd argument
eval(command + '( "' + string + '")') #Call the corresponding function with the argument "string"






