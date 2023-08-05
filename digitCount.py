#digit count of number
num = int(input("Enter number : "))
i = 0
count = 0
temp = num

while temp > 0:
    temp = temp // 10  
    count = count + 1

print(f"The digit count of {num} is {count}")
