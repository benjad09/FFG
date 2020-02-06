import os
import sys
import random
import json
from random import randint



class advancedroom:
	def __init__(self,hotzwalls,vertwalls):
		self.hotzwall = hotzwalls
		self.vertwall = vertwalls
		self.room = {}
	def createspaces(self):
		self.room["space"] = []
		for i in range(0,len(self.hotzwall)):
			self.room["space"].append([])
			for j in range(0,len(self.vertwall[0])):
				self.room["space"][-1].append(0)
		for i in range(0,len(self.hotzwall)):
			if "d" in self.hotzwall[i][0]:
				self.room["space"][i][0] = 1
			if "d" in self.hotzwall[i][1]:
				self.room["space"][i][-1] = 1
		for i in range(0,len(self.vertwall[0])):
			if "d" in self.vertwall[0][i]:
				self.room["space"][0][i] = 1
			if "d" in self.vertwall[1][i]:
				self.room["space"][-1][i] = 1


		for i in self.room["space"]:
			print(i)
		self.room["xsize"] = len(self.room["space"][0])
		self.room["ysize"] = len(self.room["space"])
		print(self.room["xsize"])
		print(self.room["ysize"])

	def returnroom(self):
		self.room["hotzwall"] = self.hotzwall
		self.room["vertwall"] = self.vertwall
		return self.room

			
