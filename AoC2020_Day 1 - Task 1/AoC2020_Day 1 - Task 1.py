file = open('Expense Report.txt','r')
nums = file.read().splitlines()

for x in nums:
    for y in nums:
        if (int(y) + int(x)) == 2020:
            print(x)
            print(y)
            print("Answer is: ", int(y) * int(x))
        
        
file.close()