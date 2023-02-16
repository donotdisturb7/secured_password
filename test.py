from requirments import *


customtkinter.set_appearance_mode("dark")


class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # creation des tabs
        self.add("Home")
        self.add("Generer un mot de passe")
        self.add("Mes mots de passes")
        a = ""
        # ajoute des widgets

        text_var = tk.StringVar(value=a)
        self.label = customtkinter.CTkLabel(master=self.tab(
            "Home"), textvariable=text_var, width=900, height=900, corner_radius=10)
        self.label.grid(row=0, column=0, padx=20, pady=20)

        text_var = tk.StringVar(value=a)
        self.label = customtkinter.CTkLabel(master=self.tab(
            "Generer un mot de passe"), textvariable=text_var, width=900, height=900)
        self.label.grid(row=0, column=0, padx=20, pady=20)

        self.password_entry = customtkinter.CTkEntry(master=self.tab(
            "Generer un mot de passe"), placeholder_text="Votre mot de passe sécurisé", width=150, height=25)
        # self.password_entry.place(relx=0.6, rely=1.5,)
        self.password_entry.grid(row=0, column=0,  padx=5,  pady=10)
        self.generate_button = customtkinter.CTkButton(master=self.tab(
            "Generer un mot de passe"), text="Generer", command=self.generate_password)
        self.generate_button.place(relx=0.2, rely=0.5, anchor=tk.CENTER)
        self.password_entry.grid(row=0, column=0,  padx=5,  pady=10)

        self.save_button = customtkinter.CTkButton(master=self.tab(
            "Generer un mot de passe"), text="Enregistrer", command=self.save_password)
        self.save_button.place(relx=0.8, rely=0.5, anchor=tk.CENTER)

        self.passwords_listbox = customtkinter.CTkTextbox(
            master=self.tab("Mes mots de passes"), width=900, height=900)
        self.passwords_listbox.grid(row=0, column=0, padx=20, pady=20)

        self.refresh_button = customtkinter.CTkButton(master=self.tab(
            "Mes mots de passes"), text="Actualiser", command=self.refresh_passwords_list)
        self.refresh_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.entry1 = customtkinter.CTkEntry(master=self.tab(
            "Generer un mot de passe"), textvariable=text_var, width=120, height=25, fg_color=("white", "gray75"), corner_radius=8)
        self.entry1.place(x=155, y=500)

        self.passwords = {}

    def save_password(self):
        password_name = simpledialog.askstring(
            "Nom du mot de passe", "Entrez le nom du mot de passe à enregistrer", parent=self.master)
        if password_name:
            password = self.password_entry.get()
            self.passwords[password_name] = password
            messagebox.showinfo(
                "Succès", f"Le mot de passe \"{password_name}\" a été enregistré avec succès.")
        else:
            messagebox.showwarning(
                "Attention", "Le nom du mot de passe ne peut pas être vide.")

    def refresh_passwords_list(self):
        self.passwords_listbox.delete(0, END)
        for name, password in self.passwords.items():
            self.passwords_listbox.insert(END, name)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Secured Password ")
        # self.geometry("900")
        self.minsize(900, 900)
        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=0, padx=0, pady=0)


app = App()
app.mainloop()
