# Written by Abdelhamid
print('''This is a simple caesar Decoder written by Abdelhamid
If you wanna explore more about caesar cipher, consider visting this URL: https://www.sciencedirect.com/topics/computer-science/caesar-cipher \n
Here is a little example to illustrate the idea of this program:
ciphertext = BCDEF
shift = 1
resulted plaintext = ABCDE ''')          
                                                  
import string
import time
for x in range(2):
        for y in range(50):
                print('-',end ='')
                time.sleep(0.01)
        print('')

def caesar_decoder(st):
    liste = []
    enc = ''
    for y in range(26):
        enc = ''
        for x in st:
            if x in string.ascii_lowercase:
                enc += chr(ord('a')+(ord(x)+y-ord('a')) % 26)
            elif x in string.ascii_uppercase:
                enc += chr(ord('A') + (ord(x) + y - ord('A')) % 26)
            else:
                enc += x
        liste.append(enc)

    return liste


inp = input('what is the cipher? ')
index = input('Enter the index of the ciphertext. If you want all results press Q: ')
if index.lower() == 'q': 
    print('\n'.join(caesar_decoder(inp)))
else:
    print(caesar_decoder(inp)[26-int(index)])

#! Greetings for going through this code :)