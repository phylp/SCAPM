
def create_unit_list(rank):
	unit_list = []
	if rank == "Lieutenant":
		unit_list.append(commandcenter)
		unit_list.append(barracks)
		unit_list.append(factory)
		return unit_list

class Unit():
	def __init__(self):
		self.actions = []
		self.verb = None

#command center
commandcenter = Unit()
commandcenter.verb = "Command Center: "
commandcenter.actions.append({"Command": "SCV", "Key": "s"})
commandcenter.actions.append({"Command": "Nuclear Silo", "Key": "n"})
commandcenter.actions.append({"Command": "ComSat Station", "Key": "c"})

#barracks
barracks = Unit()
barracks.verb = "Barracks: "
barracks.actions.append({"Command": "Marine", "Key": "m"})
barracks.actions.append({"Command": "FireBat", "Key": "f"})
barracks.actions.append({"Command": "Medic", "Key": "c"})
barracks.actions.append({"Command": "Ghost", "Key": "g"})

#factory
factory = Unit()
factory.verb = "Factory: "
factory.actions.append({"Command": "Vulture", "Key":"v"})
factory.actions.append({"Command": "Siege Tank", "Key":"t"})
factory.actions.append({"Command": "Goliath", "Key":"g"})
