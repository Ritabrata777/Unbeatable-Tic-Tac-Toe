import tkinter as tk
from tkinter import messagebox
import copy

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe - Ritabrata & Susan")
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
if best_move:
            i, j = best_move
            self.board[i][j] = 'O'
            self.buttons[i][j].config(text='O')

        winner = self.check_winner(self.board)
        if winner:
            messagebox.showinfo("Winner", f"Computer ({winner}) wins! 🤖")
            self.reset_game()
        elif self.is_draw(self.board):
            messagebox.showinfo("Draw", "It's a draw!")
            self.reset_game()
        else:
            self.current_player = 'X'

    def minimax(self, board, depth, is_maximizing):
        winner = self.check_winner(board)
        if winner == 'O':
            return 10 - depth
        elif winner == 'X':
            return depth - 10
        elif self.is_draw(board):
            return 0

        if is_maximizing:
            max_eval = -float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'O'
                        eval = self.minimax(board, depth + 1, False)
                        board[i][j] = ' '
                        max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'X'
                        eval = self.minimax(board, depth + 1, True)
                        board[i][j] = ' '
                        min_eval = min(min_eval, eval)
            return min_eval

    def check_winner(self, board):
        # Rows & Columns
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != ' ':
                return board[i][0]
            if board[0][i] == board[1][i] == board[2][i] != ' ':
                return board[0][i]
        # Diagonals
        if board[0][0] == board[1][1] == board[2][2] != ' ':
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != ' ':
            return board[0][2]
        return None

    def is_draw(self, board):
        return all(board[i][j] != ' ' for i in range(3) for j in range(3)) and not self.check_winner(board)

    def reset_game(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='')
        self.current_player = 'X'

if __name__ == "__main__":
    game = TicTacToe()
    game.mainloop()
        
    


