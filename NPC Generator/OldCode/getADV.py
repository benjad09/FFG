import os
import sys
import json
directorys = []

pullData = open("adversaries.csv",'r').read()
itemize = pullData.split('\n')
headers = itemize[0].split(',')
headers[0] = 'Adversary'
print(headers)
itemize.pop(0)
itemize.pop(-1)
for i in itemize:
	i = i.split(',')
	directorys.append({})
	for j in range(0,len(i)):
		directorys[-1][headers[j]] = i[j]
for i in range(0,len(directorys)):
	directorys[i]["Skills"] = directorys[i]["Skills"].split(";")
	directorys[i]["Talents"] = directorys[i]["Talents"].split(";")
	directorys[i]["Abilities"] = directorys[i]["Abilities"].split(";")
	directorys[i]["Equipment"] = directorys[i]["Equipment"].split(";")
	directorys[i]["Index"] = directorys[i]["Index"].split(";")

later = []
factionnpc = []
droid = []
race = []
generic = []
faction = []
race = []

for i in directorys:
	print (i["Adversary"])
	ans = raw_input()
	# if ans:
	# 	print("Brawn")
	# 	i["Brawn"] = int(raw_input())
	# 	print("Agility")
	# 	i["Agility"] = int(raw_input())
	# 	print("Int")
	# 	i["Int"] = int(raw_input())
	# 	print("Cun")
	# 	i["Brawn"] = int(raw_input())
	# 	print("Will")
	# 	i["Will"] = int(raw_input())
	# 	print("Presence")
	# 	i["Presence"] = int(raw_input())
	# 	print("Soak")
	# 	i["Soak"] = int(raw_input())
	# 	print("Thresh")
	# 	i["Thresh"] = int(raw_input())
	# 	print("Defence")
	# 	i["Defence"] = raw_input()
	if ans == 'f':
		faction.append(i)
		print("faction")
	elif ans == 'd':
		droid.append(i)
		print("droid")
	elif ans == 'g':
		generic.append(i)
		print("generic")
	else:
		later.append(i)
		print("later")




File = ""
Dir = "./adversaries"
if not os.path.exists(Dir):
	os.mkdir(Dir)
Files = os.listdir(Dir)


for i in generic:
	if not i["Adversary"]+".adv" in Files:
		x = json.dumps(i)
		try:
			File = open(Dir+"/"+i["Adversary"]+".adv", 'a+')
			File.write(x)
			File.close()
		except:
			pass

File = ""
Dir = "./droids"
if not os.path.exists(Dir):
	os.mkdir(Dir)
Files = os.listdir(Dir)


for i in droid:
	if not i["Adversary"]+".adv" in Files:
		x = json.dumps(i)
		try:
			File = open(Dir+"/"+i["Adversary"]+".adv", 'a+')
			File.write(x)
			File.close()
		except:
			pass

File = ""
Dir = "./faction"
if not os.path.exists(Dir):
	os.mkdir(Dir)
Files = os.listdir(Dir)


for i in faction:
	if not i["Adversary"]+".adv" in Files:
		x = json.dumps(i)
		try:
			File = open(Dir+"/"+i["Adversary"]+".adv", 'a+')
			File.write(x)
			File.close()
		except:
			pass

File = ""
Dir = "./later"
if not os.path.exists(Dir):
	os.mkdir(Dir)
Files = os.listdir(Dir)


for i in directorys:
	if not i["Adversary"]+".adv" in Files:
		x = json.dumps(i)
		try:
			File = open(Dir+"/"+i["Adversary"]+".adv", 'a+')
			File.write(x)
			File.close()
		except:
			pass



while(1):
	pass