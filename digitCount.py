#digit count of number
num = int(input("Enter number : "))
count = 0
while num > 0:
    num = num // 10  
    count = count + 1

print(f"The digit count of {num} is {count}")
