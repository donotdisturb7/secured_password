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
        a = ""
        # ajouter des élements aux tabs

        text_var = tk.StringVar(value=a)
        self.label = customtkinter.CTkLabel(master=self.tab("Home"), textvariable=text_var, width=900, height=900, corner_radius=10)
        self.label.grid(row=0, column=0, padx=20, pady=20)

        text_var = tk.StringVar(value=a)
        self.label = customtkinter.CTkLabel(master=self.tab("Generer un mot de passe"), textvariable=text_var, width=900, height=900)
        self.label.grid(row=0, column=0, padx=20, pady=20)

        #text_var = tk.StringVar(value=a)
        self.label = customtkinter.CTkLabel(master=self.tab("Mes mots de passes"), textvariable=text_var, width=900, height=900)
        self.label.grid(row=0, column=0, padx=20, pady=20)
        self.password_entry = customtkinter.CTkEntry(master=self.tab("Generer un mot de passe"), placeholder_text="Votre mot de passe sécurisé", width=150, height=25)
        
        self.password_entry.grid(row=0, column=0, padx=5, pady=10)
        self.button = customtkinter.CTkButton(master=self.tab("Generer un mot de passe"), text="Generer", command=self.generate_password)  # command=generate_password)
        self.button.place(relx=0.2, rely=0.5, anchor=tk.CENTER)
    
    def generate_password(self):
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=8))  # k= nbr_char))
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, password)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Secured Password ")
        self.geometry("900x900")
        # self.minsize(900, 900)
        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=0, padx=0, pady=0)


app = App()
app.mainloop()
