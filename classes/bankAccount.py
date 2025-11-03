class BankAccount:

    def __init__(self, account_holder:str, initial_balance:float):
        self.holder = account_holder
        self.balance = initial_balance

    def transfer_funds(self, other_account: BankAccount, amount: float):
        if amount <= self.balance:
            other_account.balance += amount
            self.balance -= amount
            print("confirm the transfer")
        else:
            print("no enough money")

    def __str__(self):
        return f"account holder's name: {self.holder}, the current balance {self.balance}."
    

