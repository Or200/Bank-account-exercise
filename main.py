from classes.bankAccount import BankAccount

if __name__ == "__main__":
    account1 = BankAccount("Moshe", 1000)
    account2 = BankAccount("Yossi", 500)
    print(account1.__str__())
    print(account2.__str__())
    account2.transfer_funds(account1, 400)
    account2.transfer_funds(account1, 400)
    print(account1.__str__())
    print(account2.__str__())
