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

First and foremost, the game aims to keep your wellbeing score as high as possible.
Wellbeing is about staying well in all areas of your life.
You can't affect your wellbeing score directly it's based on some other scores you have to think about:

Fun score - this shows you how much fun you're having! You can raise your fun score by buying things to keep you busy 
such as books or video games, or by doing fun activities like meeting friends or playing football.

Health score - a measure of how good your health is.
Doing sport and getting exercise is good for your health. If you don't do this enough, or you eat unhealthy food, 
your health score will go down.

Comfort score - this goes down whenever you do something that's hard work or a lot of effort, including exercise or 
cooking for yourself. 
But you can raise it with things that make life easier or more comfortable, such as a dishwasher or a winter coat.

Satisfaction anything in the game that makes you feel good about yourself increases your satisfaction score. 
Giving money to charity, reading a book or doing some exercise will all increase your satisfaction levels."""
framed_text = create_frame(a)
print(framed_text)
b = """Most things in the game don't come for free! 
Every month you'll get paid for doing your job, but you also have bills to pay - you have to decide what to spend 
your left-over money on. 
Your balance tells you how much money you've got in the bank.
Every week you must make THREE choices for each of these things:

Activities-what you spend your time doing
Food - what you eat
Transport - how you get around

There are also lots of items you can buy to increase your scores - but you don't have to.
Some items don't increase your scores, but they allow you to do other things for example you need to buy trainers to  
go running. 
You start the game with some items already."""
framed_text = create_frame(b)
print(framed_text)

c = """Each week in the game lasts one turn. Once you've made all your choices for the week, you need to click the 'Go to 
next week' button. 
Then your scores will change before the next turn starts.

To win, you need to stay in the game for 12 weeks. 
If you run out of money before then, or your wellbeing drops too low, it's game over! 
You need to make sure you always have enough money in the bank to pay all your bills. 
After 12 weeks, you can carry on playing if you like.

Don't forget to read your messages every week for advice on how you're doing, updates on your spending, and other 
important news. 
The Finance screen shows you all your fixed payments for the month, and a list of all your recent spending - use it to
plan how much you're going to spend."""
framed_text = create_frame(c)
print(framed_text)
