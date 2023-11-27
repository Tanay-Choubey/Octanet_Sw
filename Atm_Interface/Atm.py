from tabulate import tabulate
import sys

# Define a class named "ATM" to represent the ATM functionality.
class ATM:
    # Initialize the ATM with an initial balance, current balance, and an empty transaction history.
    def __init__(self):
        self.initial_balance = 100000
        self.balance = self.initial_balance
        self.transaction_history = []

    # Define a method for depositing money into the ATM.
    def deposit(self, amount):
        self.balance += amount
        transaction_detail = f'Deposited ${amount}'
        self.transaction_history.append(transaction_detail)
        return f'\nDeposited ${amount}\nNew balance: ${self.balance}'

    # Define a method for withdrawing money from the ATM.
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f'Withdrawn ${amount}')
            return f'\nWithdrawn ${amount}\nNew balance: ${self.balance}'
        else:
            return 'Insufficient funds'


    # Define a method for transferring money from the ATM to another recipient.
    def transfer(self, amount, recipient, transfer_type):
        if amount <= self.balance:
            self.balance -= amount
            if transfer_type == 1:
                transaction_detail = f'Transferred ${amount} to {recipient}'
                self.transaction_history.append(transaction_detail)
            elif transfer_type == 2:
                transaction_detail = f'Transferred ${amount} to {recipient}'
                self.transaction_history.append(transaction_detail)
            elif transfer_type == 3:
                transaction_detail = f'Transferred ${amount} to {recipient}'
                self.transaction_history.append(transaction_detail)
            return f'Transferred ${amount}{recipient}New balance: ${self.balance}'
        else:
            return 'Insufficient funds'

    # Define a method to get the current balance.
    def get_balance(self):
        return f'Current balance: ${self.balance}'

    # Define a method to get the transaction history.
    def get_transaction_history(self):
        return self.transaction_history


def atm_interface():

    # Create an instance of the ATM class.
    atm = ATM()

    
    # Print a welcome message.
    print("\n*****Welcome to the ATM Interface by TANAY CHOUBEY*****")

    # Prompt the user to enter a User ID and PIN.
    user_id = input("\nEnter User ID: ")
    pin = input("Enter PIN: ")

    # Check if the entered User ID and PIN are valid.
    if user_id == "123456" and pin == "654321":
        print("\nLogin successful!")

        while True:
            # Display the available ATM operations to the user.
            print("\nATM Operations:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer")
            print("4. Check Balance")
            print("5. Transaction History")
            print("6. Quit\n")

            # Prompt the user to enter their choice.
            choice = input("\nEnter your choice (1/2/3/4/5/6): ")

            if choice == "1":
                amount = float(input("\nEnter the deposit amount: $"))
                pass_code = input("Enter 4 or 6 digit pass_code: ")
                pass_code_display = '*' * len(pass_code)
                result = atm.deposit(amount)
                print(f"{result}\nPass_code: {pass_code_display}")
            elif choice == "2":
                amount = float(input("\nEnter the withdrawal amount: $"))
                pass_code = input("Enter 4 or 6 digit pass_code: ")
                pass_code_display = '*' * len(pass_code)
                result = atm.withdraw(amount)
                print(f"{result}\nPass_code: {pass_code_display}")
            elif choice == "3":
                print("\nChoose Transfer Type:")
                print("1. Account Transfer")
                print("2. Phone Transfer")
                print("3. Card Transfer")
                transfer_type = int(input("\nEnter your choice (1/2/3): "))

                
                amount = float(input("Enter the transfer amount: $"))
                recipient = input("\nEnter the recipient's name: ")

                transfer_details = f"\nRecipient: {recipient}"

                if transfer_type == 1:
                    account_no = input("Enter recipient's account number: ")
                    ifsc_code = input("Enter recipient's account IFSC code: ")
                    pass_code = input("Enter 4 or 6 digit pass_code: ")
                    pass_code_display = '*' * len(pass_code)
                    transfer_details = f"\nRecipient: {recipient}\nAccount: {account_no}\nIFSC: {ifsc_code}\nPasscode: {pass_code_display}\n"
                    result = atm.transfer(amount, transfer_details, transfer_type)
                elif transfer_type == 2:
                    phone_number = input("Enter recipient's phone number: ")
                    upi_id = input("Enter UPI ID: ")
                    pass_code = input("Enter 4 or 6 digit pass_code: ")
                    pass_code_display = '*' * len(pass_code)
                    transfer_details = f"\nRecipient: {recipient}\nPhone: {phone_number}\nUPI: {upi_id}\nPasscode: {pass_code_display}\n"
                    result = atm.transfer(amount, transfer_details, transfer_type)
                elif transfer_type == 3:
                    card_number = input("Enter recipient's card number: ")
                    pass_code = input("Enter 4 or 6 digit pass_code: ")
                    pass_code_display = '*' * len(pass_code)
                    transfer_details = f"\nRecipient: {recipient}\nCard: {card_number}\nPasscode: {pass_code_display}\n"
                    result = atm.transfer(amount, transfer_details, transfer_type)
                else:
                    result = "\nInvalid transfer type selection."
                    transfer_details = "N/A"
                print(f'\n{result}')
            elif choice == "4":

                balance = atm.get_balance()
                pass_code = input("Enter 4 or 6 digit pass_code: ")
                pass_code_display = '*' * len(pass_code)
                print(f"\n{balance}\nPass_code: {pass_code_display}\nAvailable Balance: ${atm.balance:.2f}")
            
            elif choice == "5":
                pass_code = input("Enter 4 or 6 digit pass_code: ")
                pass_code_display = '*' * len(pass_code)

                atm.pass_code = pass_code

                history = atm.get_transaction_history()

                if len(history) > 0:
                    table = []
                    available_balance = atm.initial_balance
                    for i, transaction in enumerate(history, start=1):
                        transaction_parts = transaction.split('$')
                        if len(transaction_parts) > 1:
                            transaction_amount = float(transaction_parts[-1].split()[0])

                            if "Deposited" in transaction:
                                available_balance += transaction_amount
                            elif "Withdrawn" in transaction or "Transferred" in transaction:
                                available_balance -= transaction_amount

                        table.append([i, transaction, f"${available_balance:.2f}"])
                    print(tabulate(table, headers=["#", "Transaction", "Available Balance"], tablefmt="grid"))
                else:
                    print("\nTransaction history is empty.")

            elif choice == "6":
                print("\nThank you for using ATM. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please enter a valid option.")

        # Check if the user wants to continue using the ATM
        continue_choice = input("\nDo you want to perform another transaction? (yes/no): ")

        if continue_choice.lower() != "yes":
            print("\nThank you for using ATM. Goodbye!")
    else:
        print("\nInvalid User ID or PIN. Exiting...")
        sys.exit() 

# Check if the script is being run as the main program.
if __name__ == "__main__":

# Call the "atm_interface" function to start the ATM application.
    atm_interface()