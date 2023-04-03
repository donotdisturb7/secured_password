import tkinter as tk
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import sqlite3
import tkinter.messagebox
import customtkinter
from PIL import Image
import os
import password


# base de donnée
conn = sqlite3.connect('passwords.db')
c = conn.cursor()
c.execute("SELECT username, password, website FROM passwords")
results = c.fetchall()


customtkinter.set_appearance_mode("Dark")


def change_theme(new_appearance_mode):
    customtkinter.set_appearance_mode(new_appearance_mode)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configuration de la fenetre
        self.title("secured password")
        self.geometry("700x550")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # images
        image_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "assets")
        self.logo_image = customtkinter.CTkImage(Image.open(
            os.path.join(image_path, "secure.png")), size=(26, 26))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")),
                                                       size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),dark_image=Image.open(os.path.join(
                                                     image_path, "home_light.png")),
                                                 size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "gen.png")),dark_image=Image.open(
                                                     os.path.join(image_path, "gen2.png")),
                                                 size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "mdp.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "mdp.png")),
                                                     size=(20, 20))

        # menu navigation
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Secured password",image=self.logo_image,compound="left",
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                   text="Home",fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Générer un Mot de passe",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w",command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Mes mots de passes",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w",
                                                      command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        # menu pour changer de thème
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame,
                                                                values=["Dark", "Light", "System"],
                                                                command=change_theme)
        self.appearance_mode_menu.grid(
            row=6, column=0, padx=20, pady=20, sticky="s")

        # creation de la frame home
        self.home_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.second_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)

        self.entry_password = customtkinter.CTkEntry(
            master=self.second_frame, width=300)

        self.entry_password.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        self.btn_generate = customtkinter.CTkButton(master=self.second_frame, text="Generer", width=100,
                                                    command=self.set_password)
        self.btn_generate.place(relx=0.2, rely=0.5, anchor=tk.CENTER)

        self.password_length_slider = customtkinter.CTkSlider(master=self.second_frame, from_=4, to=30,
                                                              number_of_steps=30,
                                                              command=self.slider_event)

        self.password_length_slider.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

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
        self.btn_geenerate = customtkinter.CTkButton(master=self.third_frame, text="bdd", width=100,
                                                     command=self.bd) 
        self.btn_geenerate.place(relx=0.2, rely=0.5, anchor=tk.CENTER)

        # bouton actualiser
        self.bt_geenerate = customtkinter.CTkButton(master=self.third_frame, text="b2d", width=100,
                                                    command=self.reload_text)
        self.bt_geenerate.place(relx=0.3, rely=0.7, anchor=tk.CENTER)

        self.textbox = customtkinter.CTkTextbox(
            master=self.third_frame, width=800, corner_radius=0)
        self.textbox.grid(row=1, column=1, sticky="nsew")

        self.username_db = customtkinter.CTkEntry(
            master=self.second_frame, width=100)
        self.username_db.place(relx=0.5, rely=0.20)
        self.website_db = customtkinter.CTkEntry(
            master=self.second_frame, width=100)
        self.website_db.place(relx=0.5, rely=0.40)
        self.password_db = customtkinter.CTkEntry(
            master=self.second_frame, width=100)
        self.password_db.place(relx=0.5, rely=0.60)

        # self.textbox.insert(0, "new text to insert")  # insert at line 0 character 0
        # self.text = self.textbox.get(0, "end")  # get text from line 0 character 0 till the end
        # self.textbox.delete(0, "end")  # delete all text

        # ce code va inserer dans la textbox les element de la bd result [0] pour username ainsi de suite
        for result in results:
            self.textbox.insert(
                tk.END, f"{result[0]}: {result[1]}: ,{result[2]} \n")

        self.large_test_iage = customtkinter.CTkEntry(master=self)
        # self.textbox.configure(state="disabled")

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
        self.entry_password.insert(0, password.create_new(length=int(self.password_length_slider.get()),
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

    def bd(self):
        self.username = str(self.username_db.get())
        self.password = str(self.password_db.get())
        self.website = str(self.website_db.get())
        c.execute("INSERT INTO passwords (username, website, password) VALUES (?, ?, ?)",
                  (self.username, self.website, self.password))
        conn.commit()

    def home_button_event(self):
        self.change_frame("home")

    def frame_2_button_event(self):
        self.change_frame("frame_2")

    def frame_3_button_event(self):
        self.change_frame("frame_3")


# la j'essaie de faire la fonction pour actualiser le textbox des mots de passe / elle fonctionne a moitier

    def reload_text(self):
        self.username = str(self.username_db.get())
        self.password = str(self.password_db.get())
        self.website = str(self.website_db.get())
        # text_var.set()
        self.textbox.delete("1.0", tk.END)
        conn.commit()
        self.textbox.insert(tk.END, c.execute(
            "INSERT INTO passwords (username, website, password) VALUES (?, ?, ?)", (self.username, self.website, self.password)))


# lancement
if __name__ == "__main__":
    app = App()
    app.mainloop()
