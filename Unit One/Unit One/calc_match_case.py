num1 =float(input("Enter 1st number: "))
operator =input("Enter operator (+ ,-,*,/): ")
num2 =float(input("Enter 2nd number: "))

match operator:
    case '+':
        print(f"Result:{num1 + num2}")
    case '-':
        print(f"Result:{num1 - num2}")
    case '*':
        print(f"Result:{num1 * num2}")
    case '/':
        if (num2!=0):
            print(f"Result:{num1 / num2}")
        else:
            ("Error : Cannot divide by zero.")
    case _:
        print("invaild operator")
        
    
