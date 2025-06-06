# dictionary = A collection of {key:value} pairs ordered and changeable.
# Concession stand program

menu = {
    "hot_dog": 3.50,
    "hamburger": 4.00,
    "french_fries": 2.50,
    "soda": 1.50,
    "water": 1.00
}

cart = []
total = 0

print("Welcome to the Concession Stand!")
print("Here is the menu:")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

while True:
    food = input("Enter an item you will buy (q to quit):").lower()

    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("-- Your Order --")
for food in cart:
    total += menu.get(food)
    print(food, end = " ") 
print()
print(f"The total Cost is ${total}")
