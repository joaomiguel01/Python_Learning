# Python Slot Machine
from random import choice


def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]

    return [choice(symbols) for _ in range(3)]      

def print_row(row):
    print("~"*30)
    print(" | ".join(row))
    print("~"*30)


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20
    
    return 0


def main():
    balance = 100

    print("~"*30)
    print(f"{'Welcome to Python Slots':<30}")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("~"*30)

    while balance > 0:
        print(f"Current balance: R${balance}")

        bet = str(input("Place your bet amount: "))

        if not bet.isdigit():
            print("Please enter a valid number")
            continue


        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue


        if bet <= 0:
            print("Bet must be greater than 0")
            continue


        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won R${payout}")
        else:
            print("Sorry you lost this round")

        balance += payout

        play_again = input("Do you want to spin again? (Y/N): ").upper()

        if play_again != "Y":
            break
    
    print("~"*30)
    print(f"Game over! Your final balance is R${balance}")
    print("~"*30)

if __name__ == "__main__":
    main()