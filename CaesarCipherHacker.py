# importing modules
import pyperclip
import pyinputplus as pyip

# every possible symbol that can be encrypted
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('This program decrypt text encrypted in Caesar cipher.')

# the string to be encrypted/decrypted
message = pyip.inputStr('input your encrypted text: ')

# the encryption/decryption key
# key = pyip.inputInt('input your key: ', min=0, max=len(letters) - 1)

# tells the program to encrypt or decrypt
# mode = pyip.inputChoice(['encrypt', 'decrypt'], 'choose program mode: ') # set to 'encrypt' or 'decrypt'
mode = 'decrypt'



# capitalize the string in message
message = message.upper()

for key in range(len(letters)):
    # stores possible symbol that can be encrypted
    translated = ''
    # run the encryption/decryption code on each symbol in the message string
    for symbol in message:
        if symbol in letters:
            # get the encrypted (or decrypted) number for this symbol
            num = letters.find(symbol) # get the number of the symbol
            if mode == 'encrypt':
                num = num + key
            elif mode == 'decrypt':
                num = num - key

            # handle the wrap-around if num is larger than the length of letters or less than 0
            if num >= len(letters):
                num = num - len(letters)
            elif num < 0:
                num = num + len(letters)

            # add encrypted/decrypted number's symbol at the end of translated
            translated = translated + letters[num]
        else:
            # just add the symbol without encrypting/decrypting
            translated = translated + symbol

    # print the encrypted/decrypted string to the screen
    print(translated)

# copy the encrypted/decrypted string to the clipboard
pyperclip.copy(translated)
