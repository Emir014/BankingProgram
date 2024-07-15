# Banking Program

This project is a simple banking program implemented in Python. It allows users to register, login, deposit, and withdraw money, with the data being stored in a CSV file.

## Features

- **Register**: Create a new user account with a username and password.
- **Login**: Access an existing user account with the correct username and password.
- **Deposit**: Add money to your account balance.
- **Withdraw**: Remove money from your account balance, subject to sufficient funds.
- **Balance Persistence**: User data, including balance, is saved to a CSV file (`user_data.csv`) for persistence across program runs.

## Project Structure

- `bank.py`: The main program file containing all the functions and logic for the banking operations.
- `user_data.csv`: The CSV file used to store user data (username, password, balance) This file is created when at least one user registers.

## Usage

### Running the Program

To run the program, navigate to the directory containing `banking_program.py` and execute the following command:

```sh
python bank.py
