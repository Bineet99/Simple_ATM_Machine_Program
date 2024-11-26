balance = 1000
print("___________________WELCOME TO ATM_________________")

while True:
    print("\n1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit\n")
    choice = input("Enter Your Choice: ")
        
    if choice == '1':
        print("Your current balance is: Rs",balance)
        
    elif choice == '2':
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print("Deposited Rs",amount,"Your new balance is Rs",balance)

    elif choice == '3':
        amount = float(input("Enter amount to withdraw: "))
        if amount > 0 and amount <= balance:
            balance -= amount
            print("You have withdrawn Rs",amount," New balance is: Rs",balance)
        elif amount > balance:
            print("Insufficient Balance! Please try again..")
        else:
            print("Insufficient Balance")
            
    elif choice == '4':
        print("Thankyou for using the ATM.")
        break
    
    else:
        print("Invalid choice, Try again.")
        break
