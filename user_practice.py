class User:
    def __init__(self, username):
        self.name =username
        self.balance = 0

    def make_deposit(self, amount):
        self.balance += amount

    def make_withdrawl(self, amount):
        self.balance -= amount
    
    def display_user_balance(self, balance):
        print(self.balance)

nate = User("nate")
big = User("big")
denny = User("denny")

nate.make_deposit(100)
nate.make_deposit(8)
nate.make_deposit(54)
nate.make_withdrawl(90)

big.make_deposit(98)
big.make_deposit(654)
big.make_withdrawl(84)
big.make_withdrawl(84)

denny.make_deposit(78455)
denny.make_withdrawl(542545)
denny.make_withdrawl(546266)
denny.make_withdrawl(5462545)

print(nate.name,"$", nate.balance)
print(big.balance)
print(denny.balance)