#finding number of trailing zeros in factorial
num = int(input("Enter number (>0) : "))
temp = num #temp is declared just for printing purpose
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


i = 5
zeroc = 0
while i<=num:
    zeroc = zeroc + num//i
    i = i * 5
print(f"Number of trailing zeros in the factorial of {num} is {zeroc} [efficient algo]")
    
    
