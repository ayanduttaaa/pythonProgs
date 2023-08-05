#getting factorial of number 
num = int(input("Enter number (>0) : "))
temp = num #temp is declared just for printing purpose
res = 1
while num>0:
    res = res * num
    num=num-1

print(f"The factorial of {temp} is {res}")
    
