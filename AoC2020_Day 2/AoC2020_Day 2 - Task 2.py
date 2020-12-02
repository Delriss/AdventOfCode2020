import re

file = open('passwords.txt','r')

validPassword = 0
for x in file:
    num1, num2, letter, password = re.split('-| |: ', x)
    letterCount = password.count(letter)
    print(num1,num2,letterCount)
    if (password[(int(num1)-1)] == letter and password[int(num2)-1] != letter) or (password[(int(num1)-1)] != letter and password[int(num2)-1] == letter):
        validPassword += 1
        
print(validPassword)