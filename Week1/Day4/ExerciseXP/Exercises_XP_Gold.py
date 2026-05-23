import sys

# PART I : BankAccount

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise Exception("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive.")
        self.balance -= amount


# PART II : MinimumBalanceAccount

class MinimumBalanceAccount(BankAccount):

    def __init__(self, balance, minimum_balance=0):
        super().__init__(balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive.")
        if self.balance - amount < self.minimum_balance:
            raise Exception(f"Cannot go below minimum balance of ${self.minimum_balance}.")
        self.balance -= amount


# PART III : Expand BankAccount
class BankAccount:

    def __init__(self, balance, username, password):
        self.balance       = balance
        self.username      = username
        self.password      = password
        self.authenticated = False

    def authenticate(self, username, password):
        if username == self.username and password == self.password:
            self.authenticated = True

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("Not authenticated.")
        if amount <= 0:
            raise Exception("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Not authenticated.")
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive.")
        self.balance -= amount


class MinimumBalanceAccount(BankAccount):

    def __init__(self, balance, username, password, minimum_balance=0):
        super().__init__(balance, username, password)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Not authenticated.")
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive.")
        if self.balance - amount < self.minimum_balance:
            raise Exception(f"Cannot go below minimum balance of ${self.minimum_balance}.")
        self.balance -= amount


# PART IV : ATM

class ATM:

    def __init__(self, account_list, try_limit):
        if not all(isinstance(a, BankAccount) for a in account_list):
            raise Exception("account_list must only contain BankAccount instances.")
        try:
            if try_limit <= 0:
                raise Exception("try_limit must be positive.")
            self.try_limit = try_limit
        except Exception:
            self.try_limit = 2

        self.account_list  = account_list
        self.current_tries = 0
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            choice = input("\n[1] Log in  [2] Exit\nSelect: ").strip()
            if choice == "1":
                self.log_in(input("Username: "), input("Password: "))
            elif choice == "2":
                sys.exit(0)

    def log_in(self, username, password):
        for account in self.account_list:
            if account.username == username and account.password == password:
                account.authenticate(username, password)
                self.current_tries = 0
                self.show_account_menu(account)
                return

        self.current_tries += 1
        if self.current_tries >= self.try_limit:
            print("Max attempts reached. Shutting down.")
            sys.exit(1)
        print(f"{self.try_limit - self.current_tries} attempt(s) left.")

    def show_account_menu(self, account):
        while True:
            choice = input(f"\n{account.username} | ${account.balance}\n[1] Deposit  [2] Withdraw  [3] Exit\nSelect: ").strip()
            if choice == "3":
                account.authenticated = False
                break
            try:
                amount = float(input("Amount: $"))
                account.deposit(amount) if choice == "1" else account.withdraw(amount)
                print(f"New balance: ${account.balance}")
            except Exception as e:
                print(e)


# TESTS

acc1 = BankAccount(500, "christian", "pass123")
acc2 = MinimumBalanceAccount(300, "sara", "abc", minimum_balance=100)

atm = ATM([acc1, acc2], try_limit=3)