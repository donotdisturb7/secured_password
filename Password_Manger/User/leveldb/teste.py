import sqlite3
import tkinter as tk

# Connect to the database
conn = sqlite3.connect('passwords.db')
c = conn.cursor()

# Execute a query to retrieve the usernames and passwords
c.execute("SELECT username, password, website FROM passwords")
results = c.fetchall()

# Create the Tkinter GUI
root = tk.Tk()
root.title("Passwords")
root.geometry("800x800")

# Create a listbox to display the usernames and passwords
listbox = tk.Listbox(root)

for result in results:
    listbox.insert(tk.END, f"{result[0]}: {result[1]}: {result[2]}")
listbox.pack()

root.mainloop()
