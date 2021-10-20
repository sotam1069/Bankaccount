 ##Bank Account Simulator CIIC 3015
 
 Your assignment is to write a simple bank account simulator. The required behavior is as 
 follows: 
 The first thing your simulator should do is ask for the name of a new account to create. 
 The second thing your simulator should do is ask for a starting balance. 
 Once the above information has been provided, it is time to enter the main loop. Print the name 
 of the account and the current balance, then present your user with the following menu of 
 options: 
 1)   Deposit some funds. 
 2)   Withdraw some funds. 
 3)   Quit. 
 For the first two options, ask the user for the appropriate amount, update their balance 
 accordingly, and then loop. 
 If the user attempts to withdraw more funds than are currently available, that is considered an 
 unsuccessful withdrawal attempt and the amount is  not  subtracted from the balance. Instead, a 
 penalty of $5 is deducted from the balance. Note that negative account balances are possible. 
 For the final option, print the final balance, the total amount of funds deposited, the total amount 
 of funds successfully withdrawn, the total amount of funds unsuccessfully withdrawn, and the 
 total amount of penalties. And then exit from the simulatio
