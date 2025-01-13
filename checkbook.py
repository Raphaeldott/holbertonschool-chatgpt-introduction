#!/usr/bin/python3
class Checkbook:
    """
    A simple checkbook system that allows deposits, withdrawals, 
    and checking the current balance.

    Attributes:
        balance (float): The current balance in the checkbook.
    """

    def __init__(self):
        """
        Initialize the checkbook with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a specified amount into the checkbook.

        Parameters:
            amount (float): The amount to be deposited.

        Returns:
            None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the checkbook.

        Parameters:
            amount (float): The amount to be withdrawn.

        Returns:
            None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Display the current balance in the checkbook.

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main function to interact with the Checkbook class.

    Prompts the user to perform actions such as deposit, withdraw,
    check balance, or exit the program. Handles invalid input gracefully.

    Returns:
        None
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            print("Thank you for using the checkbook. Goodbye!")
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount < 0:
                    print("Error: Amount must be a positive number.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Error: Please enter a valid numeric value.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount < 0:
                    print("Error: Amount must be a positive number.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Error: Please enter a valid numeric value.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()

