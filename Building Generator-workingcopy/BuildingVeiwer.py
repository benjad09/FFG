import Tkinter as tk
import BuildingBuilder2 as build
from Tkinter import *
import random
from random import randint
import os
global r

class MainWindow:
	def __init__(self,master):

		self.master = master

		self.master.state('zoomed')

		self.master.title("Building Veiwer")

		self.master.geometry("750x500") #You want the size of the app to be 750x500
		
		#self.canvas.place(relx = 0,rely = 0,relwidth = 1,relheight = 1)

		self.xsize = 50
		self.ysize = 30
		self.scale = 20
		self.offset = 10
		self.minsize = 2
		self.maxsize = 7

		self.x_size = tk.StringVar(self.master)
		self.y_size = tk.StringVar(self.master)
		self.scale_str = tk.StringVar(self.master)
		self.min_size = tk.StringVar(self.master)
		self.max_size = tk.StringVar(self.master)
		self.x_size.set(str(self.xsize))
		self.y_size.set(str(self.ysize))
		self.scale_str.set(str(self.scale))
		self.min_size.set(str(self.minsize))
		self.max_size.set(str(self.maxsize))





		
		self.building = build.building()
		self.building.generate(self.xsize,self.ysize,self.minsize,self.maxsize)
		#self.building.loadbuilding("test")

		self.canvas = tk.Canvas(self.master)#,height=self.ysize*self.scale+2*self.offset, width=self.xsize*self.scale+2*self.offset, bg="white")
		#self.canvas.place(relx=.25,rely=0)
		self.canvas.place(relx=.2,rely=0,relwidth=.8,relheight = 1)

		self.createbuilding()

		self.new = tk.Button(text = 'new_building',command = self.new_building)

		self.new.place(relx = 0,rely = 0,relheight = .1,relwidth = .2)

		self.loadandsave = tk.Frame(self.master)
		self.save = tk.Button(self.loadandsave,text = "save",command = self.savebuilding)
		self.save.place(relx = 0,rely = 0,relheight = .5,relwidth = .5)
		self.entries = tk.Entry(self.loadandsave)
		self.entries.place(relx = .5,rely = 0,relheight = .5,relwidth = .5)
		self.variable = tk.StringVar(self.master)
		self.savefiles = get_saves()
		self.options = tk.OptionMenu(self.loadandsave, self.variable, *self.savefiles)
		self.loading = tk.Button(self.loadandsave,text = "Load",command = self.loadbuilding)
		self.options.place(relx = 0,rely = .5,relheight = .5,relwidth = .5)
		self.loading.place(relx = .5,rely = .5,relheight = .5,relwidth = .5)
		self.loadandsave.place(relx = 0,rely = .1,relwidth = .2,relheight = .1)
		#self.building.savebuilding("test")

		self.x_size = tk.StringVar(self.master)
		self.y_size = tk.StringVar(self.master)
		self.scale_str = tk.StringVar(self.master)
		self.min_size = tk.StringVar(self.master)
		self.max_size = tk.StringVar(self.master)
		self.x_size.set(str(self.xsize))
		self.y_size.set(str(self.ysize))
		self.scale_str.set(str(self.scale))
		self.min_size.set(str(self.minsize))
		self.max_size.set(str(self.maxsize))

		self.buldingsettings = tk.Frame(self.master)
		self.xl = tk.Label(self.buldingsettings,text = "xdim: "+self.x_size.get(),bg = 'white')
		self.yl = tk.Label(self.buldingsettings,text = "ydim: "+self.y_size.get(),bg = 'white')
		self.sl = tk.Label(self.buldingsettings,text = "Scale: "+self.scale_str.get(),bg = 'white')
		self.minl = tk.Label(self.buldingsettings,text = "Min Room: "+self.min_size.get(),bg = 'white')
		self.maxl = tk.Label(self.buldingsettings,text = "Max Room: "+self.max_size.get(),bg = 'white')
		self.xe = tk.Entry(self.buldingsettings,textvariable = self.x_size)
		self.ye = tk.Entry(self.buldingsettings,textvariable = self.y_size)
		self.se = tk.Entry(self.buldingsettings,textvariable = self.scale_str)
		self.mine = tk.Entry(self.buldingsettings,textvariable = self.min_size)
		self.maxe = tk.Entry(self.buldingsettings,textvariable = self.max_size)

		self.xe.bind("<Return>",self.enterentry)
		self.ye.bind("<Return>",self.enterentry)
		self.se.bind("<Return>",self.enterentry)
		self.mine.bind("<Return>",self.enterentry)
		self.maxe.bind("<Return>",self.enterentry)

		self.xl.place(relx = 0,rely = 0,relwidth = .5,relheight = .2)
		self.xe.place(relx = .5,rely = 0,relwidth = .5,relheight = .2)
		self.yl.place(relx = 0,rely = .2,relwidth = .5,relheight = .2)
		self.ye.place(relx = .5,rely = .2,relwidth = .5,relheight = .2)
		self.sl.place(relx = 0,rely = .4,relwidth = .5,relheight = .2)
		self.se.place(relx = .5,rely = .4,relwidth = .5,relheight = .2)
		self.minl.place(relx = 0,rely = .6,relwidth = .5,relheight = .2)
		self.mine.place(relx = .5,rely = .6,relwidth = .5,relheight = .2)
		self.maxl.place(relx = 0,rely = .8,relwidth = .5,relheight = .2)
		self.maxe.place(relx = .5,rely = .8,relwidth = .5,relheight = .2)
		self.buldingsettings.place(relx = 0,rely = .2,relwidth = .2,relheight = .25)


	def enterentry(self,event):
		self.xsize = int(self.xe.get())
		self.ysize = int(self.ye.get())
		self.scale = int(self.se.get())
		self.offset = 10
		self.minsize = int(self.mine.get())
		self.maxsize = int(self.maxe.get())
		self.xl.configure(text = "xdim: "+self.x_size.get())
		self.yl.configure(text = "ydim: "+self.y_size.get())
		self.sl.configure(text = "Scale: "+self.scale_str.get())
		self.minl.configure(text = "Min Room: "+self.min_size.get())
		self.maxl.configure(text = "Max Room: "+self.max_size.get())
		self.createbuilding()
		pass

	def loadbuilding(self):
		string = self.variable.get()
		self.building.loadbuilding(string)
		self.createbuilding()
		

	def savebuilding(self):
		string = self.entries.get()
		self.building.savebuilding(string)
		self.savefiles = get_saves()
		self.options.place_forget()
		self.options = tk.OptionMenu(self.loadandsave, self.variable, *self.savefiles)
		self.options.place(relx = 0,rely = .5,relheight = .5,relwidth = .5)



	def createbuilding(self):
		
		self.canvas.delete("all")

		self.rooms = self.building.getrooms()
		for i in self.rooms:
			self.placeroom(i,self.scale)
		self.drawbuilding()

		
		

	
	def new_building(self):
		self.building = 0
		#print(building)
		self.building = build.building()
		self.building.generate(self.xsize,self.ysize,2,7)
		self.createbuilding()


	def drawbuilding(self):
		self.hotzwalls = self.building.gethorzwall()
		self.vertwalls = self.building.getvertwall()
		for i in range(0,len(self.hotzwalls)):
			for j in range(0,len(self.hotzwalls[i])):

				if (self.hotzwalls[i][j]==1):
					colorr = "black"
					enf  =  1
					place = 1
				elif (self.hotzwalls[i][j]==2):
					colorr = "red"
					enf = 2
					place = 1
				elif (self.hotzwalls[i][j]==3):
					colorr = "blue"
					enf = 2
					place = 1
				else:
					colorr = "grey"
					enf  =  1
					place = 0
				if place:
					self.canvas.create_line(j*self.scale+self.offset,i*self.scale+self.offset,j*self.scale+self.offset,i*self.scale+self.scale+self.offset,fill=colorr,width=enf)
				
		for i in range(0,len(self.vertwalls)):
			for j in range(0,len(self.vertwalls[i])):
				if (self.vertwalls[i][j]==1):
					colorr = "black"
					enf  =  1
					place = 1
				elif (self.vertwalls[i][j]==2):
					colorr = "red"
					enf = 2
					place = 1
				elif (self.vertwalls[i][j]==3):
					colorr = "blue"
					enf = 2
					place = 1
				else:
					colorr = "grey"
					enf = 1
					place = 0
				if place:
					self.canvas.create_line(j*self.scale+self.offset,i*self.scale+self.offset,j*self.scale+self.offset+self.scale,i*self.scale+self.offset,fill=colorr,width=enf)
	def placeroom(self,i,s):
		red = str(randint(0,7))
		green  = str(randint(0,7))
		blue = str(randint(0,7))
		colorr = '#'+red+green+blue
		colorr = "#fff"
		colorr = '#'+red+red+red
		#print(colorr)
		self.canvas.create_polygon(i[0]*s+self.offset,i[1]*s+self.offset,(i[0]+i[2])*s+self.offset,i[1]*s+self.offset,(i[0]+i[2])*s+self.offset,(i[1]+i[3])*s+self.offset,(i[0])*s+self.offset,(i[1]+i[3])*s+self.offset,fill = colorr)

def get_saves():
	File = ""
	Dir = "./buildings"
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
