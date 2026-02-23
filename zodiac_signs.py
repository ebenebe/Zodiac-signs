
# Problem Statement:

# Given the birthdate and name of the person, you want to create a Python program to determine 
# the corresponding Zodiac sign based on the date.
# Question:

# How can you write a Python program that takes name and birthdate as input and outputs 
# the corresponding Zodiac sign and store it in a file using Pandas?

import pandas as pd
from datetime import datetime 


def run_zodiac_sign(month,day):
    if(month == 1 and day >=20) or (month == 2 and day <= 18):
        return 'Aquarius'
    elif(month == 2 and day >= 19) or (month == 3 and day <= 20):
        return 'Pisces'
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return 'Aries'
    elif(month == 4 and day >= 20) or (month == 5 and day <= 20):
        return 'Taurus'
    elif(month == 5 and day >= 21) or (month == 6 and day <= 20):
        return 'Gemini'
    elif(month == 6 and day >= 21) or (month ==7 and day <= 22):
        return 'Cancer'
    elif(month == 7 and day >= 23) or (month == 8 and day <= 22):
        return 'Leo'
    elif(month == 8 and day >= 23) or (month == 9 and day <= 22):
        return 'Virgo'
    elif(month == 9 and day >= 23) or (month == 10 and day <= 22):
        return 'Libra'
    elif(month == 10 and day >= 23) or (month == 11 and day <= 21):
        return 'Scorpio'
    elif(month == 11 and day >= 22) or (month == 12 and day <= 21):
        return 'Sagittarius'
    elif(month == 12 and day >= 22) or(month == 1 and day <= 19):
        return 'Capricorn'
    

# Prompt for user details

user_name = input('Please Enter your Name:')

# Validate user date of birth input and convert data to date format
while True:
    user_DOB = input('Enter your Date of Birth (dd-mm-yyyy):')
    try:
        user_DOB = datetime.strptime(user_DOB,'%d-%m-%Y').date()
        break
    except ValueError:
        print('Invalid date format! please use dd-mm-yyyy (example: 13-05-1999)')

# separate month and day from user date of birth
day = user_DOB.day
month = user_DOB.month

#function call
user_zodiac_sign = run_zodiac_sign(month,day)

# use dataframe to store output in a fle
data = {'Name':[user_name],'Birthdate':[user_DOB],'Zodiac_sign':[user_zodiac_sign]}
df = pd.DataFrame(data)
df.to_csv('zodiac_data.csv',index= False)
print(f"\n Hello {user_name}, your zodiac sign is {user_zodiac_sign}")
print("data has been saved to zodiac_data.csv")






