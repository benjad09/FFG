import os
import sys
import random
import json

File = ""
Dir = "./faction"
Files = os.listdir(Dir)
skip = 0
for i in Files:
	if not skip:
		print(i)
		oldjs = open(Dir+"/"+i, 'r').read()
		adv = json.loads(oldjs)
		print("Brawn")
		adv["Brawn"] = int(raw_input())
		print("Agility")
		adv["Agility"] = int(raw_input())
		print("Int")
		adv["Int"] = int(raw_input())
		print("Cun")
		adv["Cun"] = int(raw_input())
		print("Will")
		adv["Will"] = int(raw_input())
		print("Presence")
		adv["Presence"] = int(raw_input())
		print("Soak")
		adv["Soak"] = int(raw_input())
		print("Thresh")
		adv["Thresh"] = int(raw_input())
		print("Defence")
		adv["Defence"] = raw_input()
		print("faction")
		adv["faction"] = raw_input()
		open(Dir+"/"+i,'w').close()
		x = json.dumps(adv)
		File = open(Dir+"/"+i, 'a+')
		File.write(x)
		File.close()
	else:
		print(i)
		if raw_input() == 's':
			skip=0
