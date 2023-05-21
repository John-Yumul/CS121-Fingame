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
        '1': {'energy_depletion': 10, 'fun_depletion': 5, 'health_depletion': 5, 'cost': 100, 'message': "You cooked a delicious meal at home."},
        '2': {'energy_depletion': 10, 'fun_depletion': 5, 'health_depletion': 10, 'cost': 150, 'message': "You ordered take out."},
        '3': {'energy_depletion': 15, 'fun_depletion': 10, 'health_depletion': 20, 'cost': 200, 'message': "You grabbed some fast food."},
        '4': {'energy_depletion': 20, 'fun_depletion': 15, 'health_depletion': 30, 'cost': 500, 'message': "You indulged in a fine dining experience."},
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
    print("2. Read a Book")
    print("3. Play Video Games")
    print("4. Go to a Theme Park")

    leisure_choice = input("Enter your choice (1-4): ")
    print()

    options = {
        '1': {'energy_depletion': 10, 'fun_depletion': 20, 'health_depletion': 5, 'cost': 200, 'message': "You enjoyed watching a movie."},
        '2': {'energy_depletion': 5, 'fun_depletion': 15, 'health_depletion': 5, 'cost': 50, 'message': "You spent time reading a book."},
        '3': {'energy_depletion': 15, 'fun_depletion': 30, 'health_depletion': 5, 'cost': 300, 'message': "You played video games."},
        '4': {'energy_depletion': 20, 'fun_depletion': 40, 'health_depletion': 10, 'cost': 500, 'message': "You had a blast at a theme park."},
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


# Function to handle the exercise tasks
def handle_exercise(energy, fun, health, net_worth, decision_counter):
    print("Exercise Options:")
    print("1. Jogging")
    print("2. Gym Workout")
    print("3. Yoga")
    print("4. Cycling")

    exercise_choice = input("Enter your choice (1-4): ")
    print()

    options = {
        '1': {'energy_depletion': 15, 'fun_depletion': 5, 'health_depletion': 10, 'cost': 0, 'message': "You went for a jogging session."},
        '2': {'energy_depletion': 20, 'fun_depletion': 10, 'health_depletion': 15, 'cost': 500, 'message': "You had a rigorous workout at the gym."},
        '3': {'energy_depletion': 10, 'fun_depletion': 5, 'health_depletion': 5, 'cost': 200, 'message': "You practiced yoga for relaxation."},
        '4': {'energy_depletion': 15, 'fun_depletion': 5, 'health_depletion': 10, 'cost': 100, 'message': "You went cycling and enjoyed the fresh air."},
    }

    if exercise_choice in options:
        energy -= options[exercise_choice]['energy_depletion']
        fun -= options[exercise_choice]['fun_depletion']
        health -= options[exercise_choice]['health_depletion']
        net_worth -= options[exercise_choice]['cost']
        print(options[exercise_choice]['message'])
        print()
        decision_counter += 1
    else:
        print("Invalid choice!")

    return energy, fun, health, net_worth, decision_counter


# Function to handle the transportation tasks
def handle_transportation(energy, fun, health, net_worth, decision_counter):
    print("Transportation Options:")
    print("1. Walk")
    print("2. Public Transport")
    print("3. Bicycle")
    print("4. Car")

    transportation_choice = input("Enter your choice (1-4): ")
    print()

    options = {
        '1': {'energy_depletion': 5, 'fun_depletion': 10, 'health_depletion': 5, 'cost': 0, 'message': "You walked to your destination."},
        '2': {'energy_depletion': 10, 'fun_depletion': 5, 'health_depletion': 5, 'cost': 50, 'message': "You used public transport."},
        '3': {'energy_depletion': 5, 'fun_depletion': 10, 'health_depletion': 5, 'cost': 200, 'message': "You rode a bicycle."},
        '4': {'energy_depletion': 15, 'fun_depletion': 5, 'health_depletion': 5, 'cost': 500, 'message': "You drove a car."},
    }

    if transportation_choice in options:
        energy -= options[transportation_choice]['energy_depletion']
        fun -= options[transportation_choice]['fun_depletion']
        health -= options[transportation_choice]['health_depletion']
        net_worth -= options[transportation_choice]['cost']
        print(options[transportation_choice]['message'])
        print()
        decision_counter += 1
    else:
        print("Invalid choice!")

    return energy, fun, health, net_worth, decision_counter


# Rest of the program

MAX_DECISIONS = 5
energy = 100
fun = 100
health = 100
net_worth = 10000
decision_counter = 0
week_counter = 1

print("Welcome to the RPG Game!")
print("Current Status:")
print(f"Energy: {energy}%")
print(f"Fun: {fun}%")
print(f"Health: {health}%")
print(f"Net Worth: {net_worth} pesos")
print()

while energy > 0 and fun > 0 and health > 0 and net_worth > 0:
    if decision_counter == MAX_DECISIONS:
        print(f"You have made all your decisions for Week {week_counter}. Your energy, fun, health, and net worth are now restored to 100%.")
        energy = 100
        fun = 100
        health = 100
        net_worth += 10000
        decision_counter = 0
        week_counter += 1

    if week_counter % 4 == 1 and week_counter > 1:
        net_worth += 10000
        print("Congratulations! You completed 4 weeks. Your net worth has increased by 10,000 pesos.")
        print(f"New Net Worth: {net_worth} pesos")
        print()

    print("Main Menu:")
    print("1. Food")
    print("2. Leisure")
    print("3. Exercise")
    print("4. Transportation")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")
    print()

    if choice == '1':
        energy, fun, health, net_worth, decision_counter = handle_food(energy, fun, health, net_worth, decision_counter)
    elif choice == '2':
        energy, fun, health, net_worth, decision_counter = handle_leisure(energy, fun, health, net_worth, decision_counter)
    elif choice == '3':
        energy, fun, health, net_worth, decision_counter = handle_exercise(energy, fun, health, net_worth, decision_counter)
    elif choice == '4':
        energy, fun, health, net_worth, decision_counter = handle_transportation(energy, fun, health, net_worth, decision_counter)
    elif choice == '5':
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
if health <= 0:
    print("Your health has reached 0. You are unwell.")
if net_worth <= 0:
    print("Your net worth has reached 0. You are broke.")
