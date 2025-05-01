import tkinter as tk
import socket
import threading

# Configuration du client
HOST = '127.0.0.1'
PORT = 5555

class ClientApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Devine le Nombre - Client")

        # Interface utilisateur
        self.label = tk.Label(root, text="Entrez un nombre entre 1 et 100 :", font=("Arial", 12))
        self.label.pack()

        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack()

        self.send_button = tk.Button(root, text="Envoyer", command=self.send_guess, font=("Arial", 12))
        self.send_button.pack()

        self.output = tk.Text(root, height=10, width=50, font=("Arial", 12))
        self.output.pack()

        # Connexion au serveur
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))

        # Thread pour recevoir les messages du serveur
        threading.Thread(target=self.receive_messages, daemon=True).start()

    def send_guess(self):
        """Envoie le nombre deviné au serveur."""
        guess = self.entry.get()
        if guess:
            self.client.sendall(guess.encode())

    def receive_messages(self):
        """Affiche les messages reçus du serveur."""
        while True:
            try:
                msg = self.client.recv(1024).decode()
                self.output.insert(tk.END, msg + '\n')
            except:
                break

# Démarrage de l'application client
if __name__ == "_main_":
    root = tk.Tk()
    app = ClientApp(root)
    root.mainloop()
