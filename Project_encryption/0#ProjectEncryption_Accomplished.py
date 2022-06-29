def Rotating_single_dict_using_single_int(x, dc):                       #This function rotates single dict over single digit
        dc_rotated = {}
        KEYS, VALUES = zip(*dc.items())
        for cnt in range(len(dc)):
                dc_rotated[KEYS[cnt]] = VALUES[(cnt - x)%len(dc)]
        return dc_rotated    
'''Creating a function which'll encrypt the the packagel using the 6-digit'''
def Encrypting_package(PIN, ROTOR_LST):       
        packageE = []
        for x in range(6):
                pn = PIN[x]
                packageE.append(Rotating_single_dict_using_single_int(pn, ROTOR_LST[x]))
        return packageE
'''Now, Creating PIN_encyption rotor list. from now we'll call it as packageE (means: package_encrypted)
Creating Passing() and Unpassing() function: These functions will be used for getting character output out of our package'''
def Passing(PEL, ch):                                    #PEL: Pin Encrypted List, ch: is a single character
        for x in range(6):
                ch = PEL[x][ch]
        return ch
def GKFVOD(dc, val):                                    #Get Key From Values in Dict
        return list(dc.keys())[list(dc.values()).index(val)] 
def Unpassing(PEL, ch):
        for x in range(1, 7):
                ch = GKFVOD(PEL[-x], ch)
        return ch
#Now, Creating Update function which plays important role as
'''
tatoo -->> flfvv in order to avoid this we'll update the PEL or packageE to be updated/rotated after every use
(we'll rotate by 1 for encryption)
'''
def Updating(PEL, e_or_d=1): #e_or_d: Encrypt or decrypt. This function by default will be used for encryption unless e_or_d value won't be given
        if e_or_d == 1:
                PIN = [1 for _ in range(6)]
                return Encrypting_package(PIN, PEL)
        else:
                PIN = [-1 for _ in range(6)]
                return Encrypting_package(PIN, PEL)
def ProcessE(PEL, password):
        passwordE = ''
        for str_ in password:
                passwordE += Passing(PEL, str_)
                PEL = Updating(PEL)
        return passwordE
def ProcessD(PEL, passwordE):
        password = ''
        for str_ in passwordE:
                password += Unpassing(PEL, str_)
                PEL = Updating(PEL)
        return password              
