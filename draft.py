import os
import random

def stats_threshold(energy, fun, health):
    energy = min(energy, 100)
    fun = min(fun, 100)
    health = min(health, 100)

# Function to handle the food tasks
def handle_food(energy, fun, health, net_worth, decision_counter):
    os.system("cls")  # Clear screen

    print("Food Options:")
    print("1. Home Cooking")
    print("2. Take Out")
    print("3. Fast Food")
    print("4. Fine Dining")

    food_choice = input("Enter your choice (1-4): ")
    print()

    options = {
        '1': {'energy_depletion': 10, 'fun_depletion': 10, 'health_depletion': 5, 'cost': 100, 'message': "You cooked a delicious meal at home."},
        '2': {'energy_depletion': 5, 'fun_depletion': 10, 'health_depletion': 10, 'cost': 200, 'message': "You ordered take-out from a nearby karinderya."},
        '3': {'energy_depletion': 5, 'fun_depletion': 5, 'health_depletion': 10, 'cost': 350, 'message': "You had a quick meal at a fast food restaurant."},
        '4': {'energy_depletion': 10, 'fun_depletion': 0, 'health_depletion': 5, 'cost': 1000, 'message': "You enjoyed a luxurious fine dining experience."},
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

    stats_threshold(energy, fun, health)

    return energy, fun, health, net_worth, decision_counter


# Function to handle the leisure tasks
def handle_leisure(energy, fun, health, net_worth, decision_counter):
    os.system("cls")  # Clear screen

    print("Leisure Options:")
    print("1. Read a Book")
    print("2. Play Video Games")
    print("3. Chill in a Coffee Shop")
    print("4. Watch a Movie in a Cinema")
    print("5. Go for Shopping")
    print("6. Attend a Concert")

    leisure_choice = input("Enter your choice (1-6): ")
    print()

    options = {
        '1': {'energy_depletion': 5, 'fun_depletion': 20, 'health_depletion': 0, 'cost': 0, 'message': "You immersed yourself in a captivating book."},
        '2': {'energy_depletion': 10, 'fun_depletion': 15, 'health_depletion': 5, 'cost': 50, 'message': "You played video games and had a blast."},
        '3': {'energy_depletion': 10, 'fun_depletion': 10, 'health_depletion': 5, 'cost': 200, 'message': "You sipped your favorite beverage in a cafe."},
        '4': {'energy_depletion': 15, 'fun_depletion': 5, 'health_depletion': 10, 'cost': 500, 'message': "You watched a movie and had a great time."},
        '5': {'energy_depletion': 20, 'fun_depletion': 5, 'health_depletion': 5, 'cost': 1000, 'message': "You spent money on the things you love."},
        '6': {'energy_depletion': 40, 'fun_depletion': 0, 'health_depletion': 15, 'cost': 5000, 'message': "You enjoyed a musical concert."},
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

    stats_threshold(energy, fun, health)

    return energy, fun, health, net_worth, decision_counter


# Function to handle the exercise tasks
def handle_exercise(energy, fun, health, net_worth, decision_counter):
    os.system("cls")  # Clear screen

    print("Exercise Options:")
    print("1. Walking")
    print("2. Running")
    print("3. Home Workout")
    print("4. Gym")

    exercise_choice = input("Enter your choice (1-4): ")
    print()

    options = {
        '1': {'energy_depletion': 5, 'fun_depletion': 15, 'health_increment': 10, 'cost': 0, 'message': "You went for a refreshing walk."},
        '2': {'energy_depletion': 10, 'fun_depletion': 10, 'health_increment': 15, 'cost': 0, 'message': "You enjoyed a good run."},
        '3': {'energy_depletion': 20, 'fun_depletion': 5, 'health_increment': 20, 'cost': 0, 'message': "You had a great time improving your fitness at home."},
        '4': {'energy_depletion': 30, 'fun_depletion': 5, 'health_increment': 15, 'cost': 500, 'message': "You hit the gym to build those muscles."},
    }

    if exercise_choice in options:
        energy -= options[exercise_choice]['energy_depletion']
        fun -= options[exercise_choice]['fun_depletion']
        health += options[exercise_choice]['health_increment']
        print(options[exercise_choice]['message'])
        print()
        decision_counter += 1
    else:
        print("Invalid choice!")

    stats_threshold(energy, fun, health)

    return energy, fun, health, net_worth, decision_counter


# Function to handle the transportation tasks
def handle_transportation(energy, fun, health, net_worth, decision_counter):
    os.system("cls")  # Clear screen

    print("Transportation Options:")
    print("1. Walk")
    print("2. Bicycle")
    print("3. Jeepney")
    print("4. Car")

    transportation_choice = input("Enter your choice (1-4): ")
    print()

    options = {
        '1': {'energy_depletion': 15, 'fun_depletion': 5, 'health_depletion': 0, 'cost': 0, 'message': "You walked to your destination."},
        '2': {'energy_depletion': 10, 'fun_depletion': 5, 'health_depletion': 0, 'cost': 0, 'message': "You rode a bicycle to your destination."},
        '3': {'energy_depletion': 5, 'fun_depletion': 10, 'health_depletion': 5, 'cost': 50, 'message': "You used a jeepney to reach your destination."},
        '4': {'energy_depletion': 0, 'fun_depletion': 5, 'health_depletion': 0, 'cost': 100, 'message': "You drove a car to your destination."},
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

    stats_threshold(energy, fun, health)

    return energy, fun, health, net_worth, decision_counter


# Main game loop
def game_loop():
    energy = 100
    fun = 100
    health = 100
    net_worth = 10000
    decision_counter = 0

    while energy > 0 and fun > 0 and health > 0 and net_worth > 0:
        os.system("cls")  # Clear screen

        print("Well-Being Stats:")
        print("Energy:", energy)
        print("Fun:", fun)
        print("Health:", health)
        print("")
        print("Net Worth:", net_worth)
        print("Decisions:", decision_counter)
        print()

        print("Options:")
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
            break
        else:
            print("Invalid choice!")

    os.system("cls")  # Clear screen

    print("Game Over!")
    print("Final Stats:")
    print("Energy:", energy)
    print("Fun:", fun)
    print("Health:", health)
    print("")
    print("Net Worth:", net_worth)
    print("Decisions:", decision_counter)
    print()

    score = energy + fun + health + net_worth - decision_counter * 100
    print("Score:", score)


# Start the game
os.system("cls") 
print("INSERT INTRO NINA BEA AT VINCE")
print()
input("Press Enter to start the game...")
game_loop()