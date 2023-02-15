import tkinter as tk
# import tkinter
from tkinter import END
import customtkinter
import random
import string




# Theme disponibles dans la librairie
# Modes: system (default), light, dark
customtkinter.set_appearance_mode("dark")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("dark-blue")

# creation de la fenêtre
app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.minsize(400, 300)
app.title("Générateur de Mot de Passe sécurisé")


# # function clear
# def clear():
#     password_entry.delete(0, END)


# def clear():
#     dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="Test")
#     return dialog.get_input()

def theme():
    customtkinter.set_appearance_mode("light")


# fontion generation de mot de passe
def generate_password():
    
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=5))#nbr_char))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    nbr_char = int(nbr_char_entry.cget(password))




password_entry = customtkinter.CTkEntry(master=app,placeholder_text="Votre mot de passe sécurisé",width=150,height=25,border_width=2,corner_radius=10)
password_entry.place(relx=0.6, rely=1.5,) #anchor=tkinter.CENTER)


#nbr_char_entry = tk.Entry(app)


#nbr_char_entry.place(relx=0.20, rely=0.7, anchor=tkinter.CENTER)
# password_label.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)
password_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
# generate_button.grid(row=1, columnspan=2, pady=10)


text_var = tk.StringVar(value="CTkLabel")

nbr_char_entry = customtkinter.CTkLabel(master=app,textvariable=text_var,width=120,height=25,fg_color=("white", "gray75"),corner_radius=8)
nbr_char_entry.place(relx=0.5, rely=0.05, anchor=tk.CENTER)
# nbr_char_entry.configure(text = password)


# CTkButton - Pour creer un le bouton qui lance la fonction generate_password
button = customtkinter.CTkButton(master=app, text="Generer",command=theme)
button.place(relx=0.2, rely=0.5, anchor=tk.CENTER)
# buttonclear = customtkinter.CTkButton(master=app, text="clear", command=clear)
# buttonclear.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

# ligne necéssaire pour lancer l'application / la fenetre
app.mainloop()
