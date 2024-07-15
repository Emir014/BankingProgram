import csv
import sys
import time

balance = 0
username, password = "", ""


def write_to_csv(username, password):
    with open("user_data.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["username", "password", "balance"])
        writer.writeheader()
        writer.writerow({"username": username, "password": password, "balance": balance})


def read_from_csv():
    try:
        with open("user_data.csv") as file:
            reader = csv.reader(file)
            user_data = list(reader)
        return user_data
    except FileNotFoundError:
        return []


def save_balance(username, password, balance):
    rows = []

    with open("user_data.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["username"] == username and row["password"] == password:
                row["balance"] = balance
            rows.append(row)

    with open("user_data.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["username", "password", "balance"])
        writer.writeheader()
        writer.writerows(rows)


def load_balance(username, password):
    global balance
    with open("user_data.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["username"] == username and row["password"] == password:
                balance = row["balance"]
    balance = int(balance)
    return balance


def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    password1 = input("Enter your password again: ")
    if password == password1 and username and password:
        write_to_csv(username, password)
        print("Registration successful!")
    elif password != password1:
        print("\nPasswords didn't match!")
    elif not username:
        print("Username cannot be empty!")
    elif not password:
        print("Password cannot be empty!")


def login():
    global username
    global password
    logged_in = False
    input_username = input("Enter your username: ")
    input_password = input("Enter your password: ")

    user_data = read_from_csv()

    if user_data:
        for row in user_data:
            if row[0] == input_username and row[1] == input_password:
                balance = int(row[2])
                print("Login successful!")
                username = input_username
                password = input_password
                logged_in = True
                break
        if not logged_in:
            print("Invalid username or password.")
    else:
        print("No users registered. Please register first.")

    return logged_in


def get_pos_float(prompt, action):
    while True:
        try:
            n = round(float(input(prompt)), 2)
            if n == int(n):
                n = int(n)
            if n < 0:
                print(f"You can only {action} positive amount of money!")
            else:
                return n
        except ValueError:
            print("You must enter a number!")


def deposit():
    global balance
    print(f"Balance: {balance}")
    n = get_pos_float("Enter the amount you want to deposit: ", "deposit")
    balance += n
    print(f"Balance: {balance}")

def withdraw():
    global balance
    print(f"Balance: {balance}")
    n = get_pos_float("Enter the amount you want to withdraw: ", "withdraw")
    if n <= balance:
        balance -= n
        print(f"Balance: {balance}")
    else:
        print("Insufficient funds!")


def first_menu(logged_in):
    text = """
-----------------------
1) Register           |
2) Login              |
3) Exit               |
                      
Choose an action (1-3): """
    while not logged_in:
        while True:
            try:
                choice = int(input(text))
                break
            except ValueError:
                print("You must enter a number!")

        match choice:
            case 1:
                register()
            case 2:
                logged_in = login()
            case 3:
                sys.exit("Exiting program...")
            case _:
                print("Invalid number!")

    return logged_in


def second_menu(logged_in):
    text = """
-----------------------
1) Deposit            |
2) Withdraw           |
3) Exit               |
    
Choose an action (1-3): """

    if logged_in:
        print(f"Balance: {load_balance(username, password)}")
        while True:
            while True:
                try:
                    choice = int(input(text))
                    break
                except ValueError:
                    print("You must enter a number!")

            match choice:
                case 1:
                    deposit()
                case 2:
                    withdraw()
                case 3:
                    save_balance(username, password, balance)
                    sys.exit("Exiting program")
                case _:
                    print("Invalid number!")


def main():
    print("Welcome to a banking program.")
    time.sleep(0.5)
    logged_in = first_menu(False)
    second_menu(logged_in)

if __name__ == "__main__":
    main()
