class BankAccount:
    interest_rate = 0.02

    def __init__(self, balance):
        self.balance = balance

    def calculate_interest(self):
        return self.balance * self.interest_rate
    
account1 = BankAccount(1000)
print(f"Interest earned: {account1.calculate_interest()}")