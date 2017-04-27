import tkinter
from tkinter import filedialog
from tkinter import messagebox
import csv

class Player(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.tkinter_id = None

class Maze(object):
    def __init__(self, canvas, player_size=.6):
        self.canvas = canvas
        self.player_size = player_size
        self.player = None
        self.loaded = False

    def redraw_player(self):
          self.canvas.delete(self.player.tkinter_id)

          self.player.x = self.player.col * self.col_step + int(self.col_step * (1-self.player_size)/2)
          self.player.y = self.player.row * self.row_step + int(self.row_step * (1-self.player_size)/2)
          self.player.tkinter_id = self.canvas.create_oval(
                  self.player.x, self.player.y,
                  self.player.x+int(self.col_step * self.player_size), self.player.y+int(self.row_step * self.player_size),
                  fill='blue') #create new oval
          # print("Player now at %d,%d" % (self.player.x, self.player.y))

    def no_wall(self, row: int, col: int) -> bool:
      """
      Function called after a keypress to check theoretical new location against
      spreadsheet. Returns boolean indicating whether there's a wall
      """
      if col < 0 or col == self.col_len: #going outside the board horizontally
        return False
      if row < 0 or row == self.row_len: #going outside the board vertically
        return False
      return self.spreadsheet[row][col] == 'O'

#Functions called after keypresses
    def left(self):
      future_col = self.player.col - 1
      if self.no_wall(self.player.row, future_col):
        self.player.col = future_col
      self.redraw_player()

    def right(self):
      future_col = self.player.col + 1
      if self.no_wall(self.player.row, future_col):
        self.player.col = future_col
      self.redraw_player()

    def up(self):
      future_row = self.player.row - 1
      if self.no_wall(future_row, self.player.col):
        self.player.row = future_row
      self.redraw_player()

    def down(self):
      future_row = self.player.row + 1
      if self.no_wall(future_row, self.player.col):
        self.player.row = future_row
      self.redraw_player()

    def redraw_canvas(self):
        """
        Scales the maze into the canvas based on window size.
        """
#Get canvas size
        self.row_step = int(canvas.winfo_height()) // self.row_len
        self.col_step = int(canvas.winfo_width()) // self.col_len

#Traverse 2D list and draw board
        self.canvas.delete('all')
        for row in range(self.row_len):
          for col in range(self.col_len):
            if self.spreadsheet[row][col] == 'X':
              y0 = row * self.row_step
              x0 = col * self.col_step
              y1 = y0 + self.row_step
              x1 = x0 + self.col_step
              self.canvas.create_rectangle(x0, y0, x1, y1, fill='pink')
#This section feels messy
            if self.player:
                self.redraw_player()
            if self.spreadsheet[row][col] == 'P':
                self.spreadsheet[row][col] = 'O'
                self.player = Player(row, col)
                self.redraw_player()

    def exactly_one_player(self):
        return 1 == [item for row in self.spreadsheet for item in row].count('P')

    def open_file(self):
#Turn spreadsheet into 2D list
        f = filedialog.askopenfile()
        if f:
            self.spreadsheet = list(csv.reader(f, dialect='excel'))
            self.row_len = len(self.spreadsheet)
            self.col_len = len(self.spreadsheet[0])
            if self.exactly_one_player():
                self.redraw_canvas()
                self.loaded = True
            else:
                messagebox.showerror('Invalid Maze Format', 'Maze must have exactly one \'P\'')


def attach_menus(window, maze):
    menubar = tkinter.Menu(window)
    filemenu = tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=lambda: maze.open_file())
    menubar.add_cascade(label="File", menu=filemenu)
    window.config(menu=menubar)

if __name__ == '__main__':
#Set up window
    window = tkinter.Tk()
    # window.resizable(width=False, height=False)
    canvas = tkinter.Canvas(window, width=500, height=500)
    # canvas.grid()
    canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)
    maze = Maze(canvas)
    attach_menus(window, maze)

#Functions called after keypresses
    def left(event):
        maze.left()

    def right(event):
        maze.right()

    def up(event):
        maze.up()

    def down(event):
        maze.down()

    def resize(event):
        if maze.loaded:
            maze.redraw_canvas()

    window.bind('<Left>', left)
    window.bind('<Right>', right)
    window.bind('<Down>', down)
    window.bind('<Up>', up)
    window.bind('<Configure>', resize)

    window.mainloop()
