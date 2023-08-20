amount = 50

while amount > 0:
    print("Amount Due:", amount)
    coins = input("Insert coin: ")
    if coins in ["5", "10", "25"]:
        amount -= int(coins)

print("Change Owed:", amount.__abs__())