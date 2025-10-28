# Python Banking Program

def show_balance(balance):
    print("********************************")
    print(f"\nYour balance is ${balance:.2f}\n")
    print("********************************")

def deposit():
    print("********************************")
    amount = float(input("Enter an amount to be deposit: $"))
    print("********************************")
    if amount < 0:
        print("\nThat's not a valid amount\n")
        return 0
    else:
        return amount
    

def withdraw(balance):
    print("********************************")
    amount = float(input("Enter amount to be withdraw: $"))
    print("********************************")

    if amount > balance:
        print("\nInssufficient funds\n")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("********************************")
        print("Banking Program")
        print("1. Show Balance \n2. Deposit \n3. Withdraw \n4. Exit")
        print("********************************\n")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("\nThat is not a valid choice")
    print("********************************")
    print("Thank you! Have a nice day!")
    print("********************************")

if __name__ == "__main__":
    main()