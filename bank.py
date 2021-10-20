# Pedro A. Matos Villanueva
#802213189
global balance
global selection
global d_count
global w_count
global sw_count
global fee
global fee_amount
global deposit
global withdraw
d_count = 0
w_count = 0
sw_count = 0
fee = 0
fee_amount = 0
withdraw_total = 0
deposit_total = 0
bad_withdraws = 0
account = (input("New Account Name: "))
while not account.isalpha():
    print("Invalid format, Try again.")
    account = str(input("New Account Name: "))

balance = (float(input("Starting Balance: ")))

round(balance,2)

while balance <= 0:
    print("Starting balance cannot be 0 or less")
    balance = float(input("Starting Balance: "))

print("Account name:", account)

print("Current Balance:$", balance)

def menu():
    global balance
    global selection
    global d_count
    global w_count
    global sw_count
    global fee
    global fee_amount
    global deposit
    global withdraw
    global withdraw_total
    global deposit_total
    global bad_withdraws
    print("-------------------------")
    print("Options: ")
    print("1) Deposit some funds")
    print("2) Withdraw some funds")
    print("3) Quit")
    selection = int(input("Please enter your selection: "))
    if selection == 1:
        deposit = (float(input("Amount to deposit: ")))
        balance = balance + deposit
        deposit_total += deposit
        d_count += 1
        print("Account:", account)
        print("New Balance:$", balance)
        print(menu())
    if selection == 2:
        withdraw = float(input("Amount to withdraw: "))
        if balance < withdraw:
            num = 5
            balance = balance - num
            bad_withdraws += num
            fee += 1
            fee_amount += 5
            w_count += 1
            withdraw_total += withdraw
            print("For withdrawing more than available, a penalty of $5 has been deducted from balance")
            print("Your new balance is $", balance)
            print(menu())
        else:
            balance = balance - withdraw
            withdraw_total += withdraw
            sw_count += 1
            print("Account:", account)
            print("New Balance:$", balance)
            print(menu())
    if selection == 3:
        print("Final statement")
        print("Account:",account)
        print("Balance:",balance)
        print(d_count,"deposits totaling",deposit_total)
        print(sw_count,"withdrawals totaling",withdraw_total)
        print(w_count,"bad withdraws totaling",bad_withdraws)
        print(fee,"fees totaling",fee_amount)
    if selection >= 4:
        print("Not an available option, try again.")
        print(menu())

menu()















