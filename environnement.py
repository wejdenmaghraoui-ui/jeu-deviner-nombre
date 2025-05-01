import gym # type: ignore
from gym import spaces # type: ignore
import numpy as np # type: ignore
import random

class GuessNumberEnv(gym.Env):
    """ Environnement Gym pour le jeu Devine le Nombre. """
    def __init__(self):
        super(GuessNumberEnv, self).__init__()

        # Définition du nombre à deviner
        self.target_number = random.randint(1, 100)

        # Espaces d'action (l'agent peut deviner un nombre entre 1 et 100)
        self.action_space = spaces.Discrete(100)

        # Espaces d'observation (dernière tentative de l’agent)
        self.observation_space = spaces.Box(low=1, high=100, shape=(1,), dtype=np.int32)

        # Initialisation des variables de jeu
        self.previous_guess = None
        self.attempts = 0

    def step(self, action):
        """ Met à jour l’état du jeu après une tentative de l’agent. """
        self.attempts += 1
        reward = -1  # Pénalité pour chaque tentative
        done = False

        if action == self.target_number:
            reward = 100  # Récompense maximale si l’agent trouve le bon nombre
            done = True
        elif action < self.target_number:
            reward = -0.5  # Légère pénalité si l’agent propose un nombre trop bas
        else:
            reward = -0.5  # Légère pénalité si l’agent propose un nombre trop haut

        self.previous_guess = action
        return np.array([action]), reward, done, {}

    def reset(self):
        """ Réinitialise le jeu pour un nouvel épisode d'entraînement. """
        self.target_number = random.randint(1, 100)
        self.previous_guess = None
        self.attempts = 0
        return np.array([random.randint(1, 100)])

    def render(self, mode='human'):
        """ Affiche l’état actuel du jeu. """
        print(f"Nombre cible: {self.target_number}, Dernière tentative: {self.previous_guess}")

# Enregistrement de l'environnement personnalisé dans Gym
gym.register("GuessNumber-v0", entry_point=GuessNumberEnv)
