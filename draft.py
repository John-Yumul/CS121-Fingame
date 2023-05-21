# Function to handle the food tasks
def handle_food(energy, fun, health, net_worth, decision_counter):
    print("Food Options:")
    print("1. Home Cooking")
    print("2. Take Out")
    print("3. Fast Food")
    print("4. Fine Dining")

    food_choice = input("Enter your choice (1-4): ")
    print()

    options = {
        '1': {'energy_depletion': 10, 'fun_depletion': 5, 'health_depletion': 0, 'cost': 50, 'message': "You cooked a delicious meal at home."},
        '2': {'energy_depletion': 5, 'fun_depletion': 10, 'health_depletion': 0, 'cost': 100, 'message': "You ordered some tasty takeout food."},
        '3': {'energy_depletion': 3, 'fun_depletion': 15, 'health_depletion': 0, 'cost': 150, 'message': "You grabbed a quick meal at a fast food restaurant."},
        '4': {'energy_depletion': 15, 'fun_depletion': 20, 'health_depletion': 0, 'cost': 500, 'message': "You had a luxurious dining experience at a fancy restaurant."},
    }

    if food_choice in options:
        energy -= options[food_choice]['energy_depletion']
        fun -= options[food_choice]['fun_depletion']
        health -= options[food_choice]['health_depletion']
        net_worth -= options[food_choice]['cost']
        print(options[food_choice]['message'])
        print()
        decision_counter += 1
    else:
        print("Invalid choice!")

    return energy, fun, health, net_worth, decision_counter

# Function to handle the leisure tasks
def handle_leisure(energy, fun, health, net_worth, decision_counter):
    print("Leisure Options:")
    print("1. Watch a Movie")
    print("2. Play Video Games")
    print("3. Read a Book")
    print("4. Go Shopping")

    leisure_choice = input("Enter your choice (1-4): ")
    print()

    options = {
        '1': {'energy_depletion': 5, 'fun_depletion': 15, 'health_depletion': 0, 'cost': 200, 'message': "You enjoyed a great movie."},
        '2': {'energy_depletion': 10, 'fun_depletion': 10, 'health_depletion': 0, 'cost': 100, 'message': "You had a fun gaming session."},
        '3': {'energy_depletion': 5, 'fun_depletion': 5, 'health_depletion': 0, 'cost': 0, 'message': "You immersed yourself in an interesting book."},
        '4': {'energy_depletion': 5, 'fun_depletion': 20, 'health_depletion': 0, 'cost': 300, 'message': "You had a great time shopping for new items."},
    }

    if leisure_choice in options:
        energy -= options[leisure_choice]['energy_depletion']
        fun -= options[leisure_choice]['fun_depletion']
        health -= options[leisure_choice]['health_depletion']
        net_worth -= options[leisure_choice]['cost']
        print(options[leisure_choice]['message'])
        print()
        decision_counter += 1
    else:
        print("Invalid choice!")

    return energy, fun, health, net_worth, decision_counter

# Main program
MAX_DECISIONS = 5
energy = 100
fun = 100
health = 100
net_worth = 10000
decision_counter = 0
week_counter = 1

print("Welcome to FinGame!")
print("Current Status:")
print(f"Energy: {energy}%")
print(f"Fun: {fun}%")
print(f"Health: {health}%")
print(f"Net Worth: {net_worth} pesos")
print()

while energy > 0 and fun > 0:
    if decision_counter == MAX_DECISIONS:
        print(f"You have made all your decisions for Week {week_counter}. Your energy and fun are now restored to 100%.")
        energy = 100
        fun = 100
        decision_counter = 0
        week_counter += 1

        if week_counter % 4 == 1:
            net_worth += 10000
            print("Congratulations! You completed 4 weeks. Your net worth has increased by 10,000 pesos.")
            print(f"New Net Worth: {net_worth} pesos")
            print()

    print("Main Menu:")
    print("1. Food")
    print("2. Leisure")
    print("3. Quit")

    choice = input("Enter your choice (1-3): ")
    print()

    if choice == '1':
        energy, fun, health, net_worth, decision_counter = handle_food(energy, fun, health, net_worth, decision_counter)
    elif choice == '2':
        energy, fun, health, net_worth, decision_counter = handle_leisure(energy, fun, health, net_worth, decision_counter)
    elif choice == '3':
        print("Thank you for playing!")
        break
    else:
        print("Invalid choice!")

    print("Current Status:")
    print(f"Energy: {energy}%")
    print(f"Fun: {fun}%")
    print(f"Health: {health}%")
    print(f"Net Worth: {net_worth} pesos")
    print()

print("Game Over!")
if energy <= 0:
    print("Your energy has reached 0. You are exhausted.")
if fun <= 0:
    print("Your fun has reached 0. You are bored.")
