
accounts = {
    "1234": {"name": "Desola", "balance": 50000, "history": [], "withdrawn_today": 0},
    "5678": {"name": "Eki", "balance": 15000, "history": [], "withdrawn_today": 0},
    "3242": {"name": "John", "balance": 87000, "history": [], "withdrawn_today": 0}
}

withdrawal_limit = 20000


def login():
    attempts = 3
    while attempts > 0:
        pin = input("Enter your PIN: ")
        if pin in accounts:
            return pin
        else:
            attempts = attempts - 1
            print("Wrong PIN. You have", attempts, "attempts left.")
    print("Too many wrong attempts. Exiting.")
    return None


def check_balance(pin):
    balance = accounts[pin]["balance"]
    print("Your balance is:", balance)


def deposit(pin):
    amount = float(input("Enter amount to deposit: "))
    if amount <= 0:
        print("You can't deposit zero or negative money.")
        return

    accounts[pin]["balance"] += amount
    accounts[pin]["history"].append("Deposited " + str(amount))
    print("Deposit successful. New balance:", accounts[pin]["balance"])


def withdraw(pin):
    amount = float(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("You can't withdraw zero or negative money.")
        return

    if amount > accounts[pin]["balance"]:
        print("Insufficient funds.")
        return

    remaining_limit = withdrawal_limit - accounts[pin]["withdrawn_today"]
    if amount > remaining_limit:
        print("You have reached your daily withdrawal limit.")
        print("You can only withdraw up to", remaining_limit, "more today.")
        return

    accounts[pin]["balance"] -= amount
    accounts[pin]["withdrawn_today"] += amount
    accounts[pin]["history"].append("Withdrew " + str(amount))
    print("Withdrawal successful. New balance:", accounts[pin]["balance"])


def transfer(pin):
    receiver_pin = input("Enter the PIN of the account to send money to: ")

    if receiver_pin == pin:
        print("You cannot transfer money to yourself.")
        return

    if receiver_pin not in accounts:
        print("That account does not exist.")
        return

    amount = float(input("Enter amount to transfer: "))

    if amount <= 0:
        print("You can't transfer zero or negative money.")
        return

    if amount > accounts[pin]["balance"]:
        print("Insufficient funds.")
        return

    accounts[pin]["balance"] -= amount
    accounts[receiver_pin]["balance"] += amount

    accounts[pin]["history"].append("Sent " + str(amount) + " to " + receiver_pin)
    accounts[receiver_pin]["history"].append("Received " + str(amount) + " from " + pin)

    print("Transfer successful. New balance:", accounts[pin]["balance"])


def show_history(pin):
    print("Transaction History:")
    if len(accounts[pin]["history"]) == 0:
        print("No transactions yet.")
    else:
        for item in accounts[pin]["history"]:
            print("-", item)


def change_pin(pin):
    new_pin = input("Enter your new 4-digit PIN: ")

    if len(new_pin) != 4 or new_pin.isdigit() == False:
        print("PIN must be exactly 4 digits.")
        return pin

    if new_pin in accounts:
        print("That PIN is already taken.")
        return pin

    accounts[new_pin] = accounts.pop(pin)
    print("PIN changed successfully.")
    return new_pin


def show_menu():
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Transaction History")
    print("6. Change PIN")
    print("7. Exit")


def main():
    print("Welcome to the ATM")
    pin = login()

    if pin is None:
        return

    running = True
    while running:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            check_balance(pin)
        elif choice == "2":
            deposit(pin)
        elif choice == "3":
            withdraw(pin)
        elif choice == "4":
            transfer(pin)
        elif choice == "5":
            show_history(pin)
        elif choice == "6":
            pin = change_pin(pin)
        elif choice == "7":
            print("Thank you for using the ATM. Goodbye!")
            running = False
        else:
            print("Invalid option. Please choose between 1 and 7.")


main()