
# The Last Invader 

![Menu Screen](images/menu%20screen.png)

> A space shooter game built with Python and Pygame. Rescue hostages, defeat alien invaders, and survive long enough to escape through the portal!

---

## 🎮 About the Game

**The Last Invader** is a 2D top-down space shooter where you play as a lone hero fighting off an alien invasion. Two villain spaceships and a powerful boss are trying to stop you — but your mission is bigger than just surviving. You must rescue 5 hostages before they drift out of bounds, defeat the alien threat, and escape through the portal to win.

---

## 🕹️ How to Play

| Action | Control |
|---|---|
| Move up / down / left / right | `W` `A` `S` `D` |
| Aim | Mouse |
| Shoot | Left Click |
| Pause | `ESC` |

### Objective
- Rescue **5 hostages** before they fall out of bounds
- Defeat villain spaceships by hitting them **10 times** each
- Once all hostages are rescued, a **portal** appears — reach it to win!

### Survival Tips
- You have **5 lives** (displayed as hearts in the top left)
- Each hit from an enemy costs you half a heart
- Villain spaceships respawn after being defeated — stay alert
- The boss moves side to side and shoots continuously — keep moving!

---

## 🖥️ Screenshots


![Gameplay](images/gameplay.png)

---

![How to Play Screen](images/how%20to%20screen.jpg)

---

## ⚙️ Installation

See the full **[Installation Guide](docs/installation_guide.md)** for step-by-step instructions for Windows, macOS, and Linux.
git
**Quick start:**
```bash
pip install pygame
python main.py
```

---

## 📁 Project Structure

```
the-last-invader/
├── main.py               # Main game file
├── requirements.txt      # Python dependencies
├── images/               # Game sprites and backgrounds
├── music/                # Sound effects and music
├── characters/           # Hostage character sprites
├── fonts/                # Custom game fonts
└── docs/
    ├── user_guide.md         # How to play the game
    ├── installation_guide.md # How to install and run
    └── developer_docs.md     # Code structure and logic
```

---

## 📄 Documentation

- 📘 [User Guide](docs/user_guide.md) — Everything a player needs to know
- 🔧 [Installation Guide](docs/installation_guide.md) — How to get the game running on your machine
- 💻 [Developer Documentation](docs/developer_docs.md) — Code structure, functions, and game logic

---

## 👾 Features

- 2D top-down space shooter gameplay
- Rotating player and enemy sprites that track mouse/movement direction
- Boss enemy with side-to-side movement pattern and continuous shooting
- Two villain spaceships that chase the player and respawn after defeat
- Heart-based lives system with half-heart damage
- Hostage rescue mechanic with out-of-bounds game over condition
- Portal win condition
- Pause menu
- Full menu system with How to Play screen, Play, and Quit options
- Original sound effects and background music

---

## 🛠️ Built With

- [Python 3](https://www.python.org/)
- [Pygame](https://www.pygame.org/)
- [PyCharm](https://www.jetbrains.com/pycharm/) — Development environment

---

## 👥 Authors

- **Samuel Florez Garcia** — Co-developer
- **Kimora Robinson** — Co-developer

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.