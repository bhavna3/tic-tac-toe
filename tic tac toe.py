import tkinter as tk
from tkinter import messagebox

# Initialize the game variables
current_player = "X"
board = [" " for _ in range(9)]

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Function to handle a player's move
def place_symbol(idx):
    global current_player
    if board[idx] == " ":
        board[idx] = current_player
        buttons[idx].config(text=current_player)
        if check_winner(current_player):
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            root.quit()
        elif " " not in board:
            messagebox.showinfo("Game Over", "It's a draw!")
            root.quit()
        else:
            current_player = "O" if current_player == "X" else "X"

# Function to check for a win
def check_winner(player):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]

    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Create buttons for the Tic Tac Toe grid
buttons = []
for i in range(9):
    row, col = divmod(i, 3)
    button = tk.Button(root, text=" ", width=10, height=2,
                       command=lambda i=i: place_symbol(i))
    button.grid(row=row, column=col)
    buttons.append(button)

# Run the main game loop
root.mainloop()
