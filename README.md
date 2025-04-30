‏# 🎮 Devine le Nombre - Jeu en Réseau avec IA DRL et Interface Graphique

‏## 📌 Description
‏_"Devine le Nombre"_ est un *jeu multijoueur* où les joueurs doivent *deviner un nombre entre 1 et 100*.  
‏Le premier qui trouve la bonne réponse *remporte la partie*!

‏Ce projet combine *un serveur en réseau*, *une interface graphique interactive*, et *une IA basée sur le Deep Reinforcement Learning (DRL)* capable de s'entraîner et d'améliorer ses performances pour deviner plus rapidement.

---

‏## 🚀 Fonctionnalités principales
‏✅ *Jeu en réseau* : plusieurs joueurs peuvent se connecter au serveur simultanément.  
‏✅ **Interface graphique (Tkinter)** : permet une meilleure interaction utilisateur.  
‏✅ **Intelligence artificielle (DRL)** : l’IA apprend à deviner efficacement grâce à Gym et stable-baselines3.  
‏✅ *Scoreboard en temps réel* : suivi du nombre de tentatives et du temps écoulé.  
‏✅ *Support pour IA et clients humains* : les joueurs peuvent jouer contre l’IA ou entre eux.  

---

‏## 🏗️ Architecture du projet
‏📌 Le projet est organisé en plusieurs fichiers :
‏- **jeu.py** : Contient le serveur et la gestion des connexions des joueurs.
‏- **client_gui.py** : Interface graphique (Tkinter) pour jouer facilement.
‏- **drl_agent.py** : Agent IA entraîné avec *Deep Reinforcement Learning*.
‏- **environment.py** : Définit l'environnement Gym utilisé pour entraîner l'IA.
‏- **README.md** : Fichier de documentation pour comprendre et utiliser le jeu.
‏- **architecture_jeu.png** : Diagramme de l’architecture du jeu.

---

‏## ▶️ Installation et Démarrage

‏### 1️⃣ Installation des dépendances
‏Avant de lancer le jeu, installez les bibliothèques nécessaires :
‏
‏pip install stable-baselines3 gym pygame tkinter

‏### 2️⃣ Lancer le serveur
‏Démarrer le serveur pour gérer les connexions des joueurs et de l'IA :
‏
‏python3 jeu.py

‏### 3️⃣ Lancer un joueur humain
‏Ouvrir l'interface graphique (Tkinter) pour jouer :
‏
‏python3 client_gui.py

‏### 4️⃣ Lancer l'agent IA DRL (optionnel)
‏Si vous souhaitez voir l'IA en action :
‏
‏python3 drl_agent.py

---

‏## 🎯 Environnement Gym pour DRL
‏L’agent IA est entraîné avec stable-baselines3 et un environnement Gym personnalisé :
‏- *Observation* : Dernière tentative et indication du serveur.
‏- *Action* : Proposition d’un nombre entre 1 et 100.
‏- *Récompense* : -1 par tentative incorrecte, +100 si l’agent trouve la bonne réponse.
‏- *Optimisation* : L’IA apprend progressivement à deviner plus rapidement.

---

‏## 🎨 Interface Graphique (Tkinter)
‏- *Saisie intuitive* du nombre via une interface simple.
‏- *Affichage des messages du serveur* pour suivre le jeu.
‏- *Scoreboard mis à jour automatiquement*.

---

‏## 🏆 Scoreboard en temps réel
‏Le tableau de score affiche :
‏- Le *nom du joueur ou de l’IA*.
‏- Le *nombre de tentatives*.
‏- Le *temps écoulé* avant de trouver la bonne réponse.

---

‏## 📚 Ressources et références
‏- 🔗 [stable-baselines3](https://stable-baselines3.readthedocs.io/)
‏- 🔗 [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
‏- 🔗 [Gym Custom Environments](https://www.gymlibrary.dev/content/environment_creation/)
```
