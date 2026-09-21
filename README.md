# 🚁 Sky Hunter

**Sky Hunter** is a 3D helicopter combat game developed using **Python, OpenGL, and PyOpenGL**. The player takes control of a combat helicopter, navigates a large 3D battlefield, attacks enemy tanks, avoids incoming missiles, and attempts to achieve the highest possible score.

The project combines interactive gameplay with fundamental **3D computer graphics concepts**, including object modeling, transformations, camera systems, animation, collision detection, and real-time rendering.

---

## 👥 Team Members

* **Afeefah Nusaybah Anfa**
* **Sujoy Chandra Kundu**
* **Dewan Iffaz Hassan**

---

## 🎮 Game Overview

In **Sky Hunter**, the player operates a combat helicopter over a large 3D battlefield. Multiple enemy tanks are placed throughout the environment and can attack the helicopter using projectiles.

The player must navigate the battlefield, switch between different camera views, locate enemy targets, drop bombs, avoid enemy attacks, and manage their remaining health. Destroying enemy tanks increases the score, while losing all available health results in a game-over state.

---

## 🕹️ How to Play

> **🚁 Move:** Control the helicopter using the movement keys and adjust its altitude to navigate the battlefield.
>
> **🎥 Camera:** Switch between different camera views and use the arrow keys to adjust the viewing direction.
>
> **💣 Attack:** Drop bombs toward enemy tanks and destroy them through accurate bombing.
>
> **⚔️ Survive:** Avoid enemy missiles and projectiles to protect the helicopter's health.
>
> **🏆 Score:** Destroy enemy tanks to earn points.
>
> **📡 Cheat Mode:** Activate Cheat Mode to detect nearby enemies, highlight targets, automatically aim and fire, and become immune to enemy bullet damage.
>
> **⏸️ Game States:** Start, pause, restart, and continue the game depending on the current state.
>
> **💥 Game Over:** Losing all health triggers the helicopter's falling/crashing sequence and ends the game.

---

## ✨ Key Features

### 1. 🚁 Helicopter Movement & Control

The player has full control over the helicopter and can move it **forward, backward, left, right, upward, and downward**.

The helicopter remains within the defined boundaries of the battlefield, preventing it from leaving the playable area. The main rotor blades also feature a **continuous spinning animation** during gameplay.

---

### 2. 🎥 3D Camera System

The game provides multiple camera perspectives so the player can experience the battlefield from different viewpoints.

Available views include:

* **Third-person view**
* **First-person view**
* **Top-down view**

The player can switch between these views during gameplay. The **left, right, up, and down arrow keys** allow the camera direction and viewing angle to be adjusted.

---

### 3. 🌎 3D Objects & Environment

Sky Hunter features a large 3D battlefield created using a **grid-based plane**.

The environment contains several 3D objects and visual elements, including:

* 🚁 Helicopter
* 💣 Bombs
* 🛡️ Enemy tanks
* 🌳 Trees
* ☁️ Clouds
* 🌱 Ground / battlefield
* 🔵 Sky

These objects are positioned within a shared 3D coordinate system and rendered using OpenGL to create the game environment.

---

### 4. 🛡️ Enemy Tanks

Multiple enemy tanks are placed throughout the battlefield and move around the environment using different movement patterns, including random movement.

Their unpredictable movement makes them more challenging targets for the player.

When **Cheat Mode** is active, nearby enemy tanks detected by the radar are **visually highlighted**, making them easier to locate.

---

### 5. 💣 Bombing & Collision System

The helicopter can drop bombs toward enemy tanks. After being released, the bombs travel **forward and downward** toward the battlefield.

When a bomb reaches the ground, an **explosion animation** is displayed. The game checks the distance between the explosion and nearby enemy tanks to determine whether they are within the effective range.

If an enemy tank is successfully hit, it is destroyed and the player's score increases.

The bombing system includes both **bomb-drop and explosion animations** to provide visual feedback during attacks.

---

