xmen_file = open('xmen_base.txt', 'r')
xmen_file.read()
xmen_file.seek(0)

for line in xmen_file:
    print(line, end="")

xmen_file.close()

with open('xmen_base.txt', 'a') as f:
    f.write('Professor Xavier\n')

xmen_file = open('xmen_base.txt', 'r')
for line in xmen_file:
    print(line, end="")
