import os
import tkinter as tk
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import sqlite3
from tkinter import messagebox

import customtkinter
from PIL import Image
import password


# base de donnée
conn = sqlite3.connect('passwords.db')
c = conn.cursor()
c.execute("SELECT password_id , username, password, website FROM passwords")
results = c.fetchall()


customtkinter.set_appearance_mode("Dark")


def change_theme(new_appearance_mode):
    customtkinter.set_appearance_mode(new_appearance_mode)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("secured password")
        self.geometry("800x550")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # images
        image_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "assets")
        self.logo_image = customtkinter.CTkImage(Image.open(
            os.path.join(image_path, "secure.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")),
                                                       size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")),
                                                       size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(
                                                     image_path, "home_light.png")),
                                                 size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "gen.png")),
                                                 dark_image=Image.open(
                                                     os.path.join(image_path, "gen2.png")),
                                                 size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "mdp.png")),
                                                     dark_image=Image.open(
                                                         os.path.join(image_path, "mdp.png")),
                                                     size=(20, 20))

        # menu navigation
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Secured password",
                                                             image=self.logo_image,
                                                             compound="left",
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                   text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=(
                                                       "gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Générer un Mot de passe",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=(
                                                          "gray70", "gray30"),
                                                      image=self.chat_image, anchor="w",
                                                      command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Mes mots de passes",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=(
                                                          "gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w",
                                                      command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        # menu pour changer de thème
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame,
                                                                values=[
                                                                    "Dark", "Light", "System"],
                                                                command=change_theme)
        self.appearance_mode_menu.grid(
            row=6, column=0, padx=20, pady=20, sticky="s")

        # creation de la frame home
        self.home_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="",
                                                                   image=self.large_test_image)
        self.home_frame_large_image_label.grid(
            row=0, column=0, padx=20, pady=10)

        self.home_frame_button_1 = customtkinter.CTkButton(
            self.home_frame, text="", image=self.image_icon_image)
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="CTkButton",
                                                           image=self.image_icon_image, compound="right")
        self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="CTkButton",
                                                           image=self.image_icon_image, compound="top")
        self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.home_frame_button_4 = customtkinter.CTkButton(self.home_frame, text="CTkButton",
                                                           image=self.image_icon_image, compound="bottom", anchor="w")
        self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

        # creation de la frame2
        self.second_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)

        self.entry_password = customtkinter.CTkEntry(
            master=self.second_frame, width=300)

        self.entry_password.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        self.btn_generate = customtkinter.CTkButton(master=self.second_frame, text="Generer un mot de passe", width=100,
                                                    command=self.set_password)
        self.btn_generate.place(relx=0.2, rely=0.5, anchor=tk.CENTER)

        self.password_length_slider = customtkinter.CTkSlider(master=self.second_frame, from_=4, to=30,
                                                              number_of_steps=30,
                                                              command=self.slider_event)

        self.password_length_slider.place(relx=0.50, rely=0.18, anchor=tk.CENTER)

        self.password_length_entry = customtkinter.CTkEntry(
            master=self.second_frame, width=50)

        self.password_length_entry.place(relx=0.1, rely=0.1, anchor=tk.CENTER)

        self.cb_digits_var = tk.StringVar()

        self.cb_digits = customtkinter.CTkCheckBox(master=self.second_frame, text="0-9",
                                                   variable=self.cb_digits_var, onvalue=digits, offvalue="")
        self.cb_digits.grid(row=2, column=0, padx=10)

        self.cb_lower_var = tk.StringVar()
        self.cb_lower = customtkinter.CTkCheckBox(master=self.second_frame, text="a-z", variable=self.cb_lower_var,
                                                  onvalue=ascii_lowercase, offvalue="")
        self.cb_lower.grid(row=2, column=1)

        self.cb_upper_var = tk.StringVar()
        self.cb_upper = customtkinter.CTkCheckBox(master=self.second_frame, text="A-Z", variable=self.cb_upper_var,
                                                  onvalue=ascii_uppercase, offvalue="")
        self.cb_upper.grid(row=2, column=2)

        self.cb_symbols_var = tk.StringVar()
        self.cb_symbols = customtkinter.CTkCheckBox(master=self.second_frame, text="@#$%", variable=self.cb_symbols_var,
                                                    onvalue=punctuation, offvalue="")
        self.cb_symbols.grid(row=2, column=3)

        # creation de la frame3
        self.third_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")

        # frame par défaut
        self.change_frame("home")

        # bouton ajouter la bd dans la textbox
        self.btn_geenerate = customtkinter.CTkButton(master=self.second_frame, text="Enregistrer le mot de passe", width=100,
                                                     command=self.put)
        self.btn_geenerate.place(relx=0.2, rely=0.7, anchor=tk.CENTER)

        # bouton actualiser
        self.bt_reload = customtkinter.CTkButton(master=self.third_frame, text="Actualiser la liste des mots de passse", width=100,
                                                    command=self.reload_text)
        self.bt_reload.place(relx=0.49, rely=0.4, anchor=tk.CENTER)
        
        
        # bouton cacher la liste de mot de passe
        self.bt_hide = customtkinter.CTkButton(master=self.third_frame, text="Cacher la liste des mots de passe", width=100,
                                                    command=self.toggle_hide)
        self.bt_hide.place(relx=0.49, rely=0.49, anchor=tk.CENTER)
        
        #bouton supprimer un mot de passe
        self.btn_sup = customtkinter.CTkButton(master=self.third_frame, text="Supprimer le mot de passe ",
                                                    command=self.delete_row)
        self.btn_sup.place(relx=0.85, rely=0.7, anchor=tk.CENTER)

        self.textbox = customtkinter.CTkTextbox(
            master=self.third_frame, width=1200,corner_radius=5, border_width=1,scrollbar_button_color='red')
        self.textbox.grid(row=1, column=2, sticky="nsew")

        self.username_db = customtkinter.CTkEntry(
            master=self.second_frame, width=100)
        self.username_db.place(relx=0.5, rely=0.20)
        self.website_db = customtkinter.CTkEntry(
            master=self.second_frame, width=100)
        self.website_db.place(relx=0.5, rely=0.40)
        
        
        self.text_inserer =  tk.StringVar(value="Inserez l'Id du mot de passe que vous voulez supprimer")
        self.label_1 = customtkinter.CTkLabel(master=self.third_frame,textvariable=self.text_inserer,width=120,
                               height=1,    font=customtkinter.CTkFont("Helvetica", -9))
        self.label_1.place(relx=0.01, rely=0.62)
        
        self.text_website =  tk.StringVar(value="Inserez le site auquelle votre mot de passe appartient (non obligatoire)")
        self.label_1 = customtkinter.CTkLabel(master=self.second_frame,textvariable=self.text_website,width=120,
                               height=1,    font=customtkinter.CTkFont("Helvetica", -9))
        self.label_1.place(relx=0.01, rely=0.65)
        
        self.text_username =  tk.StringVar(value="Inserez un username")
        self.label_1 = customtkinter.CTkLabel(master=self.second_frame,textvariable=self.text_username,width=120,
                               height=1,    font=customtkinter.CTkFont("Helvetica", -9))
        self.label_1.place(relx=0.01, rely=0.62)
        
       

        # ce code va inserer dans la textbox les element de la bd result [0] pour username ainsi de suite
        for result in results:
            self.textbox.insert(
                tk.END, f"{result[0]}: {result[1]}: ,{result[2]}: {result[3]} \n")

        self.textbox.configure(state="normal")
        
        self.password_id_entry = customtkinter.CTkEntry(master=self.third_frame)
        self.password_id_entry.place(relx=0.4, rely=0.60)



    # le slide pour choisir le nombre de charactere du mdp

    def slider_event(self, value):
        self.password_length_entry.delete(0, 'end')
        self.password_length_entry.insert(0, int(value))

    def get_characters(self):
        chars = "".join(self.cb_digits_var.get() + self.cb_lower_var.get()
                        + self.cb_upper_var.get() + self.cb_symbols_var.get())
        return chars

    def set_password(self):
        "fonction qui va afficher le mot de passe cree avec 'password.py' en prenant la valeur du slider comme length"
        self.entry_password.delete(0, 'end')
        return self.entry_password.insert(0, password.create_new(length=int(self.password_length_slider.get()),
                                                          characters=self.get_characters()))
        

    def change_frame(self, name):
        self.home_button.configure(
            fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(
            fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(
            fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # selection des frames
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
            
    # fonction de qui permet d'ajouter les entry username_db password_db et website_db a la basse de donne passwords.db
    def put(self):

        self.username = str(self.username_db.get())
        self.password = str(self.entry_password.get())
        self.website = str(self.website_db.get())
        if len(self.username) == 0 or len(self.password) == 0 :
            return messagebox.showwarning("Attention", "Vous devez d'abord generer un mot de passe et inserer un username afin de pouvoir enregistrer votre mot de passe ")
        else:
            c.execute("INSERT INTO passwords (username, website, password) VALUES (?, ?, ?)",
                    (self.username, self.website, self.password))
            conn.commit()
            a = c.fetchall()
            self.textbox.insert(tk.END,a)
            

    def home_button_event(self):
        self.change_frame("home")

    def frame_2_button_event(self):
        self.change_frame("frame_2")

    def frame_3_button_event(self):
        self.change_frame("frame_3")
        
        
    #foncton actualiser textbox
    def reload_text(self):
        c = conn.cursor()
        c.execute("SELECT password_id, username, website, password FROM passwords")
        data = c.fetchall()
        c.close()

        self.textbox.delete('1.0', 'end')
        for row in data:
            self.textbox.insert(tk.END, f"ID = {row[0]}; USERNAME = {row[1]}; WEBSITE = {row[2]};  PASSWORD = {row[3]} \n")
            
    
        
    def delete_row(self):

        self.id = self.password_id_entry.get()
        
        conn = sqlite3.connect('passwords.db')
        c = conn.cursor()
        c.execute("SELECT * FROM passwords WHERE password_id=?", (self.id,))
        row = c.fetchone()
        if row:
            c.execute("DELETE FROM passwords WHERE password_id=?", (self.id,))
            conn.commit()
            messagebox.showwarning("Succès", "Le mot de passe contenant l'id '{}' a été supprimer avec succès.".format(self.id))
            conn.close()
            
            
        else:
            messagebox.showwarning("Id non trouvé", "L'id '{}' n'a pas été trouvé dans la base de donné.".format(self.id))
        conn.close()
        
    def toggle_hide(self):

        if self.textbox:
            
            self.textbox.delete("1.0", tk.END)
            self.textbox.insert(tk.END, hidden_text)
            self.textbox = False
        else:
            hidden_text = textbox.get("1.0", tk.END)
            self.textbox.delete("1.0", tk.END)
            self.masked_text = "*" * len(hidden_text)
            self.textbox.insert(tk.END, masked_text)
            self.textbox= True


# lancement
if __name__ == "__main__":
    app = App()
    app.mainloop()
