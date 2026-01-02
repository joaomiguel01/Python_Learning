# Python Banking Program

def show_balance(balance):
    print("~"*20)
    print(f"Your balance is: ${balance:.2f}")
    print("~"*20)


def deposit():
    print("~"*20)
    amount = float(input("Enter an amount to be deposited: "))
    print("~"*20)

    if amount < 0:
        print("~"*20)
        print("That's not a valid amount")
        print("~"*20)
        return 0
    else:
        return amount


def withdraw(balance):
    print("~"*20)
    amount = float(input("Enter amount to be withdrawn: "))
    print("~"*20)

    if amount > balance:
        print("~"*20)
        print("Insufficient funds")
        print("~"*20)
        return 0
    elif amount < 0:
        print("~"*20)
        print("Amount must be greater than 0")
        print("~"*20)
        return 0
    else:
        return amount




def main():
    balance = 0
    is_running = True

    while is_running:
        print("~"*20)
        print(f"{'Banking Program':^20}")
        print("~"*20)

        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("~"*20)

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
            print("~"*20)
            print("That is not valid choice")
            print("~"*20)
    print("~"*20)
    print("Thank you! have a nice day!")
    print("~"*20)


if __name__ == "__main__":
    main()