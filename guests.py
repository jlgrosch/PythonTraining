guests = ['albert einstein', 'bill nye', 'norm evern']
for guest in guests:
    print("Your are invited to our party " + guest.title())
print(guests[1].title())
guests.remove('bill nye')
for guest in guests:
    print("Your are invited to our party " + guest.title())
guests.insert(0, 'reba macintire')
guests.append('johnny cash')
guests.insert(2, 'chris hannah')
print('\n')
for guest in guests:
    print("Your are invited to our party " + guest.title())
guests_remove = guests.pop()
print('I am sorry but we cannot invite you ' + guests_remove.title())
guests_remove = guests.pop()
print('I am sorry but we cannot invite you ' + guests_remove.title())
guests_remove = guests.pop()
print('I am sorry but we cannot invite you ' + guests_remove.title())
print('\n')
for guest in guests:
    print("Your are invited to our party " + guest.title())
print('Number of guests ' + str(len(guests)))
guests.remove('reba macintire')
guests.remove('albert einstein')
print(guests)
