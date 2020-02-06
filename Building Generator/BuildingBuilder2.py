import os
import sys
import random
import json
from random import randint


class building:
	def __init__(self):
		pass
	def generate(self,x_size,y_size,minsize,maxsize):
		self.x_size = x_size+1
		self.y_size = y_size
		self.minsize = minsize
		self.maxsize = maxsize
		self.building = []
		self.rooms = []
		self.index = 1
		for i in range(0,self.y_size):
			self.building.append([])
			for j in range(0,self.x_size):
				self.building[-1].append("____")

		self.placeroom(0,0,x_size,y_size)
		self.getlargest()
		while (self.a_w) >= self.minsize and (self.a_h) >= self.minsize:
			self.index+=1

			self.placeroom(self.a_x,self.a_y,self.a_w,self.a_h)
			#print("building")
			self.getlargest()

		for i in range(0,len(self.building)):
			self.building[i].pop(-1)
		self.x_size -= 1
			
			
			


		print(len(self.rooms))
		#self.newwalls()
		self.findhalls()

		for i in self.building:
			print(i)
			pass
		for i in self.rooms:
			print(i["name"])
			#print(i["blocks"])
		self.buildwalls()
		self.placedoors()

	def savebuilding(self,name):
		File = ""
		Dir = "./buildings"
		Files = os.listdir(Dir)
		if name+".building" in Files:
			open(Dir+"/"+name+".building",'w').close()
		File = open(Dir+"/"+name+".building", 'a+')
		save_dir = {}
		save_dir["xsize"] = self.x_size
		save_dir["ysize"] = self.y_size
		save_dir["building"] = self.building
		save_dir["hwall"] = self.horizontalwalls
		save_dir["vwall"] = self.verticalwalls
		save_dir["rooms"] = self.rooms
		x = json.dumps(save_dir)
		
		File.write(x)
		File.close()

	def loadbuilding(self,name):
		File = ""
		Dir = "./buildings"
		Files = os.listdir(Dir)

		if name+".building" in Files:
			oldjs = open(Dir+"/"+name+".building", 'r').read()
			save_dir = json.loads(oldjs)
			self.x_size = save_dir["xsize"] 
			self.y_size = save_dir["ysize"] 
			self.building = save_dir["building"] 
			self.horizontalwalls = save_dir["hwall"] 
			self.verticalwalls = save_dir["vwall"] 
			self.rooms = save_dir["rooms"] 



	def findhalls(self):
		index = 0
		for i in range(0,len(self.building)):
			for j in range(0,len(self.building[i])):
				if(self.building[i][j] == "____"):
					self.building[i][j] = "h"+str(index).zfill(2)
					index += 1
				if("h" in self.building[i][j]):
					# if self.building[min([i+1,len(self.building)-1])][j] == "___":
					# 	self.building[min([i+1,len(self.building)-1])][j] = self.building[i][j]
					if self.building[i][min([j+1,len(self.building[i])-1])] == "____":
						self.building[i][min([j+1,len(self.building[i])-1])] = self.building[i][j]


		for i in range(0,10):
			for i in range(0,len(self.building)-1):
				for j in range(0,len(self.building[i])):
					if "h" in self.building[i][j]:
						if "h" in self.building[i+1][j]:
							if self.building[i][j] != self.building[i+1][j]:
									index = 0
									#replace = 1
									while (j+index<len(self.building[0])) and ("h" in self.building[i+1][j+index]):
										self.building[i+1][j+index] = self.building[i][j]
										index += 1
									index = 0
									while (j-index>=0) and ("h" in self.building[i+1][j-index]):
										self.building[i+1][j-index] = self.building[i][j]
										index += 1
			for i in range(len(self.building)-1,0,-1):
			#for i in range(1,len(self.building)):
				for j in range(0,len(self.building[i])):
					if "h" in self.building[i][j]:
						if "h" in self.building[i-1][j]:
							if self.building[i][j] != self.building[i-1][j]:
									index = 0
									replace = 1
									while (j+index<len(self.building[0])) and ("h" in self.building[i-1][j+index]):
										self.building[i-1][j+index] = self.building[i][j]
										index += 1
									index = 0
									while (j-index>=0) and ("h" in self.building[i-1][j-index]):
										self.building[i-1][j-index] = self.building[i][j]
										index += 1
		for i in range(0,self.y_size):
			for j in range(0,self.x_size):
				if "h" in self.building[i][j]:
					index = 0
					hallexist = 0
					for k in range(0,len(self.rooms)):
						if self.rooms[k]["name"] == self.building[i][j]:
							hallexist = 1
							self.rooms[k]["blocks"].append([j,i])
					if not hallexist:
						self.rooms.append({})
						self.rooms[-1]["name"] = self.building[i][j]
						self.rooms[-1]["blocks"] = []
						self.rooms[-1]["blocks"].append([j,i])
		hallindex = 0
		ventindex = 0
		for i in range(0,len(self.rooms)):
			if "h" in self.rooms[i]["name"]:
				amivent = 1;
				for j in self.rooms[i]["blocks"]:
					if j[0] > 0:
						if j[1] > 0:
							if self.building[j[1]][j[0]] == self.building[j[1]-1][j[0]-1]:
								if self.building[j[1]][j[0]] ==  self.building[j[1]][j[0]-1] and self.building[j[1]][j[0]] == self.building[j[1]-1][j[0]]:
									amivent = 0
						if j[1] <self.y_size-1:
							if self.building[j[1]][j[0]] == self.building[j[1]+1][j[0]-1]:
								if self.building[j[1]][j[0]] == self.building[j[1]][j[0]-1] and self.building[j[1]][j[0]] == self.building[j[1]+1][j[0]]:
									amivent = 0
					if j[0]<self.x_size-1:
						if j[1] > 0:
							if self.building[j[1]][j[0]] == self.building[j[1]-1][j[0]+1]:
								if self.building[j[1]][j[0]] == self.building[j[1]][j[0]+1] and self.building[j[1]][j[0]] == self.building[j[1]-1][j[0]]:
									amivent = 0
						if j[1] <self.y_size-1:
							if self.building[j[1]][j[0]] == self.building[j[1]+1][j[0]+1]:
								if self.building[j[1]][j[0]] == self.building[j[1]][j[0]+1] and self.building[j[1]][j[0]] == self.building[j[1]+1][j[0]]:
									amivent = 0
				#print(self.rooms[i]["name"])
				#print(amivent)
				if amivent:
					newname = "v"+str(ventindex).zfill(3)
					ventindex += 1
				else:
					newname = "h"+str(hallindex).zfill(3)
					hallindex += 1
				self.rooms[i]["name"] = newname
				for j in self.rooms[i]["blocks"]:
					self.building[j[1]][j[0]] = self.rooms[i]["name"]
				i = 0
				if hallindex == 0:
					while "v" not in self.rooms[i]["name"]:
						i += 1
					newname = "h"+str(hallindex).zfill(3)
					hallindex += 1
					self.rooms[i]["name"] = newname
					for j in self.rooms[i]["blocks"]:
						self.building[j[1]][j[0]] = self.rooms[i]["name"]




	def placedoors(self):
		for i in range(0,len(self.rooms)):
			if "h" in self.rooms[i]["name"] or "v" in self.rooms[i]["name"]:
				self.rooms[i]["connected"] = []
				self.rooms[i]["connected"].append(self.rooms[i]["name"])
				randomindex = []
				for k in self.rooms[i]["blocks"]:
					randomindex.append(k)
				if "h" in self.rooms[i]["name"]:
					while len(randomindex):
						s = randint(0,len(randomindex)-1)
						j = randomindex[s]
						#print(j)
						randomindex.pop(s)
						if j[0] > 0:
							if self.building[j[1]][j[0]-1] not in self.rooms[i]["connected"]:
								if "h" not in self.building[j[1]][j[0]-1]:
									self.rooms[i]["connected"].append(self.building[j[1]][j[0]-1])
									self.horizontalwalls[j[1]][j[0]] = 2
									for l in range(0,len(self.rooms)):
										if self.rooms[l]["name"] == self.rooms[i]["connected"][-1]:
											self.rooms[l]["doors"].append(self.rooms[i]["name"])
						if j[0]<self.x_size-1:
								if self.building[j[1]][j[0]+1] not in self.rooms[i]["connected"]:
									if "h" not in self.building[j[1]][j[0]+1]:
										self.rooms[i]["connected"].append(self.building[j[1]][j[0]+1])
										self.horizontalwalls[j[1]][j[0]+1] = 2
										for l in range(0,len(self.rooms)):
											if self.rooms[l]["name"] == self.rooms[i]["connected"][-1]:
												self.rooms[l]["doors"].append(self.rooms[i]["name"])
						if j[1] > 0:
							if self.building[j[1]-1][j[0]] not in self.rooms[i]["connected"]:
								if "h" not in self.building[j[1]-1][j[0]]:
									self.rooms[i]["connected"].append(self.building[j[1]-1][j[0]])
									self.verticalwalls[j[1]][j[0]] = 2
									for l in range(0,len(self.rooms)):
										if self.rooms[l]["name"] == self.rooms[i]["connected"][-1]:
											self.rooms[l]["doors"].append(self.rooms[i]["name"])
						if j[1] <self.y_size-1:
							if self.building[j[1]+1][j[0]] not in self.rooms[i]["connected"]:
								if "h" not in self.building[j[1]+1][j[0]]:
									self.rooms[i]["connected"].append(self.building[j[1]+1][j[0]])
									self.verticalwalls[j[1]+1][j[0]] = 2
									for l in range(0,len(self.rooms)):
										if self.rooms[l]["name"] == self.rooms[i]["connected"][-1]:
											self.rooms[l]["doors"].append(self.rooms[i]["name"])
				else:
					while len(randomindex):
						s = randint(0,len(randomindex)-1)
						j = randomindex[s]
						#print(j)
						randomindex.pop(s)
						if j[0] > 0:
							if self.building[j[1]][j[0]-1] not in self.rooms[i]["connected"]:
								self.rooms[i]["connected"].append(self.building[j[1]][j[0]-1])
								self.horizontalwalls[j[1]][j[0]] = 3
						if j[0]<self.x_size-1:
							if self.building[j[1]][j[0]+1] not in self.rooms[i]["connected"]:
								self.rooms[i]["connected"].append(self.building[j[1]][j[0]+1])
								self.horizontalwalls[j[1]][j[0]+1] = 3
						if j[1] > 0:
							if self.building[j[1]-1][j[0]] not in self.rooms[i]["connected"]:
								self.rooms[i]["connected"].append(self.building[j[1]-1][j[0]])
								self.verticalwalls[j[1]][j[0]] = 3
						if j[1] <self.y_size-1:
							if self.building[j[1]+1][j[0]] not in self.rooms[i]["connected"]:
								self.rooms[i]["connected"].append(self.building[j[1]+1][j[0]])
								self.verticalwalls[j[1]+1][j[0]] = 3

		for i in range(0,len(self.rooms)):
			if "doors" in self.rooms[i]:
				self.rooms[i]["connected"] = []
				self.rooms[i]["connected"].append(self.rooms[i]["name"])
				for q in range(0,100):
					if(len(self.rooms[i]["doors"])<1):
						self.place_randdoor(i)

	def place_randdoor(self,i):
		j = self.rooms[i]["blocks"][randint(0,len(self.rooms[i]["blocks"])-1)]
		if j[0] > 0:
			if self.building[j[1]][j[0]-1] not in self.rooms[i]["connected"]:
				if "v" not in self.building[j[1]][j[0]-1]:
					for l in range(0,len(self.rooms)):
						if self.rooms[l]["name"] == self.building[j[1]][j[0]-1]:
							if len(self.rooms[l]["doors"])>0:
								self.rooms[i]["connected"].append(self.building[j[1]][j[0]-1])
								self.rooms[i]["doors"].append(self.building[j[1]][j[0]-1])
								self.horizontalwalls[j[1]][j[0]] = 2
								self.rooms[l]["doors"].append(self.rooms[i]["name"])
					
						
		if j[0]<self.x_size-1:
			if self.building[j[1]][j[0]+1] not in self.rooms[i]["connected"]:
				if "v" not in self.building[j[1]][j[0]+1]:
					for l in range(0,len(self.rooms)):
						if self.rooms[l]["name"] == self.building[j[1]][j[0]+1]:
							if len(self.rooms[l]["doors"])>0:
								self.rooms[i]["connected"].append(self.building[j[1]][j[0]+1])
								self.rooms[i]["doors"].append(self.building[j[1]][j[0]+1])
								self.horizontalwalls[j[1]][j[0]+1] = 2
								self.rooms[l]["doors"].append(self.rooms[i]["name"])
							
		if j[1] > 0:
			if self.building[j[1]-1][j[0]] not in self.rooms[i]["connected"]:
				if "v" not in self.building[j[1]-1][j[0]]:
					for l in range(0,len(self.rooms)):
						if self.rooms[l]["name"] == self.building[j[1]-1][j[0]]:
							if len(self.rooms[l]["doors"])>0:
								self.rooms[i]["connected"].append(self.building[j[1]-1][j[0]])
								self.rooms[i]["doors"].append(self.building[j[1]-1][j[0]])
								self.verticalwalls[j[1]][j[0]] = 2
								self.rooms[l]["doors"].append(self.rooms[i]["name"])
							
		if j[1] <self.y_size-1:
			if self.building[j[1]+1][j[0]] not in self.rooms[i]["connected"]:
				if "v" not in self.building[j[1]+1][j[0]]:
					for l in range(0,len(self.rooms)):
						if self.rooms[l]["name"] == self.building[j[1]+1][j[0]]:
							if len(self.rooms[l]["doors"])>0:
								self.rooms[i]["connected"].append(self.building[j[1]+1][j[0]])
								self.rooms[i]["doors"].append(self.building[j[1]+1][j[0]])
								self.verticalwalls[j[1]+1][j[0]] = 2
								self.rooms[l]["doors"].append(self.rooms[i]["name"])













	def placeroom(self,r_x,r_y,r_w,r_h):
		seed = randint(0,100);

		randwheight = r_w - ((r_w * seed * seed)/10000)
		randwheight = r_w - ((r_w *seed * seed * seed)/1000000)
		randwheight = max([self.minsize,randwheight])
		room_w = min([self.maxsize,r_w,randwheight])
		seed = randint(0,100);
		randwheight = r_h - ((r_h * seed * seed)/10000)
		randwheight = r_h - ((r_h *seed * seed * seed)/1000000)
		randwheight = max([self.minsize,randwheight])
		room_h = min([self.maxsize,r_w,randwheight])



		#room_w = min([self.maxsize,randint(self.minsize,r_w)])
		#room_h = min([self.maxsize,randint(self.minsize,r_h)])

		room_x = randint(r_x,r_w-room_w+r_x)
		room_y = randint(r_y,r_h-room_h+r_y)
		self.rooms.append({})
		self.rooms[-1]["cordinates"] = ([room_x,room_y,room_w,room_h])
		self.rooms[-1]["name"] = "r"+str(self.index).zfill(3)
		self.rooms[-1]["doors"] = []
		self.rooms[-1]["blocks"] = []
		for i in range(0,room_h):
			for j in range(0,room_w):
					self.building[i+room_y][j+room_x] = self.rooms[-1]["name"]
					self.rooms[-1]["blocks"].append([j+room_x,i+room_y])

	def getlargest(self):
		havesquare = 0
		lines = []
		for y in range(0,len(self.building)):
			lines.append([])
			for x in range(0,len(self.building[y])):
				
				if havesquare:
					if self.building[y][x] != "____":
						havesquare = 0;
						lines[-1][-1][1] = x-1 
				else:
					if self.building[y][x] == "____":
						havesquare = 1
						lines[-1].append([x,x])
				if havesquare:
					lines[-1][-1][1] = x-1

			havesquare = 0
		active = []
		
		for j in range(0,len(lines[0])):
			active.append([lines[0][j][0],0,lines[0][j][1],0])
		for i in range(0,len(lines)):
			for j in range(0,len(lines[i])):
				
				addtriangle = 1
				for k in range(0,len(active)):
					
					if active[k][3]+1 == i: #check if neigbors
						if (active[k][0] == lines[i][j][0]) and (active[k][2] == lines[i][j][1]):
							active[k] = [active[k][0],active[k][1],active[k][2],i]
							addtriangle = 0
						elif (active[k][0] >= lines[i][j][0]) and (active[k][2] <= lines[i][j][1]):
							active[k] = [active[k][0],active[k][1],active[k][2],i]
				if addtriangle:
					active.append([lines[i][j][0],i,lines[i][j][1],i])
		active2 = []
		for j in range(0,len(lines[-1])):
			active2.append([lines[-1][j][0],0,lines[-1][j][1],0])
		for i in range(len(lines)-1,0,-1):
			for j in range(0,len(lines[i])):
				addtriangle = 1
				for k in range(0,len(active2)):
					if active2[k][3]+1 == i: #check if neigbors
						if (active2[k][0] == lines[i][j][0]) and (active2[k][2] == lines[i][j][1]):
							active2[k] = [active2[k][0],i,active2[k][2],active2[k][3]]
							addtriangle = 0
						elif (active2[k][0] >= lines[i][j][0]) and (active2[k][2] <= lines[i][j][1]):
							active2[k] = [active2[k][0],i,active2[k][2],active2[k][3]]
				if addtriangle:
					active2.append([lines[i][j][0],i,lines[i][j][1],i])
		
		active2.pop(0)

		for i in active2:
			active.append(i)

		active.pop(0)
		size = []
		cordinates = []
		maxindex = 0
		m = 0 
		for i in active:
			cordinates.append([i[0],i[1],(i[2]-i[0])+1,(i[3]-i[1])+1])
			if cordinates[-1][2]>self.minsize and cordinates[-1][3]>self.minsize:
				size.append((cordinates[-1][2]*cordinates[-1][3]))
			else:
				size.append(self.minsize*self.minsize)
			#size.append((cordinates[-1][2]*cordinates[-1][3]))
			if size[maxindex]<size[-1]:
				maxindex = m
			m += 1
		self.a_x = cordinates[maxindex][0]
		self.a_y = cordinates[maxindex][1]
		self.a_w = cordinates[maxindex][2]-0
		self.a_h = cordinates[maxindex][3]
		#print("final picks")
		#print(self.a_x)
		#print(self.a_y)
		#print(self.a_w)
		#print(self.a_h)

	def buildwalls(self):
		self.horizontalwalls = []
		for i in range(0,self.y_size):
			self.horizontalwalls.append([])
			self.lastvalue = "xxx"
			for j in range(0,self.x_size):
				if self.lastvalue == self.building[i][j]:
					self.horizontalwalls[-1].append(0)
				else:
					self.horizontalwalls[-1].append(1)
				self.lastvalue = self.building[i][j]
			self.horizontalwalls[-1].append(1)
		

		self.verticalwalls = []
		self.lastvert = []
		for j in range(0,self.x_size):
			self.lastvert.append("xxx")
		for i in range(0,self.y_size):
			self.verticalwalls.append([])
			for j in range(0,self.x_size):
				if self.lastvert[j] == self.building[i][j]:
					self.verticalwalls[-1].append(0)
				else:
					self.verticalwalls[-1].append(1)
				self.lastvert[j] = self.building[i][j]
		self.verticalwalls.append([])
		for j in range(0,self.x_size):		
			self.verticalwalls[-1].append(1)








	def getrooms(self):
		return_this = []
		for i in self.rooms:
			if "cordinates" in i:
				return_this.append(i["cordinates"])
		return return_this

	def gethorzwall(self):
		return self.horizontalwalls
	def getvertwall(self):
		return self.verticalwalls



						



