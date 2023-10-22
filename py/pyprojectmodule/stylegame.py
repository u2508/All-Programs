from tkinter import *
from tkinter import messagebox
import random


class Board:
    bg_color = {
        '2': '#eee4da',
        '4': '#ede0c8',
        '8': '#edc850',
        '16': '#edc53f',
        '32': '#f67c5f',
        '64': '#f65e3b',
        '128': '#edcf72',
        '256': '#edcc61',
        '512': '#f2b179',
        '1024': '#74c1cf',
        '2048': '#edc22e',
        '4096': '#4169E1',
        '8192': '#0a0a0a',
        '16384': '#046307',
    }
    color = {
        '2': '#776e65',
        '4': '#f9f6f2',
        '8': '#f9f6f2',
        '16': '#f9f6f2',
        '32': '#f9f6f2',
        '64': '#f9f6f2',
        '128': '#f9f6f2',
        '256': '#f9f6f2',
        '512': '#776e65',
        '1024': '#f9f6f2',
        '2048': '#f9f6f2',
        '4096': '#f9f6f2',
        '8192': '#f9f6f2',
        '16384': '#f9f6f2',
    }

    def __init__(self):
        self.n = 4
        self.window = Tk()
        self.window['bg']="red"
        self.window.title('16384 Game')
        self.window.attributes('-fullscreen', True)
        self.gameArea = Frame(self.window, bg='blue')
        self.canvas = Canvas(self.window,borderwidth=0, bg="blue", width=620, height=800)
        self.canvas.place(x=750, y=-1)
        self.board = []
        self.gridCell = [[0] * 8 for _ in range(8)]
        
        self.compress = False
        self.merge = False
        self.moved = False
        self.score = 0

        label1 = Label(
            self.window, text='Welcome to\nThe 16384 Game', fg='red', bg='#C1FFC1', width="15", font=("Calibri", 48)
        ).place(x=800, y=50)

        self.reset_button = Button(
            self.window, text="Reset Game", font=("Calibri", 48), bg="red", fg="blue",width="15" , command=self.reset_game
        )
        self.reset_button.place(x=800, y=300)

        self.exit_button = Button(
            self.window, text="Exit", font=("Calibri", 48), bg="red", fg="blue",width="15" , command=self.exit_game
        )
        self.exit_button.place(x=800, y=500)

        for i in range(8):
            rows = []
            for j in range(8):
                l = Label(
                    self.gameArea, text='', bg='blue', font=('arial', 22, 'bold'), width=4, height=2
                )
                l.grid(row=i, column=j, padx=7, pady=7)
                rows.append(l)
            self.board.append(rows)
        self.gameArea.grid()
        self.gameArea.place(x=1,y=25)

    def reset_game(self):
        self.gridCell = [[0] * 8 for _ in range(8)]
        self.score = 0
        self.random_cell()
        self.random_cell()
        self.paintGrid()

    def exit_game(self):
        self.window.destroy()

    def reverse(self):
        for ind in range(8):
            i = 0
            j = 7
            while i < j:
                self.gridCell[ind][i], self.gridCell[ind][j] = self.gridCell[ind][j], self.gridCell[ind][i]
                i += 1
                j -= 1

    def transpose(self):
        self.gridCell = [list(t) for t in zip(*self.gridCell)]

    def compressGrid(self):
        self.compress = False
        temp = [[0] * 8 for _ in range(8)]
        for i in range(8):
            cnt = 0
            for j in range(8):
                if self.gridCell[i][j] != 0:
                    temp[i][cnt] = self.gridCell[i][j]
                    if cnt != j:
                        self.compress = True
                    cnt += 1
        self.gridCell = temp

    def mergeGrid(self):
        self.merge = False
        for i in range(8):
            for j in range(8 - 1):
                if self.gridCell[i][j] == self.gridCell[i][j + 1] and self.gridCell[i][j] != 0:
                    self.gridCell[i][j] *= 2
                    self.gridCell[i][j + 1] = 0
                    self.score += self.gridCell[i][j]
                    self.merge = True

    def random_cell(self):
        cells = []
        for i in range(8):
            for j in range(8):
                if self.gridCell[i][j] == 0:
                    cells.append((i, j))
        curr = random.choice(cells)
        i = curr[0]
        j = curr[1]
        self.gridCell[i][j] = 2

    def can_merge(self):
        for i in range(8):
            for j in range(7):
                if self.gridCell[i][j] == self.gridCell[i][j + 1]:
                    return True

        for i in range(7):
            for j in range(8):
                if self.gridCell[i + 1][j] == self.gridCell[i][j]:
                    return True
        return False

    def paintGrid(self):
        for i in range(8):
            for j in range(8):
                if self.gridCell[i][j] == 0:
                    self.board[i][j].config(text='', bg='azure4')
                else:
                    self.board[i][j].config(
                        text=str(self.gridCell[i][j]),
                        bg=self.bg_color.get(str(self.gridCell[i][j])),
                        fg=self.color.get(str(self.gridCell[i][j]))
                    )


class Game:
    def __init__(self, gamepanel):
        self.gamepanel = gamepanel
        self.end = False
        self.won = False

    def start(self):
        self.gamepanel.random_cell()
        self.gamepanel.random_cell()
        self.gamepanel.paintGrid()
        self.gamepanel.window.bind('<Key>', self.link_keys)
        self.gamepanel.window.mainloop()

    def link_keys(self, event):
        if self.end or self.won:
            return

        self.gamepanel.compress = False
        self.gamepanel.merge = False
        self.gamepanel.moved = False

        pressed_key = event.keysym

        if pressed_key == 'Up' or pressed_key == 'w':
            self.gamepanel.transpose()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.transpose()

        elif pressed_key == 'Down' or pressed_key == 's':
            self.gamepanel.transpose()
            self.gamepanel.reverse()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.reverse()
            self.gamepanel.transpose()

        elif pressed_key == 'Left' or pressed_key == 'a':
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()

        elif pressed_key == 'Right' or pressed_key == 'd':
            self.gamepanel.reverse()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.reverse()

        else:
            pass

        self.gamepanel.paintGrid()

        flag = 0
        for i in range(8):
            for j in range(8):
                if self.gamepanel.gridCell[i][j] == 16384:
                    flag = 1
                    break

        if flag == 1:  # found 16384
            self.won = True
            messagebox.showinfo('16384 Game', message=f'You Wonnn!! the final score is {self.gamepanel.score}')
            #print(self.gamepanel.score)
            self.gamepanel.window.destroy()
            return

        for i in range(8):
            for j in range(8):
                if self.gamepanel.gridCell[i][j] == 0:
                    flag = 1
                    break

        if not (flag or self.gamepanel.can_merge()):
            self.end = True
            n = 'Game Over!!! \n Your final score is ' + str(self.gamepanel.score)
            messagebox.showinfo('16384 Game', n)

        if self.gamepanel.moved:
            self.gamepanel.random_cell()

        self.gamepanel.paintGrid()


def mainstrt():
    gamepanel = Board()
    game2048 = Game(gamepanel)
    game2048.start()


if __name__ == "__main__":
    mainstrt()
