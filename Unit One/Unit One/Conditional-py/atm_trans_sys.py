correctpin =1234
balance =5000

pin_entered =int(input("Enter your PIN: "))

if(pin_entered == correctpin):
    withdrawal_amount =int(input("Enter amount to withdraw: "))

    if(withdrawal_amount<= balance):
        balance -= withdrawal_amount
        print(f"Transaction successful.Your remaining balance is :{balance}")
    else:
        print("Insufficient funds")
else:
    print("incorrect pin")
    