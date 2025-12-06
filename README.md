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

The logic is separated entirely from the interface, meaning you can play this game in a **Desktop Window**, on a **Website**, or even in the **Terminal**.

---

## 📂 Project Structure

This repository is organized into three main layers:

| File | Type | Description |
| :--- | :--- | :--- |
| `memory_logic.py` | **The Brain** | Contains the core game rules. It generates random sequences and checks your answers. It has zero user interface code. |
| `gui_game.py` | **Desktop App** | A graphical window (GUI) built with **Tkinter**. Run this to play on your computer. |
| `app.py` | **Web Server** | A **Flask** server that allows you to play the game in a web browser. |
| `templates/` | **Web Design** | Contains the HTML/CSS for the web version of the game. |

---

## 🚀 How to Play

### Option 1: The Desktop App (GUI)
The easiest way to play on Windows.

1.  Ensure you have Python installed.
2.  Run the game:
    ```bash
    python gui_game.py
    ```
3.  A window will pop up. Press **Start**, memorize the number, and type it in!

### Option 2: The Web Version
Play in your favorite browser (Chrome, Edge, etc.).

1.  Install Flask (one time only):
    ```bash
    pip install flask
    ```
2.  Start the server:
    ```bash
    python app.py
    ```
3.  Click the link in the terminal (usually `http://127.0.0.1:5000`) to play.

---

## ⚡ Game Rules

1.  **Watch:** A sequence of numbers (0-9) will appear on the screen.
2.  **Memorize:** You have a few seconds to memorize them before they disappear.
3.  **Repeat:** Type the sequence back exactly as it was shown.
4.  **Survive:** If you are correct, the sequence gets longer by one digit. If you fail, it's Game Over!

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **GUI Framework:** Tkinter (Standard Python Library)
* **Web Framework:** Flask
* **Styling:** Custom CSS (for the web version)

---

## 👨‍💻 Author

Created by **Yana**.
*Molecular Biology Specialist & Python Developer*

---
*Enjoying the game? Give this repo a ⭐!*
