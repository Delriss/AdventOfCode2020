file = open('Expense Report.txt','r')
nums = file.read().splitlines()

for x in nums:
    for y in nums:
        for z in nums:
            if (int(y) + int(x) + int(z)) == 2020:
                print(x)
                print(y)
                print(z)
                print("Answer is: ", int(y) * int(x) * int(z))
        
        
file.close()