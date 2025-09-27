# # # # 
# # # # 
# # # num=int(input("Enter a number:"))

# # # if num % 5 == 0: # divisible by 5
# # #     if num % 2==0: # check even
# # #         print(f"{num} is Even and divisible by 5")
# # #     else:
# # #         print(f"{num} is Odd and divisible by 5")
# # # else:
# # #     print(f"{num} is not divisible by 5")
# # # Password Strength Checker

# # password = input("Enter your password: ")

# # # Check length first
# # if len(password) < 6:
# #     print("Weak Password")
# # else:
# #     # Flags
# #     has_digit = False
# #     has_alpha = False
# #     has_special = False

# #     for ch in password:
# #         if ch.isdigit():
# #             has_digit = True
# #         elif ch.isalpha():
# #             has_alpha = True
# #         else:
# #             has_special = True

# #     # Conditions
# #     if has_alpha and not has_digit and not has_special:
# #         print("Medium Password")
# #     elif has_alpha and has_digit and not has_special:
# #         print("Strong Password")
# #     elif has_alpha and has_digit and has_special:
# #         print("Very Strong Password")
# #     else:
# #         print("Weak Password")



# age = int (input("Enter age of the person:"))
# salary =int(input("Enter the salary of person :"))

# if age >= 21 and salary >= 50000:
#     print("You are eligible for loan ")
# else:
#     print("you are not eligible for the loan application")

# string slicing

str ="Pritam"

print(str[0:6])