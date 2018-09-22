for numbers in range(1,21):
    print(numbers)
numbers = list(range(1,1000001))
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
for numbers in range(1,21,2):
    print(numbers)
for numbers in range(3,31,3):
    print(numbers)
cubes = []
for value in range(1,11):
    cubes = value**3
    print(cubes)
cubes = [value**3 for value in range(1,11)]
print(cubes)
print('The first three items in the list are ' + str(cubes[:3]))
print('The next three items on the list are '+ str(cubes[3:6]))
print('The last three items on the list are '+ str(cubes[-3:]))
