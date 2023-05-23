import shutil
import os

vertical = '\u2551'
horizontal = '\u2550'
top_left = '\u2554'
top_right = '\u2557'
bottom_left = '\u255a'
bottom_right = '\u255d'

title = "WELCOME TO THE FINGAME"

terminal_width = shutil.get_terminal_size().columns

spacing = (terminal_width - len(title)) //2
left_spacing = horizontal * spacing
right_spacing = horizontal * (terminal_width - len(title) - spacing)

print(f"{top_left}{horizontal * terminal_width}{top_right}")
print(f"{vertical}{left_spacing}{title}{right_spacing}{vertical}")
print(f"{bottom_left}{horizontal * terminal_width}{bottom_right}")


def create_frame(text):
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)
    border = '┌' +'─' * (max_length + 2)+ '┐'

    framed_text = [border]
    for line in lines:
        padding = ' ' * (max_length - len(line))
        framed_text.append(f'│ ' + line + padding + ' │')
    framed_text.append('└' + '─' * (max_length + 2) + '┘')

    return '\n'.join(framed_text)
a = """Here are the mechanics of the game.

The main condition of the game is for you to keep your well-being score as high as possible.
Well-being is about staying robust in various areas of your life.
You can't affect your well-being score directly. It's based on the scores of these following areas:

> FUN SCORE - this shows you how much fun you're having! You can raise your fun score by eating, doing leisurely
activities such as watching movies, going to parties, or reading a book. Your choice of exercise and transportation
can also affect your fun score.

> HEALTH SCORE - this is a measure of the condition of your physical health. Exercising and getting an ample amount 
of physical activity can increase your score in this area. If you don't do move around enough, or if you eat 
unhealthy food, this will go down.

> ENERGY SCORE - this goes down whenever you do something that requires a lot of hard work and effort, such 
as exercising. It is replenished every week, albeit you must not run out of energy or you will lose."""
framed_text = create_frame(a)
print(framed_text)

b = """Most things in the game don't come for free! Your balance tells you how much money you have. You must learn
how to manage it while also keeping your well-being stats in check. Every week, you must make FIVE choices for each 
of these things:

> FOOD - what you eat
> LEISURE - how you spend your free time
> EXERCISE - how you maintain your physical fitness
> TRANSPORTATION - how you get around"""
framed_text = create_frame(b)
print(framed_text)

c = """Once you've made all your choices for the week, you get 30 energy points. Once you've made five decisions 
each for the span of four weeks, you will get a monthly salary. On the other hand, payments for your utility bills
will also be deducted from your balance. If you run out of money, or your well-being drops too low, it's game over! 
You can quit the game at any time, and view your final stats, net worth, and score."""
framed_text = create_frame(c)
print(framed_text)

