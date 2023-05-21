# Function to handle the exercise tasks
def handle_exercise(energy, fun, health, decision_counter):
    print("Exercise Options:")
    print("1. Go for a Run")
    print("2. Hit the Gym")
    print("3. Attend a Zumba Session")
    print("4. Do Home Workouts")

    exercise_choice = input("Enter your choice (1-4): ")
    print()

    options = {
        '1': {'energy_depletion': 20, 'fun_depletion': 10, 'health_increment': 5, 'message': "You went for a refreshing run."},
        '2': {'energy_depletion': 30, 'fun_depletion': 10, 'health_increment': 20, 'message': "You had an intense workout at the gym."},
        '3': {'energy_depletion': 20, 'fun_depletion': 5, 'health_increment': 20, 'message': "You attended an energizing Zumba session."},
        '4': {'energy_depletion': 10, 'fun_depletion': 5, 'health_increment': 10, 'message': "You did some effective home workouts."},
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

    return energy, fun, health, decision_counter


# Function to handle the transportation tasks
def handle_transportation(energy, fun, health, net_worth, decision_counter):
    print("Transportation Options:")
    print("1. Walk")
    print("2. Bike")
    print("3. Public Transportation")
    print("4. Taxi")

    transportation_choice = input("Enter your choice (1-4): ")
    print()

    options = {
        '1': {'energy_depletion': 5, 'fun_depletion': 5, 'health_depletion': 0, 'cost': 0, 'message': "You chose to walk."},
        '2': {'energy_depletion': 5, 'fun_depletion': 5, 'health_depletion': 0, 'cost': 0, 'message': "You decided to bike."},
        '3': {'energy_depletion': 5, 'fun_depletion': 5, 'health_depletion': 0, 'cost': 50, 'message': "You took public transportation."},
        '4': {'energy_depletion': 10, 'fun_depletion': 5, 'health_depletion': 0, 'cost': 100, 'message': "You traveled by taxi."},
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


# Main program
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
        energy, fun, health, decision_counter = handle_exercise(energy, fun, health, decision_counter)
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
