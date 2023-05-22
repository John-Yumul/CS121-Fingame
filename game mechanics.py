import shutil
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
a = """Here's the Game Mechanics

First and foremost, the game requires for you to keep your well-being score as high as possible.
Well-being is about staying robust in various areas of your life.
You can't affect your well-being score directly. It's based on the scores of these following areas:

> FUN SCORE - this shows you how much fun you're having! You can raise your fun score by buying things to keep you busy 
such as books or video games, as well as by doing leisurely activities such as meeting friends or playing football.

> HEALTH SCORE - this is a measure of the condition of your physical health.
Participating in sports and getting an ample amount can increase your score in this area. 
If you don't do this enough, or if you eat unhealthy food, this will go down.

> COMFORT SCORE - this goes down whenever you do something that's requires a lot of hard work and effort, such 
as exercising or cooking for yourself. 
Contrarily, you can raise it with things that bring ease and comfort to life, such as a dishwasher or a winter coat.

> SATISFACTION - this is increased by anything in the game that makes you feel good about yourself. 
Giving money to charity, reading a book, or exercising will all increase your satisfaction levels."""
framed_text = create_frame(a)
print(framed_text)

b = """Most things in the game don't come for free! 
Every month, you'll get paid for doing your job, but you also have bills to pay. You have to decide where to spend 
your left-over money on. 
Your balance tells you how much money you've got in the bank.
Every week, you must make FIVE choices for each of these things:

> FOOD - what you eat
> LEISURE - how you spend your free time
> EXERCISE - how you maintain your physical fitness
> TRANSPORTATION - how you get around

There are also lots of items you can buy to increase your scores - but you don't have to.
Some items don't increase your scores, but they allow you to do other things. For example, you need 
to buy trainers to go running. 
You start the game with some items already."""
framed_text = create_frame(b)
print(framed_text)

c = """Each week in the game lasts one turn. Once you've made all your choices for the week, 
you need to click the 'GO TO NEXT WEEK' button. Then your scores will change before the next turn starts.

To win, you need to stay in the game for 12 weeks. 
If you run out of money before then, or your well-being drops too low, it's game over! 
You need to make sure you always have enough money in the bank to pay for all your bills. 
After 12 weeks, you can carry on playing if you like.

Don't forget to read your messages every week for advice on how you're doing, updates on your expenditure, and other 
important news. 
The Finance Screen shows you all your fixed payments for the month, and a list of all your recent spending - 
use it to plan how much you're going to spend."""
framed_text = create_frame(c)
print(framed_text)
