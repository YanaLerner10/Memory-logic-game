# 🎀 PyMemory Challenge

> **Train your brain, one digit at a time.** ✨

![Python](https://img.shields.io/badge/Python-3.8%2B-FFB7B2?style=for-the-badge\&logo=python\&logoColor=white)

---

## 🦄 About The Game

**PyMemory Challenge** is a sweet, minimal sequence-memorization game written in Python. The concept is simple: the program shows a sequence of numbers for a short time and you must repeat it back exactly. The game grows gradually in difficulty — great for short practice sessions or demonstrating clean code structure.

* **Round 1:** One number — easy warmup.
* **Round 5:** Sequence gets longer and more challenging.
* **Round 10+:** Memory workout mode!

---

## 🍭 Project Structure

| File               | Role             | What it does                                                          |
| ------------------ | ---------------- | --------------------------------------------------------------------- |
| `memory_logic.py`  | 🧠 Core logic    | Generates sequences, validates input, and manages rounds.             |
| `gui_game.py`      | 💻 GUI (Tkinter) | A small, pastel-themed windowed version.                              |
| `main.py`          | ⌨️ CLI           | Terminal/console playable version — good for CI/testing.              |
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

## ⚡ Game Rules (Short)

1. A sequence of digits (0–9) is displayed for a few seconds.
2. Memorize the sequence, then type it back exactly.
3. Correct → next round (sequence grows). Wrong → Game Over.

---