Rotor_lst = [{'!': 'o', '"': 'l', '#': 'E', '$': 'k', '%': '"', '&': '2', "'": '1', '(': '.', ')': 'S', '*': 'q', '+': '{', ',': '%', '-': 'U', '.': 'Q', '/': 't', '0': '3', '1': '4', '2': 'K', '3': 'P', '4': '|', '5': '(', '6': 'w', '7': '#', '8': 'r', '9': '=', ':': 'p', ';': 'C', '<': '[', '=': '^', '>': '`', '?': '0', '@': 'g', 'A': '_', 'B': 'b', 'C': 'V', 'D': 'm', 'E': '\\', 'F': 'd', 'G': '7', 'H': '&', 'I': '8', 'J': 'j', 'K': 'J', 'L': '6', 'M': '>', 'N': ']', 'O': 'X', 'P': ';', 'Q': '?', 'R': 'B', 'S': 'L', 'T': '5', 'U': 'R', 'V': 'G', 'W': 'y', 'X': 'v', 'Y': 'F', 'Z': '9', '[': 'N', '\\': '+', ']': 'z', '^': '!', '_': 's', '`': 'D', 'a': ',', 'b': 'Z', 'c': 'A', 'd': 'Y', 'e': 'n', 'f': '*', 'g': 'H', 'h': 'W', 'i': 'u', 'j': '@', 'k': 'x', 'l': 'h', 'm': 'i', 'n': 'T', 'o': 'c', 'p': '}', 'q': ':', 'r': '$', 's': ')', 't': 'I', 'u': '/', 'v': 'f', 'w': '<', 'x': "'", 'y': 'M', 'z': 'O', '{': '-', '|': 'e', '}': 'a'}, {'!': '@', '"': 'T', '#': '1', '$': 'C', '%': '6', '&': 'a', "'": 'c', '(': '-', ')': 'M', '*': 'H', '+': '[', ',': 'r', '-': 'R', '.': '=', '/': 'v', '0': 'y', '1': '"', '2': 'D', '3': 'k', '4': '>', '5': 'f', '6': '.', '7': 'G', '8': '{', '9': '3', ':': '$', ';': 'm', '<': '\\', '=': "'", '>': '`', '?': 'S', '@': 'L', 'A': '}', 'B': 'K', 'C': '&', 'D': '8', 'E': '2', 'F': '0', 'G': 'j', 'H': 'J', 'I': 'W', 'J': ')', 'K': 'E', 'L': 'e', 'M': '5', 'N': 'Y', 'O': 'Q', 'P': '(', 'Q': ',', 'R': '^', 'S': ']', 'T': 'V', 'U': 'A', 'V': '*', 'W': 'u', 'X': 'B', 'Y': 'n', 'Z': 'x', '[': '_', '\\': 'N', ']': 'X', '^': 'h', '_': 't', '`': '#', 'a': '/', 'b': 'q', 'c': '9', 'd': 'w', 'e': 'i', 'f': '7', 'g': 'I', 'h': 'o', 'i': '!', 'j': 'd', 'k': 'g', 'l': '?', 'm': 'Z', 'n': '%', 'o': '|', 'p': '+', 'q': 'U', 'r': 'l', 's': 'p', 't': 'F', 'u': 'O', 'v': '4', 'w': 's', 'x': ';', 'y': 'b', 'z': '<', '{': 'P', '|': 'z', '}': ':'}, {'!': 'D', '"': ':', '#': '!', '$': 'Z', '%': 'X', '&': '9', "'": ';', '(': '5', ')': 'p', '*': 'Q', '+': 'N', ',': '%', '-': '.', '.': 'P', '/': 'M', '0': '}', '1': 'i', '2': 'C', '3': '4', '4': 'm', '5': 'k', '6': 'o', '7': '{', '8': '3', '9': '?', ':': '\\', ';': 'a', '<': 'Y', '=': '@', '>': '#', '?': 'c', '@': 'y', 'A': ']', 'B': 'U', 'C': '>', 'D': 't', 'E': '^', 'F': '*', 'G': '&', 'H': 'K', 'I': 'J', 'J': '_', 'K': 'e', 'L': 's', 'M': '1', 'N': ')', 'O': 'l', 'P': 'd', 'Q': 'I', 'R': '$', 'S': 'A', 'T': 'B', 'U': 'f', 'V': 'h', 'W': 'V', 'X': '<', 'Y': 'S', 'Z': 'v', '[': '"', '\\': '6', ']': 'u', '^': '/', '_': 'r', '`': '(', 'a': 'O', 'b': 'n', 'c': 'g', 'd': 'j', 'e': 'E', 'f': 'F', 'g': 'H', 'h': ',', 'i': 'W', 'j': 'b', 'k': '=', 'l': '2', 'm': 'x', 'n': 'w', 'o': "'", 'p': 'q', 'q': 'G', 'r': '`', 's': 'z', 't': '0', 'u': '+', 'v': '-', 'w': '|', 'x': 'R', 'y': '[', 'z': 'T', '{': '7', '|': 'L', '}': '8'}, {'!': 'S', '"': 'Q', '#': 'Y', '$': 'u', '%': '!', '&': 'q', "'": '{', '(': '-', ')': '*', '*': '$', '+': 'V', ',': 'p', '-': 'h', '.': 'G', '/': 'F', '0': '3', '1': 'L', '2': '_', '3': 'T', '4': ')', '5': '/', '6': 'C', '7': '#', '8': 's', '9': 'A', ':': 'c', ';': '4', '<': 'b', '=': 'z', '>': '6', '?': 'E', '@': 'N', 'A': '^', 'B': ',', 'C': 'K', 'D': 'x', 'E': 'a', 'F': 'r', 'G': 'f', 'H': '.', 'I': 'P', 'J': 'l', 'K': '?', 'L': 'o', 'M': 'W', 'N': '"', 'O': 'g', 'P': ']', 'Q': '1', 'R': '5', 'S': 'I', 'T': '9', 'U': 'j', 'V': "'", 'W': '|', 'X': '+', 'Y': 'w', 'Z': 'k', '[': 'e', '\\': 'J', ']': '8', '^': '>', '_': 'n', '`': 'v', 'a': '`', 'b': '2', 'c': 'Z', 'd': '@', 'e': 'y', 'f': '7', 'g': '(', 'h': 'X', 'i': ';', 'j': 'H', 'k': 'U', 'l': 't', 'm': 'i', 'n': '\\', 'o': 'D', 'p': '=', 'q': 'R', 'r': 'M', 's': '%', 't': 'B', 'u': '&', 'v': '}', 'w': '[', 'x': ':', 'y': 'O', 'z': '<', '{': '0', '|': 'm', '}': 'd'}, {'!': 'e', '"': '^', '#': '|', '$': '_', '%': ';', '&': 'b', "'": '*', '(': 'I', ')': '(', '*': 'X', '+': 'g', ',': 'v', '-': '"', '.': '3', '/': '{', '0': 'S', '1': '4', '2': '=', '3': 'O', '4': 'Q', '5': 'H', '6': '5', '7': 'o', '8': 'B', '9': '2', ':': 'Z', ';': 'y', '<': ':', '=': '%', '>': 'm', '?': 'T', '@': '@', 'A': '1', 'B': '>', 'C': '\\', 'D': '#', 'E': '$', 'F': "'", 'G': 'R', 'H': 'A', 'I': 'd', 'J': '8', 'K': 's', 'L': 'D', 'M': 'f', 'N': 'w', 'O': 'r', 'P': '&', 'Q': ')', 'R': 'G', 'S': 'P', 'T': 'i', 'U': '!', 'V': 'M', 'W': '}', 'X': 'k', 'Y': ',', 'Z': 'K', '[': '/', '\\': '`', ']': '<', '^': 'x', '_': 'N', '`': '9', 'a': 'p', 'b': 'u', 'c': 'F', 'd': 'c', 'e': 'h', 'f': '0', 'g': 'E', 'h': 'L', 'i': 'a', 'j': 'j', 'k': 'q', 'l': '?', 'm': 't', 'n': '-', 'o': 'C', 'p': 'U', 'q': '7', 'r': '[', 's': 'J', 't': 'l', 'u': 'Y', 'v': 'z', 'w': '+', 'x': ']', 'y': '.', 'z': 'W', '{': 'V', '|': 'n', '}': '6'}, {'!': ']', '"': ':', '#': 'I', '$': 'A', '%': '"', '&': '2', "'": 't', '(': '7', ')': "'", '*': '[', '+': 'e', ',': 'h', '-': '/', '.': ';', '/': 'R', '0': 'p', '1': 'P', '2': '!', '3': 'n', '4': '_', '5': 'u', '6': '<', '7': '%', '8': 'F', '9': '4', ':': 'z', ';': 'C', '<': 'a', '=': '(', '>': 'w', '?': 'g', '@': 'Y', 'A': '6', 'B': 'H', 'C': 'G', 'D': 'i', 'E': '`', 'F': 'S', 'G': ')', 'H': 'W', 'I': 'q', 'J': 'Z', 'K': '$', 'L': 'y', 'M': '#', 'N': '0', 'O': '+', 'P': '1', 'Q': 'D', 'R': '}', 'S': 'j', 'T': '&', 'U': '{', 'V': 'f', 'W': 'X', 'X': '9', 'Y': 'r', 'Z': 'Q', '[': 's', '\\': 'l', ']': 'c', '^': 'M', '_': '^', '`': 'K', 'a': '5', 'b': 'N', 'c': '8', 'd': 'b', 'e': '|', 'f': 'k', 'g': 'x', 'h': 'T', 'i': 'd', 'j': '>', 'k': '3', 'l': 'B', 'm': '=', 'n': ',', 'o': '?', 'p': 'U', 'q': 'm', 'r': '*', 's': 'O', 't': '.', 'u': 'o', 'v': 'V', 'w': 'L', 'x': 'J', 'y': '@', 'z': 'v', '{': 'E', '|': '-', '}': '\\'}] #Our Encryption                                    *****Important*****
'''The above rotor list is to be well backed-up and should never be disturbed as it has contains the shuffled rotors'''
#Now, We'll ask for the 6-digit PIN
pin = input('Enter your 6-digit PIN to encrypt/decrypt the password: ')
if len(pin) == 6 and pin.isnumeric():
        PIN = [int(i) for i in pin]
        PEL = Encrypting_package(PIN, Rotor_lst)
        eVSd = input('Please enter "E" to encrypt or "D" to decrypt: ')
        if eVSd.lower() == 'e':
                password = input('Enter the password to be encrypted: ')
                passwordE = ProcessE(PEL, password)
                print('Your encrypted password is: ', passwordE)
        elif eVSd.lower() == 'd':
                passwordE = input('Enter your encrypted passowrd: ')
                password = ProcessD(PEL, passwordE)
                print('Your decrypted password: ', password)
        else:
                print('Get lost!! I aksed to enter only "E" or "D"')
                print('Thank you for using me!')
else:
        if pin.isnumeric() == False:
                print('The above is not PIN, Please only enter numbers')
        else:
                if len(pin) == 1:
                        print(f'The above PIN is of 1-digit only')
                elif len(pin) < 6:
                        print(f'The above PIN is of only {len(pin)}-digits')
                else:
                        print(f'The above PIN is of {len(pin)}-digits')
        print('Program ended!')
