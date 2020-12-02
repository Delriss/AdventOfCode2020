import re

file = open('passwords.txt','r')

validPassword = 0
for x in file:
    num1, num2, letter, password = re.split('-| |: ', x)
    letterCount = password.count(letter)
    print(num1,num2,letterCount)
    if letterCount <= int(num2) and letterCount >= int(num1):
        validPassword += 1
        
print(validPassword)