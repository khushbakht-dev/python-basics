entry = ''
start = False
while True:
    entry = input('< ' ).lower()
    if entry == 'start':
        if start:
            print('car is already started')
        else:
            start = True
            print('car started')
    elif entry == 'stop':
        if not start:
            print('car is already stopped')
        else:
            start = False
            print('car is stopped')
    elif entry == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to quit''')
    elif entry == 'quit':
        break
    else:
        print("soryy, i don't understand that")











