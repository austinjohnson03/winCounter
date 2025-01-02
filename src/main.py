"""Basic win counter for stream using TKinter"""
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

from counter import Counter
from rank import Rank

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Win Counter')
        self.geometry('200x330')
        self.attributes('-topmost', True)
        # self.rs = 2100   Find way to encapsulate this

        self.counter = Counter(0, 0, 0, 0)

        self.win_label = ttk.Label(self, text=f'Wins: {self.counter.wins}')
        self.win_label.pack(pady=10)

        self.loss_label = ttk.Label(self, text=f'Losses: {self.counter.losses}')
        self.loss_label.pack(pady=10)

        self.draw_label = ttk.Label(self, text=f'Draws: {self.counter.draws}')
        self.draw_label.pack(pady=10)

        self.win_button = ttk.Button(self, text='Win', command=self.add_win)
        self.win_button.pack(pady=10)

        self.loss_button = ttk.Button(self, text='Loss', command=self.add_loss)
        self.loss_button.pack(pady=10)

        self.draw_button = ttk.Button(self, text='Draw', command=self.add_draw)
        self.draw_button.pack(pady=10)

        self.separator = ttk.Separator(self, orient='horizontal')
        self.separator.pack(fill='x', pady=10)

        self.reset_button = ttk.Button(self, text='Reset', command=self.reset)
        self.reset_button.pack(pady=10)

    def add_win(self):
        self.counter.add_win()
        self.win_label.config(text=f'Wins: {self.counter.wins}')
        try:
            self.to_file()
        except FileNotFoundError:
            messagebox.showerror('Error', 'File not found')


    def add_loss(self):
        self.counter.add_loss()
        self.loss_label.config(text=f'Losses: {self.counter.losses}')
        try:
            self.to_file()
        except FileNotFoundError:
            messagebox.showerror('Error', 'File not found')

    def add_draw(self):
        self.counter.add_draw()
        self.draw_label.config(text=f'Draws: {self.counter.draws}')
        try:
            self.to_file()
        except FileNotFoundError:
            messagebox.showerror('Error', 'File not found')

    def reset(self):
        self.counter.reset_counter()
        self.win_label.config(text=f'Wins: {self.counter.wins}')
        self.loss_label.config(text=f'Losses: {self.counter.losses}')
        self.draw_label.config(text=f'Draws: {self.counter.draws}')
        try:
            self.to_file()
        except FileNotFoundError:
            messagebox.showerror('Error', 'File not found')

    def rs_change(self):
        try:
            points = simpledialog.askinteger('Enter RS change: ', 'Points:')
            return points
        except ValueError:
            messagebox.showerror('Error', 'Please enter a valid number')
            return None
        
    def to_file(self):
        self.counter.to_file('counter.txt')

    def from_file(self):
        self.counter.from_file('counter.txt')



if __name__ == '__main__':
    app = App()
    app.mainloop()
