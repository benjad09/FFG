import os
import sys
import json
directorys = []

pullData = open("Ships.csv",'r').read()
pullData = pullData.replace('"', '')
itemize = pullData.split('\n')
headers = itemize[0].split(',')
print(headers)
itemize.pop(0)
itemize.pop(-1)
for i in itemize:
	i = i.split(',')
	print(i)
	directorys.append({})
	#for j in range(0,len(i)-1):
	#	directorys[-1][headers[j]] = i[j]


# File = ""
# Dir = "./Starships"
# if not os.path.exists(Dir):
# 	os.mkdir(Dir)
# Files = os.listdir(Dir)


# for i in directorys:
# 	if not i["Item"]+".ship" in Files:
# 		x = json.dumps(i)
# 		File = open(Dir+"/"+i["Item"]+".stsh", 'a+')
# 		File.write(x)
# 		File.close()


while(1):
	pass