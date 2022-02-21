num = int(input("Enter a value:"))
check = num
rev_num = 0
while(num > 0):
    dig = num % 10
    rev_num = rev_num * 10 + dig
    num = num // 10
if(check == rev_num):
    print("True")
else:
    print("False")
