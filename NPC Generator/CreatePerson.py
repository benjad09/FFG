import os
import sys
import random
import json
from random import randint
import nameGenerator as names

global races
global racelist
global traits


def loadtraits():
	global traits
	try:
		datapull = open("Traitslist.txt", 'r').read()
		traits = datapull.split("\n")
		return traits
	except:
		return ["traits unavalible"]

def getracelist():
	return racelist

def loadRaces():
	global races
	global racelist
	races = {}
	racelist = []
	Dir = "./races"
	Files = os.listdir(Dir)
	for i in Files:
		oldjs = open(Dir+"/"+i, 'r').read()
		if i != "Droid.race":
			racelist.append(i.split(".",1)[0])
			races[racelist[-1]]=(json.loads(oldjs))
	#print(racelist);


def new(race):
	pick = race
	NPC = {}

	star = names.Words(randint(0,1000))

	for i in races[pick]["members"]:
		star.add(i)

	namelen = sum( map(len, races[pick]["members"]) ) / len(races[pick]["members"])


	NPC["Traits"] = []

	for i in range(0,randint(3,5)):
		NPC["Traits"].append(traits[randint(0,len(traits)-1)])
		pass

	NPC["Name"] = (star.make(randint(namelen-2,namelen+2)))
	NPC["Race"] = races[pick]["Species"]

	if randint(0,1):
		NPC["Gender"] = "M"
	else:
		NPC["Gender"] = "F"


	NPC["Brawn"] = int(races[pick]["Int"])
	NPC["Agility"] = int(races[pick]["Agility"])
	NPC["Int"] = int(races[pick]["Int"])
	NPC["Cun"] = int(races[pick]["Cun"])
	NPC["Will"] = int(races[pick]["Will"])
	NPC["Presence"] = int(races[pick]["Presence"])

	ageseed = randint(0,100)



	proposedage = int(races[pick]["Max Age"])+(int(races[pick]["Max Age"])*(ageseed*ageseed-200*ageseed)/10000)

	while proposedage<20:
		proposedage+=randint(7,10)

	NPC["Age"] = proposedage


	NPC["Height"] = float(races[pick]["Height"])*float(randint(90,110))/100



	#print(NPC)

	if len(races[pick]["skincolor"]):
		NPC["skincolor"] = races[pick]["skincolor"][randint(0,len(races[pick]["skincolor"])-1)]
	if len(races[pick]["eyecolor"]):
		NPC["eyecolor"] = races[pick]["eyecolor"][randint(0,len(races[pick]["eyecolor"])-1)]
	if len(races[pick]["haircolor"]):
		NPC["haircolor"] = races[pick]["haircolor"][randint(0,len(races[pick]["haircolor"])-1)]

	return NPC






def intpeople():
	loadRaces()
	loadtraits()



# another = 1;



# for x in range(0,1):
# 	#species_index = randint(0,len(races))
# 	#pick = "Wookiee"

# 	Char = new(racelist[randint(0,len(races)-1)])


	# print("Name: "+Char["Name"])
	# print("Race: "+Char["Race"])
	# print("Gender: "+Char["Gender"])
	# print("Age: "+str(Char["Age"]))
	# print("Height: "+str(Char["Height"]))
	# print("skincolor: "+Char["skincolor"])
	# print("eyecolor: "+Char["eyecolor"])
	# print("haircolor: "+Char["haircolor"])
	# print("Brawn: "+str(Char["Brawn"]))
	# print("Agility: "+str(Char["Agility"]))
	# print("Int: "+str(Char["Int"]))
	# print("Cun: "+str(Char["Cun"]))
	# print("Will: "+str(Char["Will"]))
	# print("Presence: "+str(Char["Presence"]))
	# print("Traits: ")
	# for i in Char["Traits"]:
	# 	print(i)
	#print("new charecter y/s")
	#if raw_input() == "y":
	#	another = 1
	#else:
	#	another = 0

# print("Done")

# while 1:
# 	pass
