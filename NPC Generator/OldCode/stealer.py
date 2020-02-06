import os
import sys
import random
import json
from random import randint
import nameGenerator as names



load = "Zabrak"
final = ""
species = {}

stealtraits = ["skincolor","haircolor","eyecolor","distinctions","planet","language","members"]

pullData = open("PasteHere.txt",'r').read()
pullData = pullData.replace('{', '')
pullData = pullData.replace('}', '')
pullData = pullData.replace('[', '')
pullData = pullData.replace(']', '')
dataArray = pullData.split('\n')
for i in dataArray:
	i = i.split("<ref", 1)[0]
	i = i.split("/Legends", 1)[0]
	#print(i)
	final = final+i+"\n"
final = final.replace('=*', '=')
final = final.replace('*', ',')
dataArray = final.split('\n|');
dataArray.pop(0);
final = ""
for i in dataArray:
	i = i.replace('\n', '')
	param = i.split("=", 1)[0]
	values = i.split("=",1)[1]
	valuessplit = values.split(',')
	for j in range(0,len(valuessplit)):
		valuessplit[j] = valuessplit[j].split("(",1)[0]

	species[param] = valuessplit
	#print(valuessplit)
	#values = i.split("=", 1)[1]
#print(species)
File = ""
Dir = "./races"
Files = os.listdir(Dir)

if load+".race" in Files:
	oldjs = open(Dir+"/"+load+".race", 'r').read()
	race = json.loads(oldjs)
	print(race["Species"])

for i in stealtraits:
	race[i] = species[i]

if load+".race" in Files:
	open(Dir+"/"+load+".race",'w').close()
	x = json.dumps(race)
	File = open(Dir+"/"+load+".race", 'a+')
	File.write(x)
	File.close()
for i in Files:
	print(i.split(".",1)[0])

while 1:
	pass




	#for i in range(0,10):
		#print(star.make(randint(7,10)))
	#print(final)
