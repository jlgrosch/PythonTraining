filename = "c:\\Users\\James\\OneDrive\\Python\\pi_digits.txt"
filename2 = "c:\\Users\\James\\OneDrive\\Python\\pi_million_digits.txt"

with open(filename) as file_object:
    """read whole content and print it out"""
    contents = file_object.read()
    print(contents.rstrip())

with open(filename) as file_object:
    """read one line at a time and print out one line at a time"""
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_object:
    """read content to use it outside of with statement"""
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))

with open(filename2) as file_object:
    """read content to use it outside of with statement for million digit file"""
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string[:52] + "...")
print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
