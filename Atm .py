# Today we make a bank Atm process
import time

print("Welcome to Allied Bank Bahawalpur")
print("Insert your Atm card-------")
time.sleep(5)
Acount =int(input("Enter your acount number:"))
code = int(input("Enter your code:"))
if code in range(10000):
    print("welcome to your Acount And enter amount")
    Balance = 1000000
    print("your current balance is", Balance)
    print(
        '''
        1 == Balance
        2 == withdraw_balance
        3 == deposit balance
        4 == Exit
    '''
          )
    try:
        option = int(input("Enter your option:"))
    except:
        print("please enter valid option")
    if option == 1:
        print("your current balance is", Balance)
    if option == 2:
        withdraw_amount = int(input("please enter your withdraw amount:"))
        balance = Balance-withdraw_amount
        print("your  remaining balance after withdraw is", balance)
    if option == 3:
        deposit = int(input("plaese deposit your amount:"))
        balance = Balance+deposit
        print("your Balance after deposit is", balance)
    if option==4:
        print("Exit")
        'break'
    recipt = input("you take your recipt or not:")
    if recipt == "yes":
        print("ok")
    else:
        print("Go green")
else:
    print("your code is wrong")
print("Thanks for use our bank Atm machine")





