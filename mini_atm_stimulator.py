import sys
PIN ="90346"
balance = 100000000
daily_limit = 20000
history = []
def check_balance(balance):
    print(f"Your current balance is Rs.{balance}")
    return balance
def deposit(balance, amount, history):
    if amount > 0:
        balance += amount
        history.append(f"Total amount: Rs.{amount}")
        print(f"Rs.{amount} deposited suceesfully")  
    else:
        print("INVALID AMOUNT")     
    return balance
def withdraw(balance, amount, history, daily_limit):
    if amount > daily_limit:
        print(f"Cannot withdraw more than daily limit"
              f"Your daily limit is {daily_limit}")
    elif amount > balance:
        print(f"Insufficient balance" 
        f"Total_balnce id {balance}")  
    elif amount<= 0:
        print("Invalid withdrawl")
    else:
        balance -= amount
        history.append(f"Total amount: Rs.{amount}")
        print(f"Rs.{amount} withdrawl sucessfully")
    return balance   
def show_history(history):
    if not history:
        print("Not transcation")
    else:
        print("Transcation history:")
        for text in history:
            print(text)  
pin = int(input("Enter your pin:"))
if pin != PIN:
    print("Incorrect pin. Try again!")
    sys.exit()
else:
    print("Login successfully!")
while True:
    print("ATM STIMULATOR")
    print("1. Check balance")
    print("2. Deposit amount")
    print("3. Withdraw Amount")
    print("4. Show history")
    print("5. Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1: 
        print("Total balance:", check_balance(balance))
    elif choice == 2:    
        print("Deposit amount:", deposit(balance, 30000, history))
    elif choice == 3:
        print("Withdrawl amount:", withdraw(balance, 15000, history, daily_limit))
    elif choice == 4:   
        show_history(history)
    else:
        print("Invalid Amount")    
 

