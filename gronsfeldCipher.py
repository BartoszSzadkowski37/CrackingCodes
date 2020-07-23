# every possible letters
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# program mode = decrypt / encrypt
programMode = ''

# user message
message = ''

# encrypting / decrypting key
key = ''

# translated message
translated = ''

# getting program mode from the user
programMode = input()

# getting the key from the user
key = input()

# getting user message
message = input()


# first number from the key
indexOfKey = 0
actualKey = int(key[indexOfKey])

# looping each letter in the message
for letter in message:

    # finding index of the current letter
    index = letters.find(letter)

    # depending of program mode we add or subtract the key
    if programMode == 'SZYFRUJ':
        # adding to the letter index actual key number
        index += actualKey

    elif programMode == 'DESZYFRUJ':
        # subtracting from the letter index actual key number
        index -= actualKey

    # if index 'wrap out'
    if index >= len(letters):
        index -= len(letters)
    elif index < 0:
        index += len(letters)

    # adding encrypted / decrypted letter to the result text
    translated += letters[index]

    # updating index of the key if key is shorter than message go to the begin
    indexOfKey += 1
    if indexOfKey > (len(key) - 1):
        indexOfKey = 0

    # changing actual key
    actualKey = int(key[indexOfKey])


# print the result
print(translated)







