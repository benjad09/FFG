import Tkinter as tk
import RoomBuilder as build
from Tkinter import *
import random
from random import randint
from PIL import Image, ImageTk
import os
import json
global r

class MainWindow:
	def __init__(self,master):

		self.master = master

		self.master.state('zoomed')

		self.master.title("room veiwer")

		self.master.geometry("750x500") #You want the size of the app to be 750x500
		
		#self.canvas.place(relx = 0,rely = 0,relwidth = 1,relheight = 1)
		self.assetsize = 40
		self.offset = 10






		

		#self.building.loadbuilding("test")

		self.canvas = tk.Canvas(self.master,bg = "white")#,height=self.ysize*self.scale+2*self.offset, width=self.xsize*self.scale+2*self.offset, bg="white")
		#self.canvas.place(relx=.25,rely=0)
		self.canvas.place(relx=.2,rely=0,relwidth=.8,relheight = 1)

		#self.loadcsv()
		#self.drawroom()
		#self.drawassets()

		self.loadandsave = tk.Frame(self.master)
		self.save = tk.Button(self.loadandsave,text = "save",command = self.saveROOM)
		self.save.place(relx = 0,rely = 0,relheight = .5,relwidth = .5)
		self.entries = tk.Entry(self.loadandsave)
		self.entries.place(relx = .5,rely = 0,relheight = .5,relwidth = .5)
		self.variable = tk.StringVar(self.master)
		self.savefiles = get_saves()
		self.options = tk.OptionMenu(self.loadandsave, self.variable, *self.savefiles)
		self.loading = tk.Button(self.loadandsave,text = "Load",command = self.loadROOM)
		self.options.place(relx = 0,rely = .5,relheight = .5,relwidth = .5)
		self.loading.place(relx = .5,rely = .5,relheight = .5,relwidth = .5)
		self.loadandsave.place(relx = 0,rely = 0,relwidth = .2,relheight = .1)
		self.NPCS = []


		self.face = tk.Frame(self.master)
		self.facev = tk.StringVar(self.master)
		self.facefiles = get_faces()
		self.faceoptions = tk.OptionMenu(self.face, self.facev, *self.facefiles)
		self.faceloading = tk.Button(self.face,text = "Load",command = self.loadface)
		self.faceoptions.place(relx = 0,rely = 0,relwidth = .5,relheight = 1)
		self.faceloading.place(relx = .5,rely = 0,relwidth = .5,relheight = 1)
		self.face.place(relx = 0,rely = .1,relwidth = .2,relheight = .05)

	def loadface(self):
		self.NPCS.append(self.createddragible(self.canvas,self.facev.get(),10,10))


	class createddragible():
		def __init__(self, canvas, asset, xpos, ypos):
			self.canvas = canvas
			self.image_name = asset
			self.xpos, self.ypos = xpos, ypos

			load = Image.open("./Char/"+asset+".png")

			render = ImageTk.PhotoImage(load)
			img = Label(image = render)
			img.image = render

			#self.canvas.create_image(x,y,anchor=NW,image=render)
			self.image_obj= canvas.create_image(xpos,ypos,anchor=NW,image=render)


			canvas.tag_bind(self.image_obj, '<Button1-Motion>', self.move)
			canvas.tag_bind(self.image_obj, '<ButtonRelease-1>', self.release)
			self.move_flag = False

		def move(self, event):
			if self.move_flag:
				new_xpos, new_ypos = event.x, event.y
				difx = new_xpos-self.mouse_xpos
				dify = new_ypos-self.mouse_ypos
				if abs(difx)>40:
					self.canvas.move(self.image_obj,(difx/abs(difx))*40,0)
					self.mouse_xpos += (difx/abs(difx))*40


				if abs(dify)>40:
					self.canvas.move(self.image_obj,0,(dify/abs(dify))*40)
					self.mouse_ypos += (dify/abs(dify))*40


				#self.canvas.move(self.image_obj,new_xpos-self.mouse_xpos ,new_ypos-self.mouse_ypos)

				#
				#self.mouse_ypos = new_ypos
				#self.mouse_xpos = new_xpos
			else:
				self.move_flag = True
				self.canvas.tag_raise(self.image_obj)
				self.mouse_xpos = event.x
				self.mouse_ypos = event.y

		def release(self, event):
			self.move_flag = False


		# self.placeasset(50,10,270,"barfront")
		# self.placeasset(50,50,0,"barleft")
		
		# self.placeasset(90,50,0,"barfront")
		# self.placeasset(130,50,0,"barright")
		# self.placeasset(130,10,90,"barfront")

	def drawroom(self):
		self.canvas.delete("all")
		self.drawassets()
		self.drawwalls()

	def drawassets(self):
		for i in range(0,self.room["ysize"]):
			for j in range(0,self.room["xsize"]):
				if self.room["space"][i][j] != 0:
					split = self.room["space"][i][j].split("#")
					split[1] = int(split[1])
					print(split)
					self.placeasset(j*self.assetsize+self.offset,i*self.assetsize+self.offset,split[1],split[0])





	def placeasset(self,x,y,r,asset):
		load = Image.open("./Assets/"+asset+".png")
			
		load = load.rotate(r)
		render = ImageTk.PhotoImage(load)
		img = Label(self.master,image = render)
		img.image = render
		
		self.canvas.create_image(x,y,anchor=NW,image=render)



	def ceateroom(self):
		
		self.canvas.delete("all")
		send = [[],[]]
		for i in range(0,15):
			send[0].append('w')
			send[1].append('w')
		send2 = []
		for i in range(0,15):
			send2.append(['w','w'])
		self.x = build.advancedroom(send2,send)
		self.x.createspaces()
		self.room = self.x.returnroom()
		self.drawwalls()

	def loadcsv(self):
		self.room = {}
		pullData = open("storage.csv",'r').read()
		self.room["space"] = pullData.split('\n')
		for i in range(0,len(self.room["space"])):
			self.room["space"][i] = self.room["space"][i].split(',')
		
		self.room["space"].pop(-1)
		self.room["space"][0][0] = "0"
		self.room["vertwall"] = [[],[]]
		for i in range(0,len(self.room["space"][0])):
			self.room["vertwall"][0].append('w')
			self.room["vertwall"][1].append('w')
		self.room["xsize"] = len(self.room["space"][0])
		self.room["hotzwall"] = []
		for i in range(0,len(self.room["space"])):
			self.room["hotzwall"].append(['w','w'])	
		self.room["ysize"] = len(self.room["space"])
		
		for i in range(0,self.room["ysize"]):
			for j in range(0,self.room["xsize"]):
				if self.room["space"][i][j] == "0":
					self.room["space"][i][j] = 0



	def drawwalls(self):
		for i in range(0,len(self.room["hotzwall"])):
			if (self.room["hotzwall"][i][0]=='w'):
				colorr = "black"
				enf  =  1
				place = 1
			elif (self.room["hotzwall"][i][0]=='d'):
				colorr = "red"
				enf = 2
				place = 1
			elif (self.room["hotzwall"][i][0]=='v'):
				colorr = "blue"
				enf = 2
				place = 1
			else:
				colorr = "grey"
				enf  =  1
				place = 0
			self.canvas.create_line(self.offset,self.offset+(i)*self.assetsize,self.offset,self.offset+(i+1)*self.assetsize,fill=colorr,width=enf)
			if (self.room["hotzwall"][i][1]=='w'):
				colorr = "black"
				enf  =  1
				place = 1
			elif (self.room["hotzwall"][i][1]=='d'):
				colorr = "red"
				enf = 2
				place = 1
			elif (self.room["hotzwall"][i][1]=='v'):
				colorr = "blue"
				enf = 2
				place = 1
			else:
				colorr = "grey"
				enf  =  1
				place = 0
			self.canvas.create_line(self.offset+self.room["xsize"]*self.assetsize,self.offset+(i)*self.assetsize,self.offset+self.room["xsize"]*self.assetsize,self.offset+(i+1)*self.assetsize,fill=colorr,width=enf)
		for i in range(0,len(self.room["vertwall"][0])):
			if (self.room["vertwall"][0][i]=='w'):
				colorr = "black"
				enf  =  1
				place = 1
			elif (self.room["vertwall"][0][i]=='d'):
				colorr = "red"
				enf = 2
				place = 1
			elif (self.room["vertwall"][0][i ]=='v'):
				colorr = "blue"
				enf = 2
				place = 1
			else:
				colorr = "grey"
				enf  =  1
				place = 0
			self.canvas.create_line(self.offset+(i)*self.assetsize,self.offset,self.offset+(i+1)*self.assetsize,self.offset,fill=colorr,width=enf)
			if (self.room["vertwall"][1][i]=='w'):
				colorr = "black"
				enf  =  1
				place = 1
			elif (self.room["vertwall"][1][i]=='d'):
				colorr = "red"
				enf = 2
				place = 1
			elif (self.room["vertwall"][1][i]=='v'):
				colorr = "blue"
				enf = 2
				place = 1
			else:
				colorr = "grey"
				enf  =  1
				place = 0
			self.canvas.create_line(self.offset+(i)*self.assetsize,self.offset+self.room["ysize"]*self.assetsize,self.offset+(i+1)*self.assetsize,self.offset+self.room["ysize"]*self.assetsize,fill=colorr,width=enf)

	def saveROOM(self):
		name = self.entries.get()
		File = ""
		Dir = "./rooms"
		Files = os.listdir(Dir)
		if name+".room" in Files:
			open(Dir+"/"+name+".room",'w').close()
		File = open(Dir+"/"+name+".room", 'a+')

		x = json.dumps(self.room)
		
		File.write(x)
		File.close()
		self.savefiles = get_saves()
		self.options.place_forget()
		self.options = tk.OptionMenu(self.loadandsave, self.variable, *self.savefiles)
		self.options.place(relx = 0,rely = .5,relheight = .5,relwidth = .5)

	def loadROOM(self):
		name = self.variable.get()
		File = ""
		Dir = "./rooms"
		Files = os.listdir(Dir)
		

		if name+".room" in Files:
			oldjs = open(Dir+"/"+name+".room", 'r').read()
			self.room = json.loads(oldjs)
		
		self.drawroom()











def get_saves():
	File = ""
	Dir = "./rooms"
	Files = os.listdir(Dir)
	filelist = []
	for i in Files:
		filelist.append(i.split(".",1)[0])
		#print(filelist[-1])
	return(filelist)

def get_faces():
	File = ""
	Dir = "./Char"
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

r = tk.Tk()
r.protocol("WM_DELETE_WINDOW", close_window) 

MainWindow(r)
r.mainloop()
