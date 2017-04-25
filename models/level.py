
import random
import math
from utils import console
from units import units

def generate_command(rank):
	unit_list = units.create_unit_list(rank)
	random1 = random.randint(0,len(unit_list)-1)
	random2 = random.randint(0, len(unit_list[random1].actions)-1)
	target = unit_list[random1].actions[random2]
	console.clear(.05)
	return (unit_list[random1].verb, target["Command"], target["Key"])

class Level():
	def __init__(self, rank):
		self.rank = rank
		self.current = generate_command(rank);
		self.command = "{} {}".format(self.current[0], self.current[1])
		self.key = self.current[2]

	def read(self):
		print(self.command)

	def restart(self):
		self.current = generate_command(self.rank);
		self.command = "{} {}".format(self.current[0], self.current[1])
		self.key = self.current[2]
