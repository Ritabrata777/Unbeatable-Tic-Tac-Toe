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

   
