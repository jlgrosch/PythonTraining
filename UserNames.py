username = ['james', 'bob', 'jerry', 'admin', 'tom', 'janie']
if username:
    for usernames in username:
        if usernames == 'admin':
            print('Hello Admin, would you like a status report')
        else:
            print('Hello ' + usernames.title() + ', thank you for logging in again')
else:
    print('We need to find some users')

current_users = ['james', 'bob', 'jerry', 'admin', 'tom', 'janie']
new_users = ['james', 'frank', 'chris', 'janie', 'alex', 'JAMES', 'JaNie']
for new_user in new_users:
    if new_user.lower() in current_users:
        print('Name already in use, please pick a new one ' + new_user.title())
    else:
        print('Name is available ' + new_user.title())
