import sys
from utils import console
from utils import terminal
import time
from models.player import Player
from models.level import Level

#resources
title = open('./resources/title.txt').read()
welcome = open('./resources/welcome.txt').read()
training = open('./resources/training.txt').read()
# bindings = open('./resources/bindings.txt').read()

# LOAD 
counter = 25
while counter < 100:
	counter += 1
	print("loading " + str(counter) + '%')
	print('=' * counter)
	console.clear(.02)

# TITLE 
print(title)
console.clear(1)

# USER 
user = None
waiting = True
while waiting:
	print("""
Game Options

1. Use default name
2. Use custom name
		""")
	answer = int(input("Please select your desired game mode\n"))
	if answer == 1:
		user = Player()
		waiting = False
		console.clear(.5)
	elif answer == 2:
		custom_name = str(input("\n Please enter your name. \n"))
		user = Player(custom_name)
		waiting = False
		console.clear(.5)
	else:
		print("not recognized")
		console.clear(1) 

# TRAIN
training_requested = str(input(("{} {} {}".format("Welcome, Lieutenant", user.name, ". Would you like to read the training manual? Y/N \n"))))

if training_requested.lower() == 'y':
	print(training)
	input("Press enter when done.")


# GAME 
#wrap this in a loop to change levels

level_score = 0
level_attempts = 0
level_rank = user.rank
level = Level(level_rank)
start = time.time()

while(time.time() - start < 30):
	level.read()
	key = console.getch()
	if key == level.key:
		level_score += 1
	level_attempts += 1
	level.restart()

print("{} {}".format("Your Score:", str(level_score)))
print("{} {}".format("Attempts:", str(level_attempts)))
print("{} {} {}".format("Efficiency:", str(round(level_score/level_attempts, 3)), "%"))
	