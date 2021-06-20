'''3. Check whether the user input number is even or odd and display it to user.'''

num = int(input('Enter your number:'))
split = num%2
if split==0:
    print(f'It is an even number.')
else:
    print(f'It is an odd number.')