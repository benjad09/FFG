import os
import sys
import random
import json
from random import randint

global rooms
global x_size
global y_size
global minsize
global maxsize

global roomindex

def placeroominbox(parm):
	a_x = parm[0]
	a_y = parm[1]
	a_w = parm[2]
	a_h = parm[3]
	global rooms
	global rowsum
	global columnsum
	global roomindex
	roomindex += 1	
	if maxsize > (a_x+a_w):
		if (minsize == a_w):
			room_w = minsize
		else:
			room_w = randint(minsize,a_w)
	else:
		room_w = randint(minsize,maxsize)
	if maxsize > (a_y+a_h):
		if (minsize == a_h):
			room_h = minsize
		else:
			room_h = randint(minsize,a_h)
	else:
		room_h = randint(minsize,maxsize)

	if a_w <= room_w:
		room_x = a_x
	else:
		room_x = a_x+randint(0,(a_w-room_w))
	if a_h <= room_h:
		room_y = a_y
	else:
		room_y = a_y+randint(0,(a_h-room_h))
	for i in range(0,room_h):
		for j in range(0,room_w):
				rooms[i+room_y][j+room_x] = roomindex
				rowsum[j+room_x] += 1
				columnsum[i+room_y] += 1

def getbiggestsquare():
	havesquare = 0
	squaresinrow = 0
	squaresinrow_n = 0
	xs = []
	lines = []
	for y in range(0,len(rooms)):
		lines.append([])
		for x in range(0,len(rooms[y])):
			
			if havesquare:
				if rooms[y][x] != 0:
					havesquare = 0;
					lines[-1][-1][1] = x 
			else:
				if rooms[y][x] == 0:
					havesquare = 1
					lines[-1].append([x,x])
			if havesquare:
				lines[-1][-1][1] = x

		havesquare = 0
		addtriangle = 1

	active = []
	for j in range(0,len(lines[0])):
		active.append([lines[0][j][0],0,lines[0][j][1],0])
	for i in range(0,len(lines)):
		for j in range(0,len(lines[i])):
			addtriangle = 1
			for k in range(0,len(active)):
				
				if(active[k][3]+1 == i):
					if (active[k][0] == lines[i][j][0]) and (active[k][2] == lines[i][j][1]):
						active[k] = [active[k][0],active[k][1],active[k][2],i]
						addtriangle = 0
					elif (active[k][0] >= lines[i][j][0]) and (active[k][2] <= lines[i][j][1]):
						active[k] = [active[k][0],active[k][1],active[k][2],i]
			if addtriangle:
						active.append([lines[i][j][0],i,lines[i][j][1],i])

			


	sizes = []
	size = []
	
	for i in active:
		sizes.append([i[0],i[1],(i[2]-i[0]),(i[3]-i[1])])
		size.append(sizes[-1][2]*sizes[-1][3])
	maxindex = 0
	for i in range(0,len(sizes)):
		if(size[maxindex]<size[i]):
			maxindex = i
		#print(active[i])
		#print(sizes[i])
		#print(size[i])
	print(sizes[maxindex])
	return(sizes[maxindex])





x_size = 20
y_size = 30

minsize = 2
maxsize = 7

roomindex = 0

rooms = []
rowsum = []
columnsum = []

for i in range(0,y_size):
	rooms.append([])
	columnsum.append(0)
	for x in range(0,x_size):
		rooms[-1].append(0)
for x in range(0,x_size):
	rowsum.append(0)

continues = 1;
oppen = [0,0,x_size,y_size]
#placeroominbox(10,10,20,20)
while continues:
	print(oppen)
	placeroominbox(oppen)
	oppen = getbiggestsquare()
	if oppen[2]<2 or oppen[3]<2:
		continues = 0
	for i in rooms:
		print(i)

for i in rooms:
	print(i)

print("done")










while 1:
	pass