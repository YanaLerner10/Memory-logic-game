# 🎀 PyMemory Challenge

> **Train your brain, one digit at a time.** ✨

![Python](https://img.shields.io/badge/Python-3.8%2B-FFB7B2?style=for-the-badge\&logo=python\&logoColor=white) ![Status](https://img.shields.io/badge/Status-Active-B5EAD7?style=for-the-badge) ![License](https://img.shields.io/badge/License-MIT-C7CEEA?style=for-the-badge)

---

## 🦄 About The Game

**PyMemory Challenge** is a sweet, minimal sequence-memorization game written in Python. The concept is simple: the program shows a sequence of numbers for a short time and you must repeat it back exactly. The game grows gradually in difficulty — great for short practice sessions or demonstrating clean code structure.

* **Round 1:** One number — easy warmup.
* **Round 5:** Sequence gets longer and more challenging.
* **Round 10+:** Memory workout mode!

The project separates logic from presentation: `memory_logic.py` contains the game rules and checks, while `gui_game.py` and `main.py` provide graphical and terminal interfaces respectively. Full type hints and readable code make this repo easy to study and extend.

---

## 🍭 Project Structure

| File               | Role             | What it does                                                          |
| ------------------ | ---------------- | --------------------------------------------------------------------- |
| `memory_logic.py`  | 🧠 Core logic    | Generates sequences, validates input, and manages rounds.             |
| `gui_game.py`      | 💻 GUI (Tkinter) | A small, pastel-themed windowed version.                              |
| `main.py`          | ⌨️ CLI           | Terminal/console playable version — good for CI/testing.              |
| `requirements.txt` | 📦 Dependencies  | Python requirements (if any).                                         |
| `assets/`          | 🎨 Images & CSS  | (Optional) background, logo, and theme files for a web or desktop UI. |

---

## ✅ Requirements

* Python 3.8+
* (Optional) `requirements.txt` — run `pip install -r requirements.txt` if present.

---

## 🚀 Run the Game

### Desktop GUI (Tkinter)

```bash
python gui_game.py
```

### Terminal / CLI

```bash
python main.py
```

---

## ⚡ Game Rules (Short)

1. A sequence of digits (0–9) is displayed for a few seconds.
2. Memorize the sequence, then type it back exactly.
3. Correct → next round (sequence grows). Wrong → Game Over.

---

## 🪄 Developer Notes

* The code is intentionally modular to make unit testing straightforward. Focus your tests on `memory_logic.py`.
* Use type hints and descriptive variable names when extending.
* Add logging if you want to trace game flow for debugging.

---

## 🎨 Website theme & assets (suggestions)

If you want to create a small website or a polished GUI, here are concrete recommendations to get a cute pastel aesthetic that matches the README vibe.

### Color palette (pastel)

* `--peach: #FFDDE1`
* `--mint:  #B5EAD7`
* `--lavender: #C7CEEA`
* `--cream: #FFF7E6`
* `--text-soft: #3B3A3A`

### Fonts (Google Fonts suggestions)

* **Primary (friendly UI):** `Poppins` or `Nunito`
* **Monospace (code blocks):** `Fira Code` or `JetBrains Mono`

Add to your HTML head (example):

```html
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&family=Fira+Code:wght@400;600&displa
