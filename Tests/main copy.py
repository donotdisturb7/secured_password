import os
import tkinter as tk
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from tkinter import messagebox

import customtkinter
from PIL import Image

import password

customtkinter.set_appearance_mode("Dark")


def change_theme(new_appearance_mode):
    customtkinter.set_appearance_mode(new_appearance_mode)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("secured password")
        self.geometry("700x550")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # images
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "secure.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")),
                                                       size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")),
                                                       size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")),
                                                 size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "gen.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "gen2.png")),
                                                 size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "mdp.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "mdp.png")),
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
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Générer un Mot de passe",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w",
                                                      command=self.frame_2_button_event)
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
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # creation de la frame home
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="",
                                                                   image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="", image=self.image_icon_image)
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
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)

        self.entry_password = customtkinter.CTkEntry(master=self.second_frame, width=300)

        self.entry_password.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        self.btn_generate = customtkinter.CTkButton(master=self.second_frame, text="Generer", width=100,
                                                    command=self.set_password)
        self.btn_generate.place(relx=0.2, rely=0.5, anchor=tk.CENTER)

        self.password_length_slider = customtkinter.CTkSlider(master=self.second_frame, from_=4, to=30,
                                                              number_of_steps=30,
                                                              command=self.slider_event)

        self.password_length_slider.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.password_length_entry = customtkinter.CTkEntry(master=self.second_frame, width=50)

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
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # frame par défaut
        self.change_frame("home")

    def slider_event(self, value):
        self.password_length_entry.delete(0, 'end')
        self.password_length_entry.insert(0, int(value))

    def get_characters(self):
        chars = "".join(self.cb_digits_var.get() + self.cb_lower_var.get()
                        + self.cb_upper_var.get() + self.cb_symbols_var.get())
        return chars

    def set_password(self):
        try :
            self.entry_password.delete(0, 'end')
            self.entry_password.insert(0, password.create_new(length=int(self.password_length_slider.get()),
                                                          characters=self.get_characters()))
        except IndexError:
                        messagebox.showwarning("Attention", "Veuillez saisir une longueur de mot de passe valide ET les characteres que vous voulez dans votre mot de passe")

        
    def change_frame(self, name):
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

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

    def home_button_event(self):
        self.change_frame("home")

    def frame_2_button_event(self):
        self.change_frame("frame_2")

    def frame_3_button_event(self):
        self.change_frame("frame_3")


# lancement
if __name__ == "__main__":
    app = App()
    app.mainloop()
