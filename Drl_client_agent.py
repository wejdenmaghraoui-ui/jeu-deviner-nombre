import socket
import time
import gym
import numpy as np
from stable_baselines3 import PPO
from environment import GuessNumberEnv

‎# إعدادات الاتصال بالسيرفر
HOST = '127.0.0.1'
PORT = 5555

‎# تحميل البيئة و تدريب النموذج
env = GuessNumberEnv()
model = PPO("MlpPolicy", env, verbose=0)
model.learn(total_timesteps=10000)

‎# الاتصال بالسيرفر
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print("[+] L'IA est connectée au serveur.")

‎# استقبال أول رسالة
msg = client.recv(1024).decode()
print(msg)

‎# تبدأ اللعبة
done = False
obs = env.reset()

while not done:
    action, _ = model.predict(obs)
    guess = int(action)

    print(f"🤖 IA propose: {guess}")
    client.sendall(str(guess).encode())

    msg = client.recv(1024).decode()
    print(f"🖥️ Serveur: {msg}")

    if "gagné" in msg or "a gagné" in msg:
        done = True
    elif "Trop" in msg or "❌" in msg:
        obs, _, _, _ = env.step(guess)
        time.sleep(0.5)
    else:
        time.sleep(0.2)

client.close()
print("🧠 IA déconnectée.")