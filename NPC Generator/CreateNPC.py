import os
import sys
import random
import json
from random import randint
import nameGenerator as names
import CreatePerson as people

global Factions
global racelist
global racelist2
global traits
global factionlist
global advlist
global adv


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
def loadadversaries():
	global advlist
	global adv
	adv = {}
	advlist = []
	Dir = "./adversaries"
	Files = os.listdir(Dir)
	for i in Files:
		oldjs = open(Dir+"/"+i, 'r').read()
		advlist.append(i.split(".",1)[0])
		adv[advlist[-1]]=(json.loads(oldjs))
	Dir = "./faction"
	Files = os.listdir(Dir)
	for i in Files:
		oldjs = open(Dir+"/"+i, 'r').read()
		advlist.append(i.split(".",1)[0])
		adv[advlist[-1]]=(json.loads(oldjs))
	advlist.insert(0,"None")
	adv["None"] = {}
	adv["None"]["Agility"] = 0
	adv["None"]["Abilities"] = ["None"]
	adv["None"]["Soak"] = 2
	adv["None"]["Level"] =  "Rival"
	adv["None"]["Skills"] = ["None"]
	adv["None"]["Int"] = 0
	adv["None"]["Cun"] = 0
	adv["None"]["Will"] = 0
	adv["None"]["Brawn"] = 0
	adv["None"]["Presence"] = 0
	adv["None"]["Equipment"] = ["Personal"]
	adv["None"]["Talents"] = ["None"]
	adv["None"]["Defence"] = "0"
	adv["None"]["Thresh"] = 5
	adv["None"]["Adversary"]= "None"




def createGenaric(faction = 'None',race = "Random"):
	racetotal = 0
	if race == "Random":
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
	else:
		NPC = people.new(race)
		NPC["Faction"] = faction
	return NPC


def createNPC(faction = 'None',race = 'Random',advers="None"):
	Base = createGenaric(faction,race)
	Base["Abilities"] = adv[advers]["Abilities"]
	Base["Soak"] = adv[advers]["Soak"]
	Base["Level"] = adv[advers]["Level"]
	Base["Abilities"] = adv[advers]["Abilities"]
	Base["Equipment"] = adv[advers]["Equipment"]
	Base["Talents"] = adv[advers]["Talents"]
	Base["Defence"] = adv[advers]["Defence"]
	Base["Thresh"] = adv[advers]["Thresh"]
	Base["Adversary"] = adv[advers]["Adversary"]
	

	Base["Agility"]=max(adv[advers]["Agility"],Base["Agility"])
	Base["Cun"]=max(adv[advers]["Cun"],Base["Cun"])
	Base["Int"]=max(adv[advers]["Int"],Base["Int"])
	Base["Will"]=max(adv[advers]["Will"],Base["Will"])
	Base["Brawn"]=max(adv[advers]["Brawn"],Base["Brawn"])
	Base["Presence"]=max(adv[advers]["Presence"],Base["Presence"])



	NPC = Base
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



def initNPC():
	global racelist
	people.intpeople()
	racelist = people.getracelist()	
	loadfactons()
	loadadversaries()

def getfactions():
	return factionlist

def getadv():
	return advlist

def getraces():
	return racelist




# print("choose faction")
# for i in factionlist:
# 	print(i)
# pick = raw_input()
# another = 1
# while another:

# 	PrintNPC(createNPC(0,"None","Chiss"))


# 	print("new charecter y/s change faction c")
# 	ans = raw_input()
# 	if ans == "y":
# 		another = 1
# 	elif ans == "c":
# 		print("choose faction")
# 		for i in factionlist:
# 			print(i)
# 		pick = raw_input()
# 	else:
# 		another = 0