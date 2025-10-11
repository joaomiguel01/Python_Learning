# Python Banking Program

def show_balance(balance):
    print("*"*25)
    print(f"Your balance is ${balance:.2f}")
    print("*"*25)


def deposit():
    print("*"*25)
    amount = float(input("Enter an amount to be deposited: "))
    print("*"*25)

    if amount < 0:
        print("*"*25)
        print("That's not a valid amount")
        print("*"*25)
        return 0
    else:
        return amount


def withdraw(balance):
    print("*"*25)
    amount = float(input("Enter amount to be withdrawn: "))
    print("*"*25)

    if amount > balance:
        print("*"*25)
        print("Insufficient funds")
        print("*"*25)
        return 0
    elif amount < 0:
        print("*"*25)
        print("Amount must be greater than 0")
        print("*"*25)
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("*"*25)
        print(f"{'Banking Program':^25}")
        print("*"*25)
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("*"*25)
            print("That is not valid choice!")
            print("*"*25)
    print("*"*25)
    print("Thank you! Have a nice day!")
    print("*"*25)

if __name__ == '__main__':
    main()