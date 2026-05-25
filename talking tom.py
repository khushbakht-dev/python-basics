print("""heyy!
 i'm talking tom, what you you like me to do?""")
entry = ''
sleeping = False
bath = False
eat = False
while True:
    entry = input(' ').lower()
    if entry == 'sleep':
        if sleeping:
            print('tom is already sleeping')
        else:
            sleeping = True
            print('tom is sleeping now')
    elif entry == 'help':
        print('''
sleep - goes to sleep
wake up - wakes up
eat - eats meal
bath - takes a bath
quit game - to quit playing''')
    elif entry == 'eat':
        if eat:
            print('tom is already eating')
        else:
            eat = True
            print('tome is eating now')
    elif entry == 'wake up':
        if not sleeping:
            print('tom is already awake')
        else:
            sleeping = False
            print('tom is awake now')
    elif entry == 'bath':
        if bath:
            print('tom is already bathing')
        else:
            bath = True
            print('tom is bathing now')
    elif entry == 'quit game':
        break
    else:
        print("i don't know what do you want me to do")

