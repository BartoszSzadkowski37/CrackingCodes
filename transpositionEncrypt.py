# importing modules
import pyperclip

def main():
    myMessage = 'Common sense in not so common.'
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)

    # print the encrypted string in ciphertext to the screen, with
    # a | (called 'pipe' character) after it in case there are spaces at
    # the end of the encrypted message.
    print(ciphertext + '|')

    # copy the encrypted string in ciphertext to the clipboard.
    pyperclip.copy(ciphertext)


def encryptMessage(key, message):
    # each string in ciphertext represents a column in the grid.
    ciphertext = [''] * key

    # loop through each column in ciphertext
    for col in range(key):
        pointer = col

        # keep looping until pointer goes past the length of the message
        while pointer < len(message):
            # place the character at pointer in message at the end of the
            # current column in the ciphertext list
            ciphertext[col] += message[pointer]

            # move pointer over
            pointer += key

        # convert the ciphertext list into a single string value and return it.
    return ''.join(ciphertext)


    # if transpositionEncrypt.py is run (instead of imported as a module) call
    # the main() function.

if __name__ == '__main__':
    main()