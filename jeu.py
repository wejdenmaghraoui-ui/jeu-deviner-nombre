import socket
import threading
import random
import time

# Paramètres du serveur
HOST = '127.0.0.1'
PORT = 5555
number_to_guess = random.randint(1, 100)
game_over = False
players = {}
start_time = time.time()
lock = threading.Lock()

def broadcast(message):
    """Envoie un message à tous les joueurs connectés."""
    with lock:
        for conn in players.values():
            try:
                conn.sendall(message.encode())
            except:
                pass

def handle_client(conn, addr):
    """Gère les interactions avec un joueur."""
    global game_over
    print(f"[+] {addr} connecté.")
    players[addr] = conn

    try:
        conn.sendall("🎯 Devine un nombre entre 1 et 100!\n".encode())
        while not game_over:
            guess = conn.recv(1024).decode().strip()
            if not guess:
                continue

            try:
                guess = int(guess)
                if guess == number_to_guess:
                    game_over = True
                    elapsed_time = round(time.time() - start_time, 2)
                    broadcast(f"🎉 {addr} a gagné en {elapsed_time} secondes!\n")
                elif guess < number_to_guess:
                    conn.sendall("🔽 Trop bas!\n".encode())
                else:
                    conn.sendall("🔼 Trop haut!\n".encode())
            except ValueError:
                conn.sendall("❌ Veuillez entrer un nombre valide!\n".encode())
    finally:
        conn.close()
        players.pop(addr, None)

def start_server():
    """Démarre le serveur et gère les connexions des joueurs."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((HOST, PORT))
        server.listen(5)
        print(f"[*] Serveur lancé sur {HOST}:{PORT} - Nombre secret: {number_to_guess}")

        while True:
            conn, addr = server.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()
    except Exception as e:
        print(f"❌ Erreur serveur: {e}")

if __name__ == "__main__":
    start_server()