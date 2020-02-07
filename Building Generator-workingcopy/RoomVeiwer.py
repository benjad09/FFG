import Tkinter as tk
import RoomBuilder as build
from Tkinter import *
import random
from random import randint
from PIL import Image, ImageTk
import os
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

		self.ceateroom()



		load = Image.open("./Assets/barfront.png")
		render = ImageTk.PhotoImage(load)
		img = Label(self.master,image = render)
		img.image = render


		self.canvas.create_image(50,50,anchor=NW,image=render)
		#self.canvas.create_image(10,50,anchor=NW,image=render)
		# load2 = Image.open("./Assets/barfront.png")
		# load2 = load2.rotate(90)
		# render2 = ImageTk.PhotoImage(load2)
		load = Image.open("./Assets/barfront.png")
		
		load = load.rotate(270)
		render = ImageTk.PhotoImage(load)
		img = Label(self.master,image = render)
		img.image = render
		
		self.canvas.create_image(10,10,anchor=NW,image=render)


		load = Image.open("./Assets/barleft.png")
		render = ImageTk.PhotoImage(load)
		img = Label(self.master,image = render)
		img.image = render
		
		#self.canvas.create_image(90,50,anchor=NW,image=render)
		self.canvas.create_image(10,50,anchor=NW,image=render)






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


def close_window():
  global r
  r.destroy()
  print "Window closed"

r = tk.Tk()
r.protocol("WM_DELETE_WINDOW", close_window) 

MainWindow(r)
r.mainloop()
