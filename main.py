import customtkinter
import tkinter as tk
from tkinter import *
import string
import random

customtkinter.set_appearance_mode("dark")


class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # creation des tabs
        self.add("Home")
        self.add("Generer un mot de passe")
        self.add("Mes mots de passes")
        # ajouter des élements aux tabs

        text_var = tk.StringVar(value=0)
        self.label1 = customtkinter.CTkLabel(master=self.tab("Home"), corner_radius=10,width=900, height=900)#textvariable=text_var, 
        self.label1.grid(row=0, column=0, padx=20, pady=20)

#width=900, height=900
        self.label2 = customtkinter.CTkLabel(master=self.tab("Generer un mot de passe"), textvariable=text_var,width=900, height=900)
        self.label2.grid(row=0, column=0, padx=20, pady=20)

        self.label3 = customtkinter.CTkLabel(master=self.tab("Mes mots de passes"), textvariable=text_var,width=900, height=900)
        self.label3.grid(row=0, column=0, padx=20, pady=20)
        self.password_entry = customtkinter.CTkEntry(master=self.tab("Generer un mot de passe"), placeholder_text="Votre mot de passe sécurisé", width=150, height=25)
        
        self.password_entry.grid(row=0, column=0, padx=5, pady=10)
        self.button = customtkinter.CTkButton(master=self.tab("Generer un mot de passe"), text="Generer", command=self.generate_password)  # command=generate_password)
        self.button.place(x=155,y=455)
        
     

        self.entry1 = customtkinter.CTkEntry(master=self.tab("Generer un mot de passe"),textvariable=text_var,width=120,height=25,fg_color=("white", "gray75"),corner_radius=8)
        self.entry1.place(x=155,y=160)









    def generate_password(self):
        password_length = self.entry1.get()
        self.label = customtkinter.CTkLabel(master = self.tab("Generer un mot de passe"))#,text="Hello, world!", fg_color="white")
        if not password_length:
        # si l'utilisateur n'a rien saisi, afficher un message d'erreur
            self.label.configure(text="Veuillez saisir une longueur de mot de passe valide")#,fg_color="white")
            self.label.grid(row=0, column=0)
        else:
            password_length = int(password_length)
            password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length))
            #self.label.configure(text = "password")
            self.password_entry.delete(0, END)
            self.password_entry.insert(0, password)



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Secured Password ")
        #self.geometry("900")
        self.minsize(400, 400)
        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=0, padx=0, pady=0)

app = App()
app.mainloop()
