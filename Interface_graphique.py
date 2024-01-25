#importe la librairie Tkinter

from tkinter import *
import customtkinter

#création de la fenêtre
page = customtkinter.CTk()

page.geometry("300x400")

boutton = customtkinter.CTkButton(master=page, texte="Bonjour")
boutton.place(dx=0.5, dy=0.5, ancre =CENTER)
page.mainloop()
