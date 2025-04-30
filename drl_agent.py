import gym
import numpy as np
from stable_baselines3 import PPO

# Chargement de l’environnement personnalisé
env = gym.make("GuessNumber-v0")

# Création du modèle IA basé sur PPO
model = PPO("MlpPolicy", env, verbose=1)

# Entraînement de l'agent IA
model.learn(total_timesteps=10000)

# Test de l’agent après entraînement
obs = env.reset()
done = False

print("🤖 L'IA commence à jouer...")

while not done:
    action, _states = model.predict(obs)
    obs, reward, done, _ = env.step(action)
    print(f"IA a essayé: {action}, Récompense: {reward}")

print("🎯 L'IA a trouvé le nombre!")