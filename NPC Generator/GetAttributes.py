
import os
import sys

pullData = open("Traits.csv",'r').read()
print(pullData)
traits = pullData.split('\n')
File = open("Traitslist.txt", 'a+')

for i in traits:
	i = i.split(". ", 1)[1]
	File.write(i+'\n')


while(1):
	pass