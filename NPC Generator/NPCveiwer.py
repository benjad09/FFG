import Tkinter as tk
from Tkinter import *
import random
import CreateNPC as NPC
from random import randint
import os
import json
global r


class MainWindow:
	def __init__(self,master):
		
		self.master = master

		self.master.state('zoomed')

		self.master.title("NPC Vewier")

		self.placeOptions()

		self.printchar()

		self.printNPC()

		self.NPC = NPC.createNPC()

		self.loadandsave = tk.Frame(self.master)
		self.save = tk.Button(self.loadandsave,text = "save",command = self.saveNPC)
		self.save.place(relx = 0,rely = 0,relheight = .5,relwidth = .5)
		self.entries = tk.Entry(self.loadandsave)
		self.entries.place(relx = .5,rely = 0,relheight = .5,relwidth = .5)
		self.variable = tk.StringVar(self.master)
		self.savefiles = get_saves()
		self.options = tk.OptionMenu(self.loadandsave, self.variable, *self.savefiles)
		self.loading = tk.Button(self.loadandsave,text = "Load",command = self.loadNPC)
		self.options.place(relx = 0,rely = .5,relheight = .5,relwidth = .5)
		self.loading.place(relx = .5,rely = .5,relheight = .5,relwidth = .5)
		self.loadandsave.place(relx = 0,rely = .2,relwidth = .2,relheight = .1)

	def printNPC(self):
		self.NPCL = tk.Frame(self.master)

		
		# Base["Soak"] = adv[advers]["Soak"]
		# Base["Level"] = adv[advers]["Level"]
		# Base["Abilities"] = adv[advers]["Abilities"]
		# Base["Equipment"] = adv[advers]["Equipment"]
		# Base["Talents"] = adv[advers]["Talents"]
		# Base["Defence"] = adv[advers]["Defence"]
		# Base["Thresh"] = adv[advers]["Thresh"]
		# Base["Adversary"] = adv[advers]["Adversary"]

		# Base["Agility"]=max(adv[advers]["Agility"],Base["Agility"])
		# Base["Cun"]=max(adv[advers]["Cun"],Base["Cun"])
		# Base["Int"]=max(adv[advers]["Int"],Base["Int"])
		# Base["Will"]=max(adv[advers]["Will"],Base["Will"])
		# Base["Brawn"]=max(adv[advers]["Brawn"],Base["Brawn"])
		# Base["Presence"]=max(adv[advers]["Presence"],Base["Presence"])

		self.Adversary = tk.Label(self.NPCL,text = "Type: ",bg = 'white')
		self.Level = tk.Label(self.NPCL,text = "Lvl: ",bg = 'white')
		self.Brawn =  tk.Label(self.NPCL,text = "0\nBrawn",bg = 'white')
		self.Agle =  tk.Label(self.NPCL,text = "0\nAgility",bg = 'white')
		self.Intel =  tk.Label(self.NPCL,text = "0\nIntellect",bg = 'white')
		self.Cun =  tk.Label(self.NPCL,text = "0\nCunning",bg = 'white')
		self.Will =  tk.Label(self.NPCL,text = "0\nWillpower",bg = 'white')
		self.Pres =  tk.Label(self.NPCL,text = "0\nPresence",bg = 'white')
		self.Soak = tk.Label(self.NPCL,text = "Soak: ",bg = 'white')
		self.Thresh = tk.Label(self.NPCL,text = "Wound: ",bg = 'white')
		self.Defence = tk.Label(self.NPCL,text = "Defence: ",bg = 'white')
		self.Talents = tk.Label(self.NPCL,text = "Talents: ",bg = 'white')
		self.Equipment = tk.Label(self.NPCL,text = "Equipment: ",bg = 'white')
		self.Abilities = tk.Label(self.NPCL,text = "Abilities: ",bg = 'white')

		self.Adversary.place(relx = 0,rely = 0,relwidth = .5,relheight = .2)
		self.Level.place(relx = .5,rely = 0,relwidth = .5,relheight = .2)
		self.Brawn.place(relx = 0,rely = .2,relwidth = .16,relheight = .2)
		self.Agle.place(relx = .16,rely = .2,relwidth = .17,relheight = .2)
		self.Intel.place(relx = .33,rely = .2,relwidth = .17,relheight = .2)
		self.Cun.place(relx = .5,rely = .2,relwidth = .17,relheight = .2)
		self.Will.place(relx = .67,rely = .2,relwidth = .17,relheight = .2)
		self.Pres.place(relx = .84,rely = .2,relwidth = .16,relheight = .2)
		self.Soak.place(relx = 0,rely = .4,relwidth = .3,relheight = .2)
		self.Thresh.place(relx = .3,rely = .4,relwidth = .4,relheight = .2)
		self.Defence.place(relx = .7,rely = .4,relwidth = .3,relheight = .2)

		self.Talents.place(relx = 0,rely = .6,relwidth = .5,relheight = .2)
		self.Abilities.place(relx = .5,rely = .6,relwidth = .5,relheight = .2)

		self.Equipment.place(relx = 0,rely = .8,relwidth = 1,relheight = .2)
		
		self.NPCL.place(relx = .6,rely = 0,relwidth = .3,relheight = .3)

	def updateNPC(self):
		self.Adversary.configure(text = "Type: "+self.NPC["Adversary"])
		self.Level.configure(text = "Lvl: "+self.NPC["Level"])
		self.Brawn.configure(text = str(self.NPC["Brawn"])+"\nBrawn")
		self.Agle.configure(text = str(self.NPC["Agility"])+"\nAgility")
		self.Intel.configure(text = str(self.NPC["Int"])+"\nIntellect")
		self.Cun.configure(text = str(self.NPC["Cun"])+"\nCunning")
		self.Will.configure(text = str(self.NPC["Will"])+"\nWillpower")
		self.Pres.configure(text = str(self.NPC["Presence"])+"\nPresence")
		self.Soak.configure(text = "Soak: "+str(self.NPC["Soak"]))
		self.Thresh.configure(text = "Treshold: "+str(self.NPC["Thresh"]))
		self.Defence.configure(text = "Defence: "+self.NPC["Defence"])
		string = "Talents: "
		for i in self.NPC["Talents"]:
			string += (i+", ")
		self.Talents.configure(text=string)

		string = "Abilities: "
		for i in self.NPC["Abilities"]:
			string += (i+", ")
		self.Abilities.configure(text=string)

		string = "Equipment: "
		for i in self.NPC["Equipment"]:
			string += (i+", ")
		self.Equipment.configure(text=string)



	def printchar(self):

		self.CharL = tk.Frame(self.master)

		self.Name = tk.Label(self.CharL,text = "Name: ",bg = 'white')
		self.Race = tk.Label(self.CharL,text = "Race: ",bg = 'white')
		self.Gender = tk.Label(self.CharL,text = "Gender: ",bg = 'white')
		self.Faction = tk.Label(self.CharL,text = "Faction: ",bg = 'white')
		self.Age = tk.Label(self.CharL,text = "Age: ",bg = 'white')
		self.Height = tk.Label(self.CharL,text = "Height: ",bg = 'white')
		self.Skincolor = tk.Label(self.CharL,text = "Skincolor: ",bg = 'white')
		self.Eyecolor = tk.Label(self.CharL,text = "Eyecolor: ",bg = 'white')
		self.Haircolor = tk.Label(self.CharL,text = "Haircolor: ",bg = 'white')
		self.Traits = tk.Label(self.CharL,text = "Traits: ",bg = 'white')

		self.Name.place(relx = 0,rely = 0,relwidth = .5,relheight = .16)
		self.Faction.place(relx = .5,rely = 0,relwidth = .5,relheight = .16)
		self.Race.place(relx = 0,rely = .16,relwidth = .5,relheight = .17)
		self.Gender.place(relx = .5,rely = .16,relwidth = .5,relheight = .17)
		self.Age.place(relx = 0,rely = .33,relwidth = .5,relheight = .17)
		self.Height.place(relx = .5,rely = .33,relwidth = .5,relheight = .17)
		self.Skincolor.place(relx = 0,rely = .50,relwidth = .5,relheight = .17)
		self.Eyecolor.place(relx = 0,rely = .67,relwidth = .5,relheight = .17)
		self.Haircolor.place(relx = 0,rely = .84,relwidth = .5,relheight = .16)
		self.Traits.place(relx = .5,rely = .50,relwidth = .5,relheight = .50)

		self.CharL.place(relx = .2,rely = 0,relwidth = .3,relheight = .3)


	def updatechar(self):
		self.Name.configure(text = "Name: "+self.NPC["Name"])
		self.Faction.configure(text = "Faction: "+self.NPC["Faction"])
		self.Race.configure(text = "Race: "+self.NPC["Race"])
		self.Gender.configure(text = "Gender: " +self.NPC["Gender"])
		self.Age.configure(text = "Age: " + str(self.NPC["Age"]))
		self.Height.configure(text = "Height: "+str(self.NPC["Height"])+"m")
		self.Skincolor.configure(text = "Skincolor: "+self.NPC["skincolor"])
		self.Eyecolor.configure(text = "Eyecolor: "+self.NPC["eyecolor"])
		self.Haircolor.configure(text = "Haircolor: "+ self.NPC["haircolor"])
		traitsstring = "Traits: "
		for i in self.NPC["Traits"]:
			traitsstring += (i+"\n")
		self.Traits.configure(text=traitsstring)
		#self.Traits.place(relx = .5,rely = .38,relwidth = .5,relheight = .48)



	def placeOptions(self):

		NPC.initNPC()

		self.factions = NPC.getfactions()

		self.races = NPC.getraces()


		self.advesaries = NPC.getadv()

		self.FacV = tk.StringVar()
		self.advV = tk.StringVar()
		self.RaceV = tk.StringVar()

		self.FacV.set("None")
		self.advV.set("None")
		self.RaceV.set("Random")

		self.OptionsF = tk.Frame(self.master)

		self.new = tk.Button(self.OptionsF,text = 'new NPC',command = self.MakeNPC)

		self.FacO = tk.OptionMenu (self.OptionsF,self.FacV, *self.factions)
		self.advO = tk.OptionMenu (self.OptionsF,self.advV, *self.advesaries)
		self.RaceO = tk.OptionMenu (self.OptionsF,self.RaceV,"Random", *self.races)

		self.FacL = tk.Label(self.OptionsF,text = "Faction",bg = 'white')
		self.advL = tk.Label(self.OptionsF,text = "advesaries",bg = 'white')
		self.RaceL = tk.Label(self.OptionsF,text = "Race:",bg = 'white')

		self.FacL.place(relx = 0,rely = 0,relwidth = .25,relheight = .25)
		self.FacO.place(relx = .25,rely = 0,relwidth = .75,relheight = .25)

		self.advL.place(relx = 0,rely = .25,relwidth = .25,relheight = .25)
		self.advO.place(relx = .25,rely = .25,relwidth = .75,relheight = .25)

		self.RaceL.place(relx = 0,rely = .5,relwidth = .25,relheight = .25)
		self.RaceO.place(relx = .25,rely = .5,relwidth = .75,relheight = .25)

		self.new.place(relx = 0,rely = .75,relwidth = 1,relheight = .25)



		self.OptionsF.place(relx = 0,rely = 0,relwidth = .2,relheight = .2)
		
	def MakeNPC(self):
		self.NPC = NPC.createNPC(self.FacV.get(),self.RaceV.get(),self.advV.get())
		self.updatechar()
		self.updateNPC()

	def saveNPC(self):
		name = self.entries.get()
		File = ""
		Dir = "./NPC"
		Files = os.listdir(Dir)
		if name+".NPC" in Files:
			open(Dir+"/"+name+".npc",'w').close()
		File = open(Dir+"/"+name+".npc", 'a+')

		x = json.dumps(self.NPC)
		
		File.write(x)
		File.close()
		self.savefiles = get_saves()
		self.options.place_forget()
		self.options = tk.OptionMenu(self.loadandsave, self.variable, *self.savefiles)
		self.options.place(relx = 0,rely = .5,relheight = .5,relwidth = .5)

	def loadNPC(self):
		name = self.variable.get()
		File = ""
		Dir = "./NPC"
		Files = os.listdir(Dir)

		if name+".npc" in Files:
			oldjs = open(Dir+"/"+name+".npc", 'r').read()
			self.NPC = json.loads(oldjs)
		self.updatechar()
		self.updateNPC()












def get_saves():
	File = ""
	Dir = "./rooms"
	Files = os.listdir(Dir)
	filelist = []
	for i in Files:
		filelist.append(i.split(".",1)[0])
		#print(filelist[-1])
	return(filelist)



def close_window():
  global r
  r.destroy()
  print "Window closed"

NPC.initNPC()

r = tk.Tk()
r.protocol("WM_DELETE_WINDOW", close_window) 

MainWindow(r)
r.mainloop()