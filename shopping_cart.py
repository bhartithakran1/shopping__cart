# This project is for shopping cart
foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        try:
            price = float(input(f"Enter the price of {food}: $"))
            foods.append(food)
            prices.append(price)
        except ValueError:
            print("Invalid price! Please enter a numeric value.")

print("\n------ YOUR CART -------")
for i in range(len(foods)):
    print(f"{foods[i]}: ${prices[i]}")
    total += prices[i]

print(f"\nYour total is: ${total}")
print("----- THANK YOU -----")
