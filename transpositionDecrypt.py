import math, pyperclip

def main():
    myMessage = 'Cenoonommstmme oo snnio. s s c'
    myKey = 8

    plaintext = decryptMessage(myKey, myMessage)

    # Print the encrypted string in ciphertext to the screen, with
    # a | after it in case there are spaces at the end of the message
    print(plaintext + '|')

    pyperclip.copy(plaintext)

def decryptMessage(key, message):
    # The number of columns in transposition grid
    numOfColumns = int(math.ceil(len(message) / float(key)))
    # The number of rows in grid
    numOfRows = key
    # The number of empty boxes in last golumn of the grid
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # Each string in plaintext represents a column in the grid
    plaintext = [''] * numOfColumns

    # The column and row variables point to where in the grid
    # the next character in the encrypted message will go
    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1 # point to the next column

        # If there are no more columns OR we're at a shaded box
        # go back to the first column and the next row
        if (column == numOfColumns) or (column == numOfColumns -1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1

    return ''.join(plaintext)

# If transpositionDecrypt.py is run instead of imported as a module
# call the main() function
if __name__ == '__main__':
    main()