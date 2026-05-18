print("Welcome to our store")
print("Please provide your Information")

name = input("Enter your name: ")
while name == "":
    name = input("Enter your name: ")

age = int(input("Enter your age: "))

print(f"{name}, what would you like to buy?")

items = ["Fender", "Gibson", "PRS", "Majesty"]
prices = [2000, 3000, 4000, 4000]

# Show items with index numbers
for i in range(len(items)):
    print(f"{i}. {items[i]}")

cus_item = int(input("ENTER THE NUMBER INDEX YOU WANT TO BUY: "))

# Validate index
if cus_item < 0 or cus_item >= len(items):
    print("Invalid item index")
else:
    print(f"You selected {items[cus_item]} : {prices[cus_item]}$")




