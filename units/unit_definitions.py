class Unit():
	def __init__(self):
		self.actions = []
		self.verb = None

#command center
commandcenter = Unit()
commandcenter.verb = "Command Center: "
commandcenter.actions.append({"Command": "SCV", "Key": "s"})

#command center (advanced)
commandcenter2 = Unit()
commandcenter2.verb = "Command Center: "
commandcenter2.actions.append({"Command": "Nuclear Silo", "Key": "n"})
commandcenter2.actions.append({"Command": "ComSat Station", "Key": "c"})

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

factory2 = Unit()
factory2.verb = "Factory: "
factory2.actions.append({"Command": "Machine Shop", "Key":"c"})

#starport
starport = Unit()
starport.verb = 'Starport: '
starport.actions.append({"Command": "Wraith", "Key":"w"})
starport.actions.append({"Command": "Science Vessel", "Key":"v"})
starport.actions.append({"Command": "Dropship", "Key":"d"})
starport.actions.append({"Command": "Battlecruiser", "Key":"b"})
starport.actions.append({"Command": "Valkryie", "Key":"y;"})

#science facility
scifacility = Unit()
scifacility.verb = "Science Facility: "
scifacility.actions.append({"Command": "Covert Ops", "Key":"c;"})
scifacility.actions.append({"Command": "Physics Lab", "Key":"p;"})

#scv
scv = Unit()
scv.verb = "SCV: "
scv.actions.append({"Command": "Bunker", "Key": "u"})
scv.actions.append({"Command": "Command Center", "Key": "c"})
scv.actions.append({"Command": "Supply Depot", "Key": "s"})
scv.actions.append({"Command": "Barracks", "Key": "b"})
scv.actions.append({"Command": "Refinery", "Key": "r"})
scv.actions.append({"Command": "Engineering Bay", "Key": "e"})
scv.actions.append({"Command": "Missile Turret", "Key": "t"})
scv.actions.append({"Command": "Academy", "Key": "a"})

#scv (advanced)
scv2 = Unit()
scv2.verb = "SCV"
scv2.actions.append({"Command": "Factory", "Key":"f"})
scv2.actions.append({"Command": "Armory", "Key":"a"})
scv2.actions.append({"Command": "Science Facility", "Key":"i"})

#lieutenant
lieutenant_list = []
lieutenant_list.extend([commandcenter, scv])

#captain
captain_list = list(lieutenant_list)
captain_list.extend([barracks, scv2])

#major
major_list = list(captain_list)
major_list.extend([starport, factory])

#general
general_list = list(captain_list)
general_list.extend([commandcenter2, factory2, scifacility])