class Game:
    def __init__(self):
        # Initialize game attributes
        self.energy, self.fun, self.health = 100, 100, 100
        self.net_worth, self.decision_counter = 20000, 5
        self.week_counter, self.month_counter = 1, 1
        self.print_stats()

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def print_stats(self):
        # Print well-being stats and game information
        print(f"Week {self.week_counter}, Month {self.month_counter}\n")
        print("Well-Being Stats:")
        self.print_status_bar("Energy:", self.energy)
        self.print_status_bar("Fun:\t", self.fun)
        self.print_status_bar("Health:", self.health)
        print(f"\nNet Worth: ₱{self.net_worth}")
        print(f"Decisions: {self.decision_counter}\n")

    def print_status_bar(self, label, value):
        # Print a status bar for a given stat
        bar_length = 30
        filled_length = int(bar_length * value / 100)
        empty_length = bar_length - filled_length

        filled_bar = u"\u2584" * filled_length
        empty_bar = '-' * empty_length

        bar = filled_bar + empty_bar
        level = f'{value}%'

        print(f"{label} \t [{bar}] {level}")

    def print_invalid_choice(self):
        print("Invalid choice!\n")

    def calculate_score(self):
        return sum([self.energy, self.fun, self.health, self.net_worth])

    def handle_task(self, options):
        self.clear_screen()
        self.print_stats()

        for key, value in options.items():
            print(f"{key}. {value['name']}")

        user_choice = input(f"Enter your choice (1-{len(options)}): ")
        self.clear_screen()

        if user_choice in options:
            option = options[user_choice]
            self.energy = min(self.energy + option["energy_change"], 100)
            self.fun = min(self.fun + option["fun_change"], 100)
            self.health = min(self.health + option["health_change"], 100)
            self.net_worth -= option["cost"]
            self.print_stats()
            print("You chose", option["name"])
            print(option["message"], "\n")
            print(f"Energy: {option['energy_change']}", end=" ")
            print(f"Fun: {option['fun_change']}", end=" ")
            print(f"Health: {option['health_change']}")
            print(f"Cost: -₱{option['cost']}\n")
            self.decision_counter -= 1
        else:
            self.print_invalid_choice()

        if self.decision_counter == 0:
            self.energy = min(self.energy + 30, 100)
            self.fun = min(self.fun + 30, 100)
            self.health = min(self.health + 30, 100)
            self.decision_counter = 5
            print(f"It's now the end of Week {self.week_counter}.")
            print("You receive +30 to your Energy, Fun, and Health.\n")
            self.week_counter += 1

        if self.week_counter == 5:
            self.week_counter = 1
            self.month_counter += 1
            self.net_worth -= 4750  # Deduct house bills such as rent, water, electricity, and internet

            print("House bills deducted from your net worth:")
            print("- Rent: 2,000")
            print("- Water Bill: 500")
            print("- Electric Bill: 750")
            print("- Internet Bill: 1,500\n")

            self.net_worth += 20000 # Add monthly salary

            print("+ Monthly Salary: 20,000\n")
            print(f"It's now Month {self.month_counter}.")
            print("You receive +20,000 to your net worth.")

    def game_loop(self):
        while all([self.energy > 0, self.fun > 0, self.health > 0, self.net_worth > 0]):
            print("Options:")
            print("1. Food")
            print("2. Leisure")
            print("3. Exercise")
            print("4. Transportation")
            print("0. Quit")

            choice = input("Enter your choice (0-4): ")
            self.clear_screen()

            option_mapping = {
                "1": self.get_food_options,
                "2": self.get_leisure_options,
                "3": self.get_exercise_options,
                "4": self.get_transportation_options,
            }

            if choice == "0":
                break
            elif choice in option_mapping:
                self.handle_task(option_mapping[choice]())
            else:
                self.print_invalid_choice()

        self.clear_screen()

        print("Game Over!\n")
        print("Final Stats:")
        print(f"Energy: {self.energy}%")
        print(f"Fun: {self.fun}%")
        print(f"Health: {self.health}%")
        print(f"Net Worth: ₱{self.net_worth}")
        print(f"Decisions: {self.decision_counter}")
        print(f"Score: {self.calculate_score()}\n")

    @staticmethod
    def create_options(options):
        return {str(index + 1): option for index, option in enumerate(options)}

    def get_food_options(self):
        options = [
            {
                "name": "Eat a healthy meal",
                "energy_change": 10,
                "fun_change": -5,
                "health_change": 10,
                "cost": 50,
                "message": "ate a healthy meal.",
            },
            {
                "name": "Grab a quick snack",
                "energy_change": 5,
                "fun_change": 0,
                "health_change": -5,
                "cost": 10,
                "message": "grabbed a quick snack.",
            },
            {
                "name": "Skip a meal",
                "energy_change": -10,
                "fun_change": 0,
                "health_change": -5,
                "cost": 0,
                "message": "skipped a meal.",
            },
        ]
        return self.create_options(options)

    def get_leisure_options(self):
        options = [
            {
                "name": "Watch a movie",
                "energy_change": -10,
                "fun_change": 20,
                "health_change": 0,
                "cost": 50,
                "message": "watched a movie.",
            },
            {
                "name": "Go to a party",
                "energy_change": -20,
                "fun_change": 30,
                "health_change": -10,
                "cost": 100,
                "message": "went to a party.",
            },
            {
                "name": "Read a book",
                "energy_change": -5,
                "fun_change": 5,
                "health_change": 0,
                "cost": 20,
                "message": "read a book.",
            },
        ]
        return self.create_options(options)

    def get_exercise_options(self):
        options = [
            {
                "name": "Go for a run",
                "energy_change": -20,
                "fun_change": 10,
                "health_change": 20,
                "cost": 0,
                "message": "went for a run.",
            },
            {
                "name": "Do yoga",
                "energy_change": -10,
                "fun_change": 5,
                "health_change": 15,
                "cost": 0,
                "message": "did yoga.",
            },
            {
                "name": "Lift weights",
                "energy_change": -15,
                "fun_change": 5,
                "health_change": 25,
                "cost": 0,
                "message": "lifted weights.",
            },
        ]
        return self.create_options(options)

    def get_transportation_options(self):
        options = [
            {
                "name": "Take a taxi",
                "energy_change": -5,
                "fun_change": 10,
                "health_change": 0,
                "cost": 50,
                "message": "took a taxi.",
            },
            {
                "name": "Ride a bike",
                "energy_change": -15,
                "fun_change": 10,
                "health_change": 10,
                "cost": 0,
                "message": "rode a bike.",
            },
            {
                "name": "Walk",
                "energy_change": -10,
                "fun_change": 5,
                "health_change": 15,
                "cost": 0,
                "message": "walked.",
            },
        ]
        return self.create_options(options)

start = input(create_frame("Press Enter to start the game.") + "\n")
while True:
    if start == "":
        os.system("cls")
        game = Game()
        game.game_loop()
        break
    else:
        start = input(create_frame("Invalid input. Please press Enter to continue.") + "\n")

