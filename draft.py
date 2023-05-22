import os

class Game:
    def __init__(self):
        self.energy = 100
        self.fun = 100
        self.health = 100
        self.net_worth = 20000
        self.decision_counter = 0

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def print_stats(self):
        print("Well-Being Stats:")
        print("Energy:", self.energy)
        print("Fun:", self.fun)
        print("Health:", self.health)
        print("")
        print("Net Worth:", self.net_worth)
        print("Decisions:", self.decision_counter)
        print()

    def print_invalid_choice(self):
        print("Invalid choice!")
        print()

    def calculate_score(self):
        return self.energy + self.fun + self.health + self.net_worth - self.decision_counter * 100

    def handle_task(self, options):
        self.clear_screen()
        self.print_stats()

        for key, value in options.items():
            print(f"{key}. {value['name']}")

        user_choice = input(f"Enter your choice (1-{len(options)}): ")
        self.clear_screen()

        if user_choice in options:
            option = options[user_choice]
            self.energy = min(self.energy + option['energy_change'], 100)
            self.fun = min(self.fun + option['fun_change'], 100)
            self.health = min(self.health + option['health_change'], 100)
            self.net_worth -= option['cost']
            print(option['message'])
            print()
            self.decision_counter += 1
        else:
            self.print_invalid_choice()

        if self.decision_counter % 5 == 0:
            self.energy = min(self.energy + 30, 100)
            self.fun = min(self.fun + 30, 100)
            self.health = min(self.health + 30, 100)

        if self.decision_counter % 20 == 0 and self.decision_counter > 0:
            self.net_worth -= 4750  # Deduct house bills such as rent, water, electricity, and internet

            print("House bills deducted from your net worth:")
            print("- Rent: 2000")
            print("- Water Bill: 500")
            print("- Electric Bill: 750")
            print("- Internet Bill: 1500")
            print()

    def game_loop(self):
        while self.energy > 0 and self.fun > 0 and self.health > 0 and self.net_worth > 0:
            self.print_stats()

            print("Options:")
            print("1. Food")
            print("2. Leisure")
            print("3. Exercise")
            print("4. Transportation")
            print("5. Quit")

            choice = input("Enter your choice (1-5): ")
            self.clear_screen()

            if choice == '1':
                self.handle_task(self.get_food_options())
            elif choice == '2':
                self.handle_task(self.get_leisure_options())
            elif choice == '3':
                self.handle_task(self.get_exercise_options())
            elif choice == '4':
                self.handle_task(self.get_transportation_options())
            elif choice == '5':
                break
            else:
                self.print_invalid_choice()

        self.clear_screen()
        self.print_stats()

        print("Game Over!")
        print("Final Stats:")
        print("Energy:", self.energy)
        print("Fun:", self.fun)
        print("Health:", self.health)
        print("Net Worth:", self.net_worth)
        print("Decisions:", self.decision_counter)
        print("Score:", self.calculate_score())

    def get_food_options(self):
        options = {
            '1': {
                'name': 'Eat a healthy meal',
                'energy_change': 10,
                'fun_change': -5,
                'health_change': 10,
                'cost': 50,
                'message': 'You ate a healthy meal. Energy +10, Fun -5, Health +10.'
            },
            '2': {
                'name': 'Grab a quick snack',
                'energy_change': 5,
                'fun_change': 0,
                'health_change': -5,
                'cost': 10,
                'message': 'You grabbed a quick snack. Energy +5, Fun +0, Health -5.'
            },
            '3': {
                'name': 'Skip a meal',
                'energy_change': -10,
                'fun_change': 0,
                'health_change': -5,
                'cost': 0,
                'message': 'You skipped a meal. Energy -10, Fun +0, Health -5.'
            }
        }
        return options

    def get_leisure_options(self):
        options = {
            '1': {
                'name': 'Watch a movie',
                'energy_change': -10,
                'fun_change': 20,
                'health_change': 0,
                'cost': 50,
                'message': 'You watched a movie. Energy -10, Fun +20, Health +0.'
            },
            '2': {
                'name': 'Go to a party',
                'energy_change': -20,
                'fun_change': 30,
                'health_change': -10,
                'cost': 100,
                'message': 'You went to a party. Energy -20, Fun +30, Health -10.'
            },
            '3': {
                'name': 'Read a book',
                'energy_change': -5,
                'fun_change': 5,
                'health_change': 0,
                'cost': 20,
                'message': 'You read a book. Energy -5, Fun +5, Health +0.'
            }
        }
        return options

    def get_exercise_options(self):
        options = {
            '1': {
                'name': 'Go for a run',
                'energy_change': -20,
                'fun_change': 10,
                'health_change': 20,
                'cost': 0,
                'message': 'You went for a run. Energy -20, Fun +10, Health +20.'
            },
            '2': {
                'name': 'Do yoga',
                'energy_change': -10,
                'fun_change': 5,
                'health_change': 15,
                'cost': 0,
                'message': 'You did yoga. Energy -10, Fun +5, Health +15.'
            },
            '3': {
                'name': 'Lift weights',
                'energy_change': -15,
                'fun_change': 5,
                'health_change': 25,
                'cost': 0,
                'message': 'You lifted weights. Energy -15, Fun +5, Health +25.'
            }
        }
        return options

    def get_transportation_options(self):
        options = {
            '1': {
                'name': 'Take the bus',
                'energy_change': -5,
                'fun_change': 0,
                'health_change': 0,
                'cost': 5,
                'message': 'You took the bus. Energy -5, Fun +0, Health +0.'
            },
            '2': {
                'name': 'Ride a bike',
                'energy_change': -10,
                'fun_change': 5,
                'health_change': 10,
                'cost': 0,
                'message': 'You rode a bike. Energy -10, Fun +5, Health +10.'
            },
            '3': {
                'name': 'Drive a car',
                'energy_change': -15,
                'fun_change': 10,
                'health_change': 5,
                'cost': 20,
                'message': 'You drove a car. Energy -15, Fun +10, Health +5.'
            }
        }
        return options


# Create and start the game
game = Game()
game.game_loop()
