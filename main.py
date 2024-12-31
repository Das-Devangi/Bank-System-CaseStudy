import time
from Sys_Bank import BankSys
from Customer_Account import Customer_Account

def main():
    bank_system = BankSys('data.csv')
    bank_system.interest_thread()

    while True:
        print("\n--- Welcome to the Banking System ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Transactions")
        print("5. Show Interest (for Savings Account)")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            # Create Account
            customer_id = input("Enter customer ID: ")
            name = input("Enter customer name: ")
            bal_initial = float(input("Enter initial balance: "))
            acc_type = input("Enter account type (Savings/Current)ony one of them: ")
            bank_system.create_account(customer_id, name, bal_initial, acc_type)
            print(f"Account created for {name}.")

        elif choice == '2':
            # Deposit
            customer_id = input("Enter customer ID: ")
            amount = float(input("Enter deposit amount: "))
            customer = bank_system.customers.get(customer_id)
            if customer:
                print(customer.deposit(amount, bank_system))
            else:
                print("Customer not found.")

        elif choice == '3':
            # Withdraw
            customer_id = input("Enter customer ID: ")
            amount = float(input("Enter withdrawal amount: "))
            customer = bank_system.customers.get(customer_id)
            if customer:
                print(customer.withdraw(amount, bank_system))
            else:
                print("Customer not found.")

        elif choice == '4':
            # View Transactions
            customer_id = input("Enter customer ID: ")
            customer = bank_system.customers.get(customer_id)
            if customer:
                transactions = customer.trans_his()
                for transaction in transactions:
                    print(transaction)
            else:
                print("Customer not found.")

        elif choice == '5':
            # Show Interest for Savings Account
            customer_id = input("Enter customer ID: ")
            customer = bank_system.customers.get(customer_id)
            if customer and customer.acc_type == 'Savings':
                print(customer.show_interest())  
            else:
                print("No savings account found or customer not found.")

        elif choice == '6':
            # Exit
            print("Thank you for using the bank system.")
            break

        else:
            print("Invalid option. Please try again.")

        # time.sleep(10)

if __name__ == "__main__":
    main()