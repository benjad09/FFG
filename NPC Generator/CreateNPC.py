import os
import sys
import random
import json
from random import randint
import nameGenerator as names
import CreatePerson as people

global Factions
global racelist
global traits
global factionlist


def loadfactons():
	global Factions
	global factionlist
	Factions = {}
	factionlist = []
	
	datapull = open("Factions.csv", 'r').read()
	lines = datapull.split("\n")
	for i in range(0,len(lines)):
		lines[i] = lines[i].split(",")
		#print(lines[i])
	lines[0].pop(0)
	lines.pop(-1)
	for i in range(0,len(lines[0])):
		Factions[lines[0][i]] = {}
		factionlist.append(lines[0][i])
		for k in range(1,len(lines)):
			Factions[lines[0][i]][lines[k][0]] = int(lines[k][i+1])
	#print(Factions)

def createNPC(faction):
	racetotal = 0
	for i in racelist:
		racetotal += Factions[faction][i]
	racethreshold = randint(0,racetotal)
	racesum = 0;
	raceindex = 0;
	while(racesum<racethreshold):
		racesum += Factions[faction][racelist[raceindex]]
		raceindex+=1
	randomrace = racelist[raceindex-1]
	NPC = people.new(randomrace)
	NPC["Faction"] = faction
	return NPC

def PrintNPC(Char):
	print("Name: "+Char["Name"])
	print("Race: "+Char["Race"]+" "+Char["Gender"])
	print("Faction: "+Char["Faction"])
	print("Age: "+str(Char["Age"]))
	print("Height: "+str(Char["Height"]))
	print("skincolor: "+Char["skincolor"])
	print("eyecolor: "+Char["eyecolor"])
	print("haircolor: "+Char["haircolor"])
	print("Brawn: "+str(Char["Brawn"]))
	print("Agility: "+str(Char["Agility"]))
	print("Int: "+str(Char["Int"]))
	print("Cun: "+str(Char["Cun"]))
	print("Will: "+str(Char["Will"]))
	print("Presence: "+str(Char["Presence"]))
	print("Traits: ")
	for i in Char["Traits"]:
		print(i)



	


people.intpeople()

racelist = people.getracelist()	
loadfactons()
print("choose faction")
for i in factionlist:
	print(i)
pick = raw_input()
another = 1
while another:

	PrintNPC(createNPC(pick))


	print("new charecter y/s change faction c")
	ans = raw_input()
	if ans == "y":
		another = 1
	elif ans == "c":
		print("choose faction")
		for i in factionlist:
			print(i)
		pick = raw_input()
	else:
		another = 0