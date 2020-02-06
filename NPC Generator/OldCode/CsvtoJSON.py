import os
import sys
import json
directorys = []

pullData = open("Races.csv",'r').read()
itemize = pullData.split('\n')
headers = itemize[0].split(',')
print(headers)
itemize.pop(0)
itemize.pop(-1)
for i in itemize:
	i = i.split(',')
	directorys.append({})
	for j in range(0,len(i)):
		directorys[-1][headers[j]] = i[j]


File = ""
Dir = "./races"
if not os.path.exists(Dir):
	os.mkdir(Dir)
Files = os.listdir(Dir)


for i in directorys:
	if not i["Species"]+".race" in Files:
		x = json.dumps(i)
		File = open(Dir+"/"+i["Species"]+".race", 'a+')
		File.write(x)
		File.close()


while(1):
	pass