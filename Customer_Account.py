import threading
import csv

class Customer_Account:
    def __init__(self, cus_id, name, acc_bal, acc_type):
        self.cus_id = cus_id
        self.name = name
        self.acc_bal = round(float(acc_bal), 2)
        self.acc_type = acc_type
        self.lock = threading.Lock()

    # Deposit function for money deposit by the customers
    def deposit(self, amount, cus_passbook):
        with self.lock:
            self.acc_bal += round(amount, 2)  
            cus_passbook.update_bal(self.cus_id, self.acc_bal)  
            self.log_trans("The amount deposited: ", amount)
            return "Deposited amount is: {:.2f}\nNew balance is: {:.2f}".format(amount, self.acc_bal)

    # Withdraw function to withdraw amount from customer's account
    def withdraw(self, amount, cus_passbook):
        with self.lock:
            if self.acc_bal >= amount:  
                self.acc_bal -= round(amount, 2)  
                cus_passbook.update_bal(self.cus_id, self.acc_bal)  
                self.log_trans("Withdrawal", -amount)
                return "Amount withdrawn is: {:.2f}\nNew balance is: {:.2f}".format(round(amount, 2), self.acc_bal)
            else:
                return "Cannot withdraw insufficient funds. Please recheck the Balance"

    # Creating a function to calculate interest
    def apply_interest(self):
        with self.lock:
            if self.acc_type == 'Savings':
                interest = round(self.acc_bal * 0.05, 2)
                self.acc_bal -= interest  
                return interest  

    # Log the transaction to the transaction file
    def log_trans(self, transaction_type, amount):
        with open('transaction.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.cus_id, transaction_type, round(amount, 2), self.acc_bal])

    # Get the transaction history for the customer
    def trans_his(self):
        transactions = []
        with open('transaction.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 4 and row[0] == self.cus_id: 
                    transactions.append(row)
        return transactions


    # Function to show the interest of the savings account
    def show_interest(self):
        if self.acc_type == 'Savings':
            interest = round(self.acc_bal * 0.05, 2)
            self.acc_bal -= interest 
            return "Interest: {1:.2f},\nNew balance: {2:.2f}".format(interest, self.acc_bal)
        else:
            return "No savings account for interest application."
