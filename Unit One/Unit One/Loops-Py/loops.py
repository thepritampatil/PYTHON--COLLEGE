'''
# sum of digits
num =int(input("Enter a number :"))
sum_of_digits =0
while num > 0:
    digits = num % 10 # last digit
    sum_of_digits += digits # add in it
    num = num //10 # remove 
    
print("sum of digits",sum_of_digits)

'''
'''
# Reverse a number

num = int(input("Enter a number:"))

rev =0;

while num > 0:
    digit =num % 10 # last digit
    rev = rev *10 + digit
    num = num//10

print("Reverse number :", rev)

 '''
'''
# check palindrome (number)
# check whether the entered number is palindrom or not 

num = int(input("Enter a number to palindrome or not:"))
original =num
rev = 0

while num > 0:
    digit = num % 10
    rev  = rev * 10 + digit
    num = num // 10


if original == rev:
    print(f"{original} is palindrome")
else:
    print(f"{original} is not palindrome")
'''

# count Digits
# input a number and count how many digit it has using a while loop ex 12345 5 - digits

num = int(input("Enter a number :"))

count =0

if num == 0:
    count = 1 
else:
    while num > 0:
     digit = num % 10
     count +=1
     num = num //10

print("total ", count)