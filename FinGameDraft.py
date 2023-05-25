import shutil
import os
import pygame
import time
import random
from pygame import mixer

os.system("cls")

pygame.mixer.init()
start_sound = pygame.mixer.Sound(r'.\SFX\Start.mp3')
common_sound = pygame.mixer.Sound(r'.\SFX\Common_SFX.mp3')
game_over_sound = pygame.mixer.Sound(r'.\SFX\Game_Over.mp3')
week_sound = pygame.mixer.Sound(r'.\SFX\Week.mp3')
month_sound = pygame.mixer.Sound(r'.\SFX\Month.mp3')
invalid_sound = pygame.mixer.Sound(r'.\SFX\Invalid.mp3')

pygame.init()
mixer.music.load(r'.\BG\BG.mp3')
mixer.music.play(-1)
with open('.\FingameTitle.txt', "r", encoding="utf8") as f:
    for line in f:
        print(line.rstrip())
    input("Press Enter to read the mechanics.")
    pass
os.system("cls")

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
class Mechanics:
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

    a = """Here are the mechanics of the game.

    The main condition of the game is for you to keep your well-being score as high as possible.
    Well-being is about staying robust in various areas of your life.
    You can't affect your well-being score directly. It's based on the scores of these following areas:

    > FUN SCORE - this shows you how much fun you're having! You can raise your fun score by eating, doing leisurely
    activities such as watching movies, going to parties, or reading a book. Your choice of exercise and transportation
    can also affect your fun score.

    > HEALTH SCORE - this is a measure of the condition of your physical health. Exercising and getting an ample amount 
    of physical activity can increase your score in this area. If you don't do move around enough, or if you eat 
    unhealthy food and skip meals, this will either remain stagnant or decrease.

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
    > TRANSPORTATION - how you get around
    > INVESTMENT - how you can put your spare money to work and build wealth"""
    framed_text = create_frame(b)
    print(framed_text)

    c = """Once you've made all your choices for the week, you get 30 points each for your Energy, Fun, and Health score. Once 
    you've made five decisions each for the span of four weeks, you will get a monthly salary. At the same time, your 
    utility bills will also be deducted from your balance. If you run out of money, or any of your stats drop too low, 
    it's game over! You can quit the game at any time and view your final stats, net worth, and score"""
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
        if value <= 30:
            print(f"\t\t Running Low.")
            invalid_sound.play()

    def print_invalid_choice(self):
        invalid_sound.play()
        print("Invalid choice!\n")
        self.print_stats()

    def calculate_score(self):
        return max(0, sum([self.energy, self.fun, self.health, self.net_worth]))

    def handle_task(self, options):
        self.clear_screen()
        self.print_stats()

        for key, value in options.items():
            print(f"{key}. {value['name']} (-₱{value['cost']})")

        print()
        user_choice = input(f"Enter your choice (1-{len(options)}): ")
        self.clear_screen()

        if user_choice in options:
            common_sound.play()
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
            if option['invested'] == True:
                growth = round(random.uniform(option["lower_range"], option["upper_range"]), 2)
                print(f"Your investment has grown by ", (growth-1)*100, "%")
                self.net_worth += (option["cost"]*growth)
                print('Your net worth is now', self.net_worth)

            self.decision_counter -= 1
        else:
            self.print_invalid_choice()

        if self.decision_counter == 0:
            self.energy = min(self.energy + 30, 100)
            self.fun = min(self.fun + 30, 100)
            self.health = min(self.health + 30, 100)
            self.decision_counter = 5
            week_sound.play()
            print(f"It's now the end of Week {self.week_counter}.")
            print("You receive +30 to your Energy, Fun, and Health.\n")
            self.week_counter += 1

        if self.week_counter == 5:
            self.week_counter = 1
            self.month_counter += 1
            self.net_worth -= 8000  # Deduct house bills such as rent, water, electricity, and internet
            month_sound.play()
            print(f"It's now the end of Month {self.month_counter-1}.")
            print("Utility bills deducted from your net worth:")
            print("Rent: \t\t-₱4,000")
            print("Water Bill: \t-₱700")
            print("Electric Bill: \t-₱1500")
            print("Internet Bill: \t-₱1,800\n")
            self.net_worth += 20000 # Add monthly salary
            print("Monthly Salary: +₱20,000\n")
            input(create_frame(f"Press Enter to Jump into Month {self.month_counter}") + "\n")
            start_sound.play()

    def game_loop(self):
        while all([self.energy > 0, self.fun > 0, self.health > 0, self.net_worth > 0]):
            print("Options:")
            print("1. Food")
            print("2. Leisure")
            print("3. Exercise")
            print("4. Transportation")
            print("5. Investment")
            print("0. Quit\n")

            choice = input("Enter your choice (0-5): ")
            self.clear_screen()
    
            option_mapping = {
                "1": self.get_food_options,
                "2": self.get_leisure_options,
                "3": self.get_exercise_options,
                "4": self.get_transportation_options,
                "5": self.get_investment_options,
            }

            if choice == "0":
                break
            elif choice in option_mapping:
                common_sound.play()
                self.handle_task(option_mapping[choice]())
            else:
                self.print_invalid_choice()

        self.clear_screen()

        mixer.music.stop()
        game_over_sound.play()
        print("Game Over!\n")
        print("Final Stats:")
        print(f"Energy: {self.energy}%")
        print(f"Fun: {self.fun}%")
        print(f"Health: {self.health}%")
        print(f"Net Worth: ₱{self.net_worth}")
        print(f"Score: {self.calculate_score()}")
        time.sleep(3)

    @staticmethod
    def create_options(options):
        return {str(index + 1): option for index, option in enumerate(options)}

    def get_food_options(self):
        options = [
            {   "name": "Home Cooking",
                "energy_change": 15,    "fun_change": -10,      "health_change": 10,
                "cost": 200,            "message": "Ah, that home-cooked meal was so good.", "invested": False,
            },
            {   "name": "Take-Out",
                "energy_change": 15,    "fun_change": -5,        "health_change": -10,
                "cost": 500,            "message": "Just had a take-out from a nearest food shop.", "invested": False,
            },
            {   "name": "Foodpanda/GrabFood",
                "energy_change": 15,    "fun_change": 10,       "health_change": -15,
                "cost": 700,            "message": "The rider is on his way to my doorstep.", "invested": False,
            },
            {   "name": "Fast Food Dine-In",
                "energy_change": 15,    "fun_change": 15,       "health_change": -20,
                "cost": 900,            "message": "Just had my favorites chicken and fries.", "invested": False,
            },
            {   "name": "Coffee Shop",
                "energy_change": 5,     "fun_change": 20,       "health_change": 5,
                "cost": 300,            "message": "Just had a sipped with my favorite latte.", "invested": False,
            },
            {   "name": "Quick Snack",  
                "energy_change": 5,     "fun_change": 0,        "health_change": -5,
                "cost": 100,            "message": "Just grabbed a bite on my sandwich.", "invested": False,
            },
            {   "name": "Fine Dining",
                "energy_change": 15,    "fun_change": 30,       "health_change": 15,
                "cost": 1200,           "message": "Went to the fanciest dining place I have ever been.", "invested": False,
            },
            {   "name": "Skip a meal",
                "energy_change": -30,   "fun_change": -15,      "health_change": -30,
                "cost": 0,              "message": "Didn't have the appetite to eat.", "invested": False,
            },
        ]
        return self.create_options(options)

    def get_leisure_options(self):
        options = [
            {   "name": "Watch a Movie",
                "energy_change": -20,   "fun_change": 20,   "health_change": 0,
                "cost": 700,            "message": "Just watched my favorite Disney film.", "invested": False,
            },
            {   "name": "Go to a Pool Party",
                "energy_change": -20,   "fun_change": 30,   "health_change": -10,
                "cost": 1000,           "message": "Had the best night on the pool.", "invested": False,
            },
            {   "name": "Read a Book",  
                "energy_change": -5,    "fun_change": 5,    "health_change": 0,
                "cost": 0,              "message": "Had fun reading Stephanie Mayer's Twilight books.", "invested": False,
            },
            {   "name": "Concert",  
                "energy_change": -40,    "fun_change": 50,  "health_change": -20,
                "cost": 7000,            "message": "I will never forget my Taylor Swift  | The Eras Tour experience.", "invested": False,
            },
            {   "name": "Casino",  
                "energy_change": -20,    "fun_change": 20,  "health_change": -5,
                "cost": 3000,            "message": "Lost a few turns but gave my best bets.", "invested": False,
            },
        ]
        return self.create_options(options)

    def get_exercise_options(self):
        options = [
            {   "name": "Run",
                "energy_change": -20,   "fun_change": 0,   "health_change": 5,
                "cost": 0,              "message": "Had a few laps around the block.", "invested": False,
            },
            {   "name": "Yoga",
                "energy_change": -10,   "fun_change": 5,   "health_change": 10,
                "cost": 100,            "message": "Felt focused more than ever.", "invested": False,
            },
            {   "name": "Home Workout",
                "energy_change": -30,   "fun_change": -10,  "health_change": 20,
                "cost": 500,            "message": "Just had a workout at my own space.", "invested": False,
            },
            {   "name": "Gym",
                "energy_change": -40,   "fun_change": 10,  "health_change": 30,
                "cost": 1500,           "message": "I'm ready to get the muscles bigger.", "invested": False,
            },
        ]
        return self.create_options(options)

    def get_transportation_options(self):
        options = [
            {   "name": "Walk",
                "energy_change": -30,   "fun_change": -20,  "health_change": 5,
                "cost": 0,              "message": "Had a tiring walk from home to work.", "invested": False,
            },
            {   "name": "Bike",
                "energy_change": -20,   "fun_change": 5,    "health_change": 10,
                "cost": 0,              "message": "Almost got my pedals broken, but I arrived at my place.", "invested": False,
            },
            {   "name": "Public Transportation",
                "energy_change": -10,   "fun_change": -10,  "health_change": -5,
                "cost": 300,            "message": "Just rode a Jeepney to Trinoma.", "invested": False,
            },
            {   "name": "Grab/Angkas",
                "energy_change": 0,     "fun_change": 10,   "health_change": 0,
                "cost": 600,            "message": "Almost had my ride taken by other people.", "invested": False,
            },
            {   "name": "Car",
                "energy_change": -5,    "fun_change": 5,    "health_change": 0,
                "cost": 1000,           "message": "Rode my own car to my work.", "invested": False,
            },
        ]
        return self.create_options(options)
    
    def get_investment_options(self):
        options = [
            {   "name": "Stock (1 unit)",
                "energy_change": 0,   "fun_change": 0,  "health_change": 0, 
                "cost": 1000,              "message": "You invested in the stock market index!", "invested": True,
                "lower_range" : 0.945, "upper_range" : 1.05,
            },
            {   "name": "Stock (10 units)",
                "energy_change": 0,   "fun_change": 0,  "health_change": 0, 
                "cost": 10000,              "message": "You invested in the stock market index!", "invested": True,
                "lower_range" : 0.945, "upper_range" : 1.05,
            },
            {   "name": "Crypto (1 unit)",
                "energy_change": 0,   "fun_change": 0,  "health_change": 0, 
                "cost": 1000,              "message": "You invested in a variety of cryptocurrencies", "invested": True,
                "lower_range" : 0.73, "upper_range" : 1.20,
            },
            {   "name": "Crypto (10 units)",
                "energy_change": 0,   "fun_change": 0,  "health_change": 0, 
                "cost": 10000,              "message": "You invested in a variety of cryptocurrencies", "invested": True,
                "lower_range" : 0.73, "upper_range" : 1.20,
            }
        ]

        return self.create_options(options)
    
start = input(create_frame("Press Enter to start the game.") + "\n")
while True:
    if start == "":
        os.system("cls")
        start_sound.play()
        game = Game()
        game.game_loop()
        break
    else:
        start = input(create_frame("Invalid input. Please press Enter to continue.") + "\n")
