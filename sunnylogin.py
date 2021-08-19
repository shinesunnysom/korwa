while True:
    print('Who are you?')
    name = input()
    if name != 'Sunny':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'wololo':
        break
print('Access granted.') 
