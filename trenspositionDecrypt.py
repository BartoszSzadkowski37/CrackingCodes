# importing modules
import math, pyperclip

def main():
    myMessage = 'Cenoonommstmme oo snnio. s s c'
    myKey = 8

    plaintext = decryptMessage(myKey, myMessage)

    # print with a | after it in case
    # there are spaces at the end of the decrypted message.
    print(plaintext + '|')

    pyperclip.copy(plaintext)

def decryptMessage(key, message):
    # the transposition decrypt function will simulate the 'columns' and
    # 'rows' of the grid that the plaintext is written on by using a list
    # of strings. First, we need to calculate a few values.

    # the number of 'columns' in our transposition grid:
    numOfColumns = math.ceil(len(message) / key)
    # the number of 'rows' in our grid will ned:
    numOfRows = key
    # the number of 'shaded boxes' in the last 'column' of the grid:
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # each string in plaintext represents a column in the grid
    plaintext = [''] * numOfColumns

    # the col and row variables point to where in the grid the next
    # character in the encrypted message will go
    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1 # point to next column

        # it there are no more columns OR we're at a shaded box, go back to
        # the first column and the next row
        if (col == numOfColumns) or (col == numOfColumns -1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1
    return ''.join(plaintext)

# if transpositionDecrypt.py is run (instead of imported as a module) call
# the main() function
if __name__ == '__main__':
    main()