import tkinter as tk
from tkinter import messagebox
import sys

# Try to import the logic. If this fails, we catch the error to tell you why.
try:
    from memory_logic import MemoryGame
except ImportError:
    messagebox.showerror("Error", "Could not find 'memory_logic.py'.\nMake sure both files are in the same folder!")
    sys.exit()

class MemoryGameGUI:
    def __init__(self, root):
        self.game = MemoryGame()
        self.root = root
        self.root.title("Python Memory Game")
        self.root.geometry("400x350")

        # 1. Setup the UI Elements
        
        # Instruction Label
        self.lbl_instruction = tk.Label(root, text="Press Start to begin!", font=("Arial", 12))
        self.lbl_instruction.pack(pady=20)

        # The Big Number Display
        self.lbl_display = tk.Label(root, text="?", font=("Arial", 40, "bold"), fg="blue")
        self.lbl_display.pack(pady=20)

        # Input Box (Entry)
        self.entry_input = tk.Entry(root, font=("Arial", 14))
        self.entry_input.pack(pady=10)
        # Bind the 'Enter' key to the check_answer function
        self.entry_input.bind('<Return>', self.check_answer) 
        self.entry_input.config(state='disabled') 

        # Buttons frame
        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(pady=10)

        # Fixed color: used hex code #dddddd (light gray)
        self.btn_start = tk.Button(self.btn_frame, text="Start Game", command=self.start_round, bg="#dddddd")
        self.btn_start.pack(side=tk.LEFT, padx=5)

        # Fixed color: changed "#lightblue" to "lightblue" (removed the hashtag)
        self.btn_submit = tk.Button(self.btn_frame, text="Submit", command=self.check_answer, bg="lightblue")
        self.btn_submit.pack(side=tk.LEFT, padx=5)
        self.btn_submit.config(state='disabled')

    def start_round(self):
        """Starts a new round: gets sequence and displays it."""
        self.entry_input.delete(0, tk.END)
        self.entry_input.config(state='disabled')
        self.btn_submit.config(state='disabled')
        self.btn_start.config(state='disabled')
        
        try:
            # Get next sequence from your logic file
            sequence = self.game.next_round()
            self.lbl_instruction.config(text=f"Round {self.game.round}: Memorize this!")
            
            # Show the sequence
            seq_str = " ".join(map(str, sequence))
            self.lbl_display.config(text=seq_str)

            # Hide the text after 2000ms (2 seconds) using .after()
            self.root.after(2000, self.hide_sequence)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def hide_sequence(self):
        """Clears the screen and enables typing."""
        self.lbl_display.config(text="???")
        self.lbl_instruction.config(text="Type the sequence and press Enter")
        
        # Enable input
        self.entry_input.config(state='normal')
        self.entry_input.focus() 
        self.btn_submit.config(state='normal')

    def check_answer(self, event=None):
        """Gets user text, checks logic."""
        user_text = self.entry_input.get()
        
        # Strip spaces and validate
        clean_text = user_text.replace(" ", "").strip()
        
        if not clean_text.isdigit():
            messagebox.showwarning("Invalid Input", "Please enter numbers only.")
            return

        user_list = [int(char) for char in clean_text]

        is_correct, score = self.game.check_response(user_list)

        if is_correct:
            self.lbl_display.config(text="CORRECT!", fg="green")
            # Schedule next round automatically after 1 second
            self.root.after(1000, lambda: self.lbl_display.config(fg="blue"))
            self.root.after(1000, self.start_round)
        else:
            self.lbl_display.config(text="GAME OVER", fg="red")
            messagebox.showinfo("Game Over", f"Wrong! Score: {score}")
            
            # Reset logic and UI
            self.game.reset()
            self.lbl_instruction.config(text="Press Start to play again")
            self.btn_start.config(state='normal')
            self.entry_input.config(state='disabled')
            self.btn_submit.config(state='disabled')
            self.lbl_display.config(text="?", fg="blue")

if __name__ == "__main__":
    root = tk.Tk()
    app = MemoryGameGUI(root)
    root.mainloop()