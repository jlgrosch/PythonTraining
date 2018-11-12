import pyperclip

def main():
    myMessage = 'Common sense is not so common.'
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)

    # Print the encrypted string in ciphertext to the screen, with
    # a | after it in case there are spaces at the end of the message
    print(ciphertext + '|')

    # Copy the encrypted string in ciphertext to the clipboard
    pyperclip.copy(ciphertext)

def encryptMessage(key, message):
    # Each string in cipertext represents a column in the grid
    cipertext = [''] * key

    # Loop through each column in cipertext
    for column in range(key):
        currentIndex = column

        # Keep looping until the currentIndex goes past the message length
        while currentIndex < len(message):
            # Place the character at currentIndex in message at the
            # end of the current column in the ciphertext list
            cipertext[column] += message[currentIndex]

            # Move currentIndex over
            currentIndex += key
    
    # Convert the ciphertext list into a single string value and return it
    return ''.join(cipertext)

# If transpositionEncrypt.py is run instead of imported as a module call main function
if __name__ == '__main__':
    main()