### 6. ❤️ Score & Life System

The game includes a score and health system to track the player's progress and survival.

* Destroying enemy tanks increases the player's **score**.
* The helicopter has a limited amount of **health/lives**.
* Enemy attacks reduce the helicopter's health when they hit it.
* The player must manage their health while continuing to attack enemies.

When all available health/lives are lost, the helicopter enters a **falling and crashing animation**, followed by the Game Over state.

---

### 7. 🚀 Enemy Attack System

Enemy tanks can attack the helicopter using **missiles or other projectiles**.

The player must continuously move the helicopter and change its altitude to avoid incoming attacks.

If an enemy projectile hits the helicopter, its health is reduced, making movement and positioning an important part of survival.

---

### 8. 🎮 Game States

The game uses different states to manage the overall gameplay flow.

The main game states include:

* **Start** — Displays the initial game screen and allows the player to begin.
* **Playing** — Runs the main gameplay, movement, combat, and enemy systems.
* **Pause** — Temporarily stops gameplay while preserving the current game state.
* **Game Over** — Triggered when the helicopter loses all available health.
* **Restart** — Allows the player to start a new game after Game Over.

Each state controls the gameplay logic and information displayed on the screen.

---

### 9. 📡 Cheat Mode

A dedicated **Cheat Mode** can be activated or deactivated during gameplay using a specific key.

When Cheat Mode is enabled:

* A **radar system** detects nearby enemy tanks.
* Detected enemies are **visually highlighted**.
* Nearby targets can be automatically selected.
* The helicopter can automatically aim and fire toward selected targets.
* The helicopter becomes **invulnerable to enemy bullet damage**.

The player can toggle Cheat Mode on or off at any time during gameplay.

---

## 🛠️ Technologies Used

| Technology   | Purpose                              |
| ------------ | ------------------------------------ |
| **Python**   | Core programming language            |
| **OpenGL**   | 3D graphics rendering                |
| **PyOpenGL** | Python bindings for OpenGL           |
| **GLUT**     | Window management and input handling |

---

## 🎮 Controls

| Input               | Action               |
| ------------------- | -------------------- |
| `W`                 | Move Forward         |
| `S`                 | Move Backward        |
| `A`                 | Move Left            |
| `D`                 | Move Right           |
| `↑`                 | Adjust Camera Up     |
| `↓`                 | Adjust Camera Down   |
| `←`                 | Adjust Camera Left   |
| `→`                 | Adjust Camera Right  |
| `Mouse`             | Aim / Camera Control |
| `Left Mouse Button` | Attack / Fire        |
| `ESC`               | Exit Game            |

---

## 📂 Project Structure

The project is intentionally kept simple and consists of a single Python source file and this README.

```text
Sky-Hunter/
│
├── CSE423_final.py
└── README.md
```

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/sky-hunter.git
```

Then move into the project directory:

```bash
cd sky-hunter
```

### 2. Check Python

Make sure Python is installed:

```bash
python --version
```

### 3. Install Required Libraries

Install the required OpenGL packages:

```bash
pip install PyOpenGL PyOpenGL_accelerate
```

### 4. Run the Game

Run the Python file:

```bash
python CSE423_final.py
```

---

Some necessary pictures:


<img width="1117" height="783" alt="image" src="https://github.com/user-attachments/assets/2ab097b4-3998-4d3c-b540-1d6d224a236e" /> <img width="1118" height="807" alt="image" src="https://github.com/user-attachments/assets/758a56e5-0bd3-4a33-92af-62be907df61e" />





---

## 🎓 Academic Project

**Sky Hunter** was developed as a **Computer Graphics project** at:

**BRAC University**
**Department of Computer Science and Engineering**

The project applies 3D graphics concepts to create an interactive helicopter combat environment.

---


## ⭐ Project Highlights

> **Sky Hunter combines Python programming, OpenGL-based 3D rendering, interactive controls, combat mechanics, collision detection, and real-time game logic into a single interactive computer graphics project.**


