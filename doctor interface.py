print('good afternoon')
name = input('what is your full name?' )
print(' hello ' + name + '!')
complain = input('what is your presenting complain?' )
time = input('how long have you been having this for?' )
associated_symptoms = input( f' what other symptoms do you have{name}?' )
print(f'so {name} you have complain of {complain} for {time} and other symptoms such as {associated_symptoms}')
available_tomorrow = input('are you available for consultation tomorrow?' )
if available_tomorrow == str('yes'):
    print('your appointment is scheduled for tomorrow')
else:
    date = input('which date of the month are you available for the appointment?' )
print('thankyou for contacting us!')
print( f'thankyou for contacting us {name}! your appointment is scheduled for {str(date)} of june. ')
