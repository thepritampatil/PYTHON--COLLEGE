day_number = int(input("Enter a number bet 1 to 7 :"))

match day_number:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("sunday")
    case _:
        print("Invaild input please enter number between 1 to 7 ")
