# This is a vigenere decoder written by Abdelhamid.

print('Welcome Mr. to the Vigenere decoder written by Abdelhamid.\n'
      'Greetings! \n')
print('If you wanna learn about Vigenere ciphere, visit this URL: https://www.boxentriq.com/code-breaking/vigenere-cipher  \n')
print('''Here is an example: 
vigenere ciphertext = UN6S-GD
key = Abdelhamid
RESULTED PLAINTEXT = UM6P-CS ''')

def viginere_decoder(st, key):
    key_ords = []
    real_key = []
    # create a list of the order of characters in ASCII table
    for ch in key:
        if ch.isupper():
            key_ords.append(ord(ch)-ord('A'))
        elif ch.islower():
            key_ords.append(ord(ch) - ord('a'))
    # duplicate the list of ords to the lenght of the cipher 
    for lenght in range(len(st)):
        real_key.append(key_ords[lenght%len(key_ords)])
    strng = list(st)
    a = 0
    dec = ''
    # decipher the cipher
    increment_cip = 0
    increment_key = 0
    for char in strng:
        if char.isupper():
            dec += chr(ord('A') + (ord(strng[increment_cip]) - real_key[increment_key] - ord('A')) % 26)
            increment_cip+=1
            increment_key+=1
        elif char.islower():
            dec += chr(ord('a') + (ord(strng[increment_cip]) - real_key[increment_key] - ord('a')) % 26)
            increment_cip+=1
            increment_key+=1
        else:
            dec += char
            increment_cip+=1
    return dec


inp = input('Please, enter the vigenere cipher? ')
ky = input('Please, enter the key you wanna use to decode it: ')
print(f'Here is the plaintext : "{viginere_decoder(inp, ky)}"')