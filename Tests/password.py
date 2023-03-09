import secrets


def create_new(length, characters):
    "fonction de generation d'un mot de passe aléatoire "
    return "".join(secrets.choice(characters) for _ in range(length))
