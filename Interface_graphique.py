#importe la librairie Tkinter

from tkinter import *
import customtkinter

#création de la fenêtre
page = customtkinter.CTk()

#Création de la fenêtre
x=640
y=480
fenetre = pygame.display.set_mode((x, y))

#Variable qui continue la boucle si = 1, stoppe si = 0
continuer = 1
