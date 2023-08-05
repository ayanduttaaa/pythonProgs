#checking if input is palindrome or not
num = int(input("Enter number (>0) : "))
temp = num
store = 0
while temp != 0:
    rem = temp % 10
    store = store*10 + rem
    temp = temp//10
if store == num:
    print(f"Yes, {num} is a Palindrome number")
else:
    print(f"No, {num} is not a Palindrome number")
    
