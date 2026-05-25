secret_number = 5
guess_count = 0
guess_limit = 5
while guess_count < guess_limit:
    guess = int(input('guess the number: ' ))
    guess_count += 1
    if guess == secret_number:
        print('yayyy! you won<3')
        break
else:
    print('oops,better luck next time!')