import threading
import time
import csv
from Customer_Account import Customer_Account

class BankSys:
    def __init__(self, data_file):
        self.data_file = data_file
        self.customers = {}
        self.customer_info()

    # Function to read customer data or information
    def customer_info(self):
        with open(self.data_file, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                if len(row) == 4: 
                    customer_id, name, account_balance, acc_type = row
                    self.customers[customer_id] = Customer_Account(customer_id, name, account_balance, acc_type)

    # The function starts the thread that counts the interest for savings account periodically
    def interest_thread(self):
        def log_trans():
            while True:
                for customer in self.customers.values():
                    if customer.acc_type == 'Savings':
                        customer.apply_interest()  
                time.sleep(3600) 

        # Creating and starting the thread
        interest_thread = threading.Thread(target=log_trans, daemon=True)
        interest_thread.start()

    # Function to update the balance in the data.csv file
    def update_bal(self, customer_id, new_balance):
        rows = []
        updated = False
        with open(self.data_file, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)

        #if customer exists the print statement lets us know
        print(f"Customer ID: {customer_id},\nNew Balance: {round(new_balance, 2)}")

        for i, row in enumerate(rows):
            if len(row) == 4 and row[0] == customer_id:
                rows[i][2] = str(round(new_balance, 2))
                updated = True
                break

        if updated:
            with open(self.data_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
        else:
            print(f"Customer ID {customer_id} not found. Please check customerID once more")

    # Creates new user accounts in the bank
    def create_account(self, customer_id, name, bal_initial, acc_type):
        with open(self.data_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([customer_id, name, round(bal_initial, 2), acc_type])

        # Create customer account object
        self.customers[customer_id] = Customer_Account(customer_id, name, bal_initial, acc_type)

        #Initial transaction
        with open('transaction.csv', mode='a', newline='') as file:
            writer = csv
