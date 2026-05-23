weight = int(input('your weight: ' ))
unit = input('(L)bs or (k)g: ' )
if unit.upper() == 'L':
    final_weight = 0.4536 * weight
    print(f'you are {final_weight} kilos')
else:
    final_weight=2.20462 * weight
    print(f'you are {final_weight} pounds')
