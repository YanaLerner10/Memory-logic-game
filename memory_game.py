import os
import time
import sys
from memory_logic import MemoryGame, MemoryError

def clear_screen():
    """Clears the console screen based on OS."""
    os.system('cls' if os.name == 'nt' else 'clear')

def run_game():
    game = MemoryGame()
    
    print("Welcome to the Memory Game!")
    print("Memorize the sequence, then repeat it back.")
    input("Press Enter to start...")

    while not game.over:
        clear_screen()
        
        # 1. Get the new sequence
        try:
            sequence = game.next_round()
        except MemoryError as e:
            print(e)
            break

        # 2. Display the sequence briefly
        print(f"Round {game.round}")
        print(f"Sequence: {' '.join(map(str, sequence))}")
        
        # Wait time increases slightly as sequence gets longer (optional design choice)
        display_time = 1.5 + (len(sequence) * 0.5)
        time.sleep(display_time)
        
        # 3. Hide sequence
        clear_screen()

        # 4. Get user input
        print(f"Round {game.round}")
        user_input_str = input("Enter the sequence (e.g., 123 or 1 2 3): ")
        
        # Parse input: allow spaces or no spaces
        # Remove spaces, then convert characters to ints
        cleaned_input = user_input_str.replace(" ", "").strip()
        
        if not cleaned_input.isdigit():
            print("Invalid input! You entered non-digits. Game Over.")
            break
            
        user_response = [int(char) for char in cleaned_input]

        # 5. Check response
        is_correct, score = game.check_response(user_response)

        if is_correct:
            print("Correct!")
            time.sleep(0.8)
        else:
            print(f"\nWrong! The correct sequence was: {sequence}")
            print(f"Final Score: {score}")
            
            retry = input("Play again? (y/n): ").lower()
            if retry == 'y':
                game.reset()
            else:
                print("Thanks for playing!")
                break

if __name__ == "__main__":
    run_game()
    