num = int(input("Enter number (>0) : "))
temp = num
res = 1
while temp>0:
    res = res * temp
    temp=temp-1
print(f"The factorial of {num} is {res}")


count = 0
fact = res
while fact % 10 == 0:
    rem = fact % 10
    fact = fact // 10
    count += 1

print(f"Number of trailing zeros in the factorial of {num} is {count}")


    
    
