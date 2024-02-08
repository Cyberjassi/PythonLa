account = {
    'checking':1897.00,
    'savings':3456.09

}
def add_balance(amount,name):
    account[name] +=amount
    return account[name]

transactions = [
    (-1244.65,'checking'),
    (7654.65,'checking'),
    (-9876.09,'savings'),
    (1244.65,'checking'),
    (-0987.87,'checking'),
    (244.65,'savings'),
    (-144.65,'checking'),
    (-14.65,'savings'),
]
for i in transactions:
    add_balance(*i)

print(account)

# packing
def pack(*t):
    print(t)

pack(1,2,3)


def dic(**t):
    print(t)

dic(a=1,b=2,c=3)