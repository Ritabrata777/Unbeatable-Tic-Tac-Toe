import tkinter as tk
from tkinter import messagebox
import copy

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe - Ritabrata")
        self.geometry("300x300")
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self, text='', font=('Helvetica', 24), width=3, height=1,
                                   command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = button

   
 def make_move(self, row, col):
        if self.board[row][col] == ' ' and self.current_player == 'X':
            self.board[row][col] = 'X'
            self.buttons[row][col].config(text='X')
            winner = self.check_winner(self.board)
            if winner:
                messagebox.showinfo("Winner", f"Player {winner} wins!")
                self.reset_game()
            elif self.is_draw(self.board):
                messagebox.showinfo("Draw", "It's a draw! :(")
                self.reset_game()
            else:
                self.current_player = 'O'
                self.after(300, self.computer_move)  # Delay for better UX
def computer_move(self):
        best_score = -float('inf')
        best_move = None

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'O'
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = ' '
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        
    


