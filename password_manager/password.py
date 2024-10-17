import bcrypt
import json
import os
import tkinter as tk
from tkinter import messagebox

class PasswordManager:
    def __init__(self, file_path='passwords.json'):
        self.file_path = file_path
        self.passwords = self.load_passwords()

    def add_password(self, website, password):
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        self.passwords[website] = hashed_password
        self.save_passwords()
        return hashed_password

    def load_passwords(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        return {}

    def save_passwords(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.passwords, file)

class PasswordManagerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Password Manager")

        self.pm = PasswordManager()

        self.label = tk.Label(master, text="Website:")
        self.label.pack()

        self.website_entry = tk.Entry(master)
        self.website_entry.pack()

        self.label2 = tk.Label(master, text="Password:")
        self.label2.pack()

        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack()

        self.add_button = tk.Button(master, text="Add Password", command=self.add_password)
        self.add_button.pack()

        self.view_button = tk.Button(master, text="View Hashed Password", command=self.view_password)
        self.view_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def add_password(self):
        website = self.website_entry.get()
        password = self.password_entry.get()
        if website and password:
            hashed_password = self.pm.add_password(website, password)
            messagebox.showinfo("Success", f"Password added for {website}.\nHashed: {hashed_password}")
            self.website_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter both website and password.")

    def view_password(self):
        website = self.website_entry.get()
        if website in self.pm.passwords:
            hashed_password = self.pm.passwords[website]
            self.result_label.config(text=f"Hashed Password for {website}: {hashed_password}")
        else:
            messagebox.showwarning("Not Found", "Website not found.")

if __name__ == "__main__":
    root = tk.Tk()
    password_manager_gui = PasswordManagerGUI(root)
    root.mainloop()
