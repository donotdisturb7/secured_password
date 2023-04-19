import secrets
from tkinter import messagebox


def cree_password(length, characters):
    "fonction de generation d'un mot de passe aléatoire "
    if characters == "":
        messagebox.showwarning("Attention", "Veuillez choisir les charactères que vous vouler dans votre mot de passe")
    if length >= 8:
        return "".join(secrets.choice(characters) for _ in range(length))
    else:
        messagebox.showwarning("Attention", "Pour des mesures de sécurité votre mot de passe doit contenir au minimuim 8 charactères")
    