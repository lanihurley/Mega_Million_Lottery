"""
Program: megalotteryGUI.py
Author: Lani Hurley 11/19/2021

simple program that will replicate the New York Lottery "Mega Millions" number draw.
The program  "draws" five random numbers between 1 and 70.
It also has a special, "Mega Ball" number which is only between 1 and 25.

*** NOTE: the file "breezypythongui.py" MUST be in the same directory as the file for the application to work.***
**** NOTE: NEED IMAGE FILE: "logo-megamillions.png". MUST be in the same directory as the file for the application to work.***
*** NOTE: Need to have .wav file: "clicksound.wav". MUST be in the same directory as the file for the application to work.***
*** NOTE: MUST install the pygame package by running: pip install pygame

"""
from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font
import pygame
import random

class MegaLotteryGUI(EasyFrame):

	def __init__(self):
		"""Sets up the window and the widgets."""
		EasyFrame.__init__(self, title = "MEGA MILLIONS ONLINE LOTTERY - NEW YORK", width = 820, height = 700, background = "#328ace", resizable = False)
		# Title label
		self.imageLabel = self.addLabel(text = "", row = 0, column = 0, columnspan = 6, background = "#0060a7")
		# Load the image and associate it with the image label
		self.image = PhotoImage(file = "logo-megamillions.png")
		self.imageLabel["image"] = self.image
		
		self.addLabel(text = "MEGA BALL", row = 1, column = 5, sticky = "NSWE", font = Font(family = "Impact", size = 25), background = "#1c4d8c", foreground = "white")
		self.addLabel(text = "LOTTERY NUMBERS", row = 1, column = 2, columnspan = 3, font =Font(family = "Impact"), background = "#328ace")
		# Fields for the random numbers to appear
		self.numField1 = self.addIntegerField(value = 0, width = 8, row = 2, column = 0, sticky = "NSEW")
		self.numField2 = self.addIntegerField(value = 0, width = 8, row = 2, column = 1, sticky = "NSEW")
		self.numField3 = self.addIntegerField(value = 0, width = 8, row = 2, column = 2, sticky = "NSEW")
		self.numField4 = self.addIntegerField(value = 0, width = 8, row = 2, column = 3, sticky = "NSEW")
		self.numField5 = self.addIntegerField(value = 0, width = 8, row = 2, column = 4, sticky = "NSEW")
		self.numField6 = self.addIntegerField(value = 0, row = 2, column = 5, sticky = "NSEW")
		self.numField6["background"]  = "yellow"

		# add draw  button
		self.playButton = self.addButton(text = "Click to Draw\nNumbers", row = 3, column = 5, command = self.NumDraw)
		self.playButton["font"] = "Impact"
		self.playButton["padx"] = "15"
		self.playButton["foreground"] = "#1c4d8c"
	
	# Event Handling Method
	def NumDraw(self):
		# adding the sound to button
		pygame.mixer.init()
		pygame.mixer.music.load("clicksound.wav")
		pygame.mixer.music.play(loops = 0)

		# Variables and constants 
		num1 = random.randint(1, 70)
		num2 = random.randint(1, 70)
		num3 = random.randint(1, 70)
		num4 = random.randint(1, 70)
		num5 = random.randint(1, 70)
		num6 = random.randint(1, 25)

		# Output phase
		self.numField1.setNumber("%18d" % num1)
		self.numField2.setNumber("%18d" % num2)
		self.numField3.setNumber("%18d" % num3)
		self.numField4.setNumber("%18d" % num4)
		self.numField5.setNumber("%18d" % num5)
		self.numField6.setNumber("%32d" % num6)

		return

# definition of the main() function for program entry
def main():
	"""Instantiates and pops up the window."""
	MegaLotteryGUI().mainloop()
# global call to trigger the main() function
if __name__ == "__main__":
	main()