temperature = 29
if temperature == 30:
    print('its a hot day')
else:
    print('its not a hot day')


price = 1000000
good_credit = False
if good_credit:
    down_payment = price * 0.10
else:
    down_payment = price * 0.20
print(f'your down payment is ${down_payment}')


name = 'ali'
if len(name) < 3:
    print('name must be at least 3 characters.')
elif len(name) > 50:
    print('name can be a maximum of 50 characters.')
else:
    print('name looks good!')





