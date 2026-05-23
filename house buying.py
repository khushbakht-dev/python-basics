print('''heyy!
         good afternoon, hope you are doing well.''')
buy = input('do you want to buy a house?' )
if buy == str('yes'):
    print("""the price of the house is $1m.
    answer a few questions below to know if you're eligible to buy.""")
else:
    print('no worries, come back next time!')
    breakpoint()
good_credit = input('do you have good credit?' )
criminal_record = input('do you have a criminal record?' )
if good_credit == str('yes') and not criminal_record == str('yes'):
    print('you are eligible to buy!')
else:
    print('you are not eligible to buy!')
    breakpoint()
price_of_house = 1000000
if good_credit == str('yes'):
    down_payment = price_of_house * 0.10
    print(f'the down payment of the house is ${down_payment}')
else:
    down_payment = price_of_house * 0.20
    print(f'the down payment of the house is ${down_payment}')
print('thankyou for contacting us!')