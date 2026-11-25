"""
class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
a = BankAccount("Sam")
b = BankAccount("Lina", 100)

print(a.owner, a.balance)    # Sam 0
print(b.owner, b.balance)    # Lina 100

a.balance = 50
print(a.balance, b.balance)  # 50 100
     """
"""
class Contact:
    def __init__(self,name):
        self.name=name
a=Contact(["firas","dede","dld"])

for i in a.name:
    print(i)
    """
"""
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

# Two dictionaries from your Contact Book
d1 = {"name": "Sam", "phone": "21612345678"}
d2 = {"name": "Lina", "phone": "21698765432"}

# Convert each dictionary into its own Contact object
c1 = Contact(d1["name"], d1["phone"])
c2 = Contact(d2["name"], d2["phone"])

print(c1.name, c1.phone)    
print(c2.name, c2.phone)   
""" 
