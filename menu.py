def Menu():
    global balance, new_balance, attempts
    while True:

        if menu == 1:
            deposit_amount = int(input("How much would you like to deposit?: "))
            if deposit_amount > 0:
                new_balance = balance + deposit_amount
                balance = new_balance
                print("Your new balance is: $", new_balance)
            else:
                print("You cannot deposit 0 or less.")

        if menu == 2:
            withdraw_amount = int(input("How much would you like to withdraw?: "))
            new_balance = balance - withdraw_amount
            balance = new_balance

            if withdraw_amount > balance:
                deduction = new_balance - 5
                print("For withdrawing more than available, a penalty of $5 has been deducted from balance")
                print("Your new balance is $", deduction)

            if withdraw_amount > 0:
                print("Withdraw successful.")
                print("Your new balance is: $", new_balance)

            if withdraw_amount <= 0:
                print("You cannot withdraw 0 or less")
        else:
            pass

    if menu == 3:
        print("Final statement")
        print("Balance:", new_balance)
        print("Total amount of funds deposited:", deposit_amount)
        print("Total amount of funds withdrawn:", withdraw_amount)
        print("Total amount of funds unsuccessfully withdrawn:", attempts)

    else:
        print("Not an available option, Please try again.")

Menu()
