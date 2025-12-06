# 🧠 PyMemory Challenge

> **Train your brain, one digit at a time.**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## 🎮 About The Game

**PyMemory Challenge** is a sequence memorization game built with Python. The concept is simple but addictive: the game shows you a sequence of numbers, and you must repeat it back exactly.

* **Round 1:** One number. Easy.
* **Round 5:** Five numbers. Getting harder.
* **Round 10:** ...Can you keep up?

The logic is separated entirely from the interface, designed with clean "Pythonic" code and full type hinting.

---

## 📂 Project Structure

This repository is organized into three main components:

| File | Type | Description |
| :--- | :--- | :--- |
| `memory_logic.py` | **The Brain** | Contains the core game rules. It generates random sequences and checks your answers. It has zero user interface code and is fully testable. |
| `gui_game.py` | **Desktop App** | A graphical window (GUI) built with **Tkinter**. Run this to play with a visual interface. |
| `main.py` | **CLI Game** | A terminal-based version of the game for quick testing and playing in the command line. |

---

## 🚀 How to Play

### Option 1: The Desktop App (GUI)
The best experience on Windows.

1.  Ensure you have Python installed.
2.  Run the game:
    ```bash
    python gui_game.py
    ```
3.  A window will pop up. Press **Start**, memorize the number, and type it in!

### Option 2: The Terminal (CLI)
Play directly in your command prompt.

1.  Run the script:
    ```bash
    python main.py
    ```
2.  Follow the on-screen prompts.

---

## ⚡ Game Rules

1.  **Watch:** A sequence of numbers (0-9) will appear.
2.  **Memorize:** You have a few seconds to memorize them before they disappear.
3.  **Repeat:** Type the sequence back exactly as it was shown.
4.  **Survive:** If you are correct, the sequence gets longer by one digit. If you fail, it's Game Over!

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **GUI Framework:** Tkinter (Standard Python Library)
* **Architecture:** Separation of Concerns (Logic vs. UI)

---

## 👨‍💻 Author

Created by **Yana**.
*Molecular Biology Specialist & Python Developer*

---
*Enjoying the game? Give this repo a ⭐!*