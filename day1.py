print('Enter a number to check if it is Even: ')
input_num = int(input())

if input_num % 2 == 0:
    print('Input number', input_num, ' is Even')

# Program to check if a number if Even or not.

print('Enter a number to check if it is Even: ')
input_num = int(input())

if input_num % 2 == 0:
    print('Input number', input_num, ' is Even')
else:
    print('Input number', input_num, ' is not Even')

# Program to check if a number if Even or Odd.

print('Enter a number to check if it is Even: ')
input_num = int(input())

if input_num % 2 == 0:
    print('Input number', input_num, ' is Even')
else:
    print('Input number', input_num, ' is Odd')

'''
Accept average score from the user and print the result as follows.
0  - 50 Fail
51 - 75 SC
76 - 90 FC
91 - 100 Distinction
Also check for Invalid score
'''

average_score = int(input('Enter your average score to print your result: '))

if average_score >= 0 and average_score <= 50:
    print('Fail')
elif  average_score <= 75:
    print('Second Class')
elif average_score <= 90:
    print('First Class')
elif average_score <= 100:
    print('Distinction')
else:
    print('Invalid Input')

# x++ != y && --y > z || y++ <= x

i = -1
i -= -1 # i = i - (-1) = -1 + 1 = 0
print(i)


import random

player_number = int(input('Enter a number of your choice between 0 to 9: '))

system_number = random.randint(9, 10)
print(system_number)

if player_number == system_number:
    print('You are crorepati')
else:
    print('You are Roadpati')