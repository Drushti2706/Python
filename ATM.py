balance = 1000

while True:
    print("\n1.Check Balance\n2.Deposit\n3.Withdraw\n4.Exit")
    opt = input("Choose: ")
    if opt == "1":
        print("Balance: ₹", balance)
    elif opt == "2":
        amt = float(input("Enter deposit: ₹"))
        balance += amt
    elif opt == "3":
        amt = float(input("Enter withdraw: ₹"))
        if amt <= balance:
            balance -= amt
        else:
            print("Insufficient funds")
    elif opt == "4":
        break
