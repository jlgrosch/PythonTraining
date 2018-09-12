def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, 'rb') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about "+ str(num_words) + " words.")

filename = "c:\\Users\\James\\OneDrive\\Python\\alice.txt"
count_words(filename)

filenames = ["c:\\Users\\James\\OneDrive\\Python\\alice.txt", "c:\\Users\\James\\OneDrive\\Python\\siddhartha.txt", "c:\\Users\\James\\OneDrive\\Python\\moby_dick.txt", "c:\\Users\\James\\OneDrive\\Python\\little_women.txt"]
for filename in filenames:
    count_words(filename)
