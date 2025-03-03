from abc import ABC, abstractmethod
from datetime import datetime

class TransactionHistory:
    """Class untuk menyimpan riwayat transaksi"""
    def __init__(self):
        self.transactions = []

    def add_transaction(self, type, amount, balance):
        self.transactions.append({
            "type": type,
            "amount": amount,
            "balance": balance,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def get_transactions(self):
        return self.transactions


class BankAccount(ABC):
    """Abstract Base Class untuk akun bank"""
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self._balance = balance 
        self.history = TransactionHistory()

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.history.add_transaction("Deposit", amount, self._balance)
            print(f"Deposit sebesar {amount} berhasil! Saldo sekarang: {self._balance}")
        else:
            print("Jumlah deposit harus lebih dari 0!")

    @abstractmethod
    def withdraw(self, amount):
        """Metode abstrak untuk penarikan dana"""
        pass

    def get_balance(self):
        return self._balance

    def get_transaction_history(self):
        return self.history.get_transactions()


class SavingAccount(BankAccount):
    """Akun Tabungan"""
    def __init__(self, account_number, owner, balance=0, interest_rate=0.02):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if amount > self._balance:
            print("Saldo tidak mencukupi!")
        else:
            self._balance -= amount
            self.history.add_transaction("Withdraw", amount, self._balance)
            print(f"Penarikan {amount} berhasil! Saldo sekarang: {self._balance}")

    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        self.history.add_transaction("Interest", interest, self._balance)
        print(f"Bunga sebesar {interest} telah ditambahkan. Saldo sekarang: {self._balance}")


class CheckingAccount(BankAccount):
    """Akun Giro"""
    def __init__(self, account_number, owner, balance=0, overdraft_limit=500):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self._balance + self.overdraft_limit:
            print("Melebihi batas overdraft!")
        else:
            self._balance -= amount
            self.history.add_transaction("Withdraw", amount, self._balance)
            print(f"Penarikan {amount} berhasil! Saldo sekarang: {self._balance}")


saving_acc = SavingAccount("12345", "Alice", 1000)
checking_acc = CheckingAccount("67890", "Bob", 500)

saving_acc.deposit(500)
saving_acc.withdraw(300)
saving_acc.apply_interest()
print("Riwayat transaksi akun tabungan:", saving_acc.get_transaction_history())

checking_acc.deposit(1000)
checking_acc.withdraw(1800) 
print("Riwayat transaksi akun giro:", checking_acc.get_transaction_history())
