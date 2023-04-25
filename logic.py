import tkinter as tk
import color as clr
import random

class Game:
    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry("600x550")
        self.window.resizable(height=False, width=False)
        self.window.config(bg="black")
        self.window.title("2048 game")
        self.game_area = tk.Frame(self.window,bg="#AD6260",bd=10,borderwidth=10,height=500,width=500)
        self.game_area.grid(padx=80,pady=80)
        self.make_GUI()
        self.initialize()
        self.window.bind("<Left>",self.left)
        self.window.bind("<Right>", self.right)
        self.window.bind("<Up>", self.up)
        self.window.bind("<Down>", self.down)
        self.window.bind("a",self.check)

        self.window.mainloop()

    def check(self,event):
        self.update_GUI()
        self.printmat()
        self.stack()
        self.combine()
        self.stack()
        self.add_newtile()
        self.update_GUI()
        self.printmat()
        #self.combine()


    def printmat(self):
        for i in range(4):
            for j in range(4):
                print(self.matrix[i][j],"  ",end="")
            print()

    #making empty 4×4 cell
    def make_GUI(self):
        self.cell=[]

        for i in range(4):
            row=[]
            for j in range(4):
                cell_frame = tk.Frame(self.game_area,bg="#FAABF1",height=100,width=100)
                cell_number = tk.Label(self.game_area,bg="#FAABF1")
                cell_frame.grid(row=i,column=j,pady=5,padx=5)
                cell_number.grid(row=i,column=j)
                cell_data={"frame":cell_frame,"number":cell_number}
                row.append(cell_data)
            self.cell.append(row)

        score_frame = tk.Frame(self.window, height=70,width=150,bg="#B06362")
        score_frame.place(x=200,y=5,height=60,width=200)
        tk.Label(score_frame, text="SCORE",font=("ariel",14,"bold"),bg="#B06362").place(x=50,y=0)
        self.score_label = tk.Label(score_frame, text="0",font=("ariel",14,"bold"),bg="#B06362")
        self.score_label.place(x=80,y=28)


    #initialize the game by randomly placing the initial two 2s at ramdom places
    def initialize(self):
        #creating matrix of zeroes
        self.matrix = [[0]*4 for _ in range(4) ]  #empty matrix

        r = random.randint(0,3)
        c = random.randint(0,3)

        self.matrix[r][c]=2
        self.cell[r][c]["frame"].config( bg = clr.bg_color[2]),
        self.cell[r][c]["number"].config( bg = clr.bg_color[2],
            fg = clr.fg_color[2],
            font= clr.color_fonts[2],
            text="2"
        )
        #the second 2,making sure it does not go at the previous place

        while(self.matrix[r][c] != 0):

            r = random.randint(0, 3)
            c = random.randint(0, 3)
        self.matrix[r][c] = 2
        self.cell[r][c]["frame"].config(bg=clr.bg_color[2]),
        self.cell[r][c]["number"].config(bg=clr.bg_color[2],
                                         fg=clr.fg_color[2],
                                         font=clr.color_fonts[2],
                                         text="2"
                                         )
        self.score = 0

    #we will create few function now,b using then we can manipulate each move into left move
    #func to stack each move to the lest side
    def stack(self):    #working properly
        new_mat = [[0]*4 for _ in range(4) ]
        for i in range(4):    #range 4 is from 0 to 3
            no_of_position = 0
            for j in range(4):
                if(self.matrix[i][j] != 0):
                    new_mat[i][no_of_position] = self.matrix[i][j]
                    no_of_position += 1
        self.matrix = new_mat

    #func to reverse the matrix
    def reverse(self):
        new_mat = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                new_mat[i][j] = self.matrix[i][3-j]
        self.matrix = new_mat


    #func to transpose the matrix
    def transpose(self):
        new_mat = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                new_mat[i][j] = self.matrix[j][i]
        self.matrix = new_mat

    #fucn to combine two value that are same and next to each other(only for a left move)
    def combine(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] !=0 and self.matrix[i][j] == self.matrix[i][j+1]:
                    self.matrix[i][j] *= 2
                    self.matrix[i][j+1] = 0
                    self.score += self.matrix[i][j]


    #add 2 or 4 ramdomly to an empt cell
    def add_newtile(self):
        if any(0 in row for row in self.matrix):
            r = random.randint(0, 3)
            while (self.matrix[r][3] != 0):
                r = random.randint(0, 3)
            self.matrix[r][3] = random.choice([2, 4])


    # update the GUI to a new row or column (from the left side;) )
    def update_GUI(self):
        for i in range(4):
            for j in range(4):
                cell_value = self.matrix[i][j]
                if cell_value == 0:
                    self.cell[i][j]["frame"].config(bg="#FAABF1"),
                    self.cell[i][j]["number"].config(bg="#FAABF1",text="")
                else:
                    self.cell[i][j]["frame"].config(bg=clr.bg_color[cell_value])
                    self.cell[i][j]["number"].config(bg=clr.bg_color[cell_value],
                                                     fg=clr.fg_color[cell_value],
                                                     font=clr.color_fonts[cell_value],
                                                     text=str(cell_value))
        self.score_label.config(text=self.score)
        self.window.update_idletasks()

    #four func for four possible moves
    def left(self, event):
        self.stack()
        self.combine()
        self.stack()
        self.add_newtile()

        self.update_GUI()

        self.game_status()

    def right(self, event):
            self.reverse()
            self.stack()
            self.combine()
            self.stack()
            self.add_newtile()
            self.reverse()

            self.update_GUI()
            self.game_status()


    def up(self, event):
            self.transpose()
            self.stack()
            self.combine()
            self.stack()
            self.add_newtile()
            self.transpose()

            self.update_GUI()
            self.game_status()

    def down(self, event):
            self.transpose()
            self.reverse()
            self.stack()
            self.combine()
            self.stack()
            self.add_newtile()
            self.reverse()
            self.transpose()

            self.update_GUI()
            self.game_status()

    #func to check if any possible moves left
    def horizontal_moves_exits(self):
        for i in range(4):
            for j in range(3):
                if(self.matrix[i][j] == self.matrix[i][j+1]):
                    return True
        print("no hor move")
        return False

    def vertical_moves_exits(self):
        for i in range(3):
            for j in range(4):
                if(self.matrix[i][j] == self.matrix[i+1][j]):
                    return True

        return False

    def left_move_exist(self):
        f=0
        for i in range(4):
            if(self.matrix[i][3]!=0):
                f=1
        if(f==1):
            return True
        else:
            print("no left move")
            return False

    def right_move_exist(self):
        f=0
        for i in range(4):
            if(self.matrix[i][0]!=0):
                f=1
        if(f==1):
            return True
        else:
            print("no right move")
            return False

    def up_move_exist(self):
        f=0
        for j in range(4):
            if(self.matrix[3][j]!=0):
                f=1
        if(f==1):
            return True
        else:
            return False

    def down_move_exist(self):
        f=0
        for j in range(4):
            if(self.matrix[0][j]!=0):
                f=1
        if(f==1):
            return True
        else:
            return False



    #to check if the game is over (win\lose)
    def game_status(self):
        #game won
        if any(2048 in row for row in self.matrix):
            print("game won")
            game_status_frame = tk.Frame(self.game_area,bg="#26FFE1",bd=10,borderwidth=10,height=100,width=200)
            game_status_frame.place(x=500,y=5)
            tk.Label(game_status_frame, text="YOU WON!!!",bg="#FFCC00",
                     fg="#26FFE1",
                     font=("Helvetica",50, "bold"),
                      ).place()

        elif not any( 0 in row for row in self.matrix) and not self.horizontal_moves_exits() and not self.vertical_moves_exits():
            print("game over")
            game_status_frame = tk.Frame(self.window,bg="#C2A8AD",bd=10,borderwidth=10,height=100,width=300)
            game_status_frame.place(relx=0.5,rely=0.5,anchor="center")
            tk.Label(game_status_frame, text="YOU LOSE!!!",
                     bg="#C2A8AD",
                     fg ="#F1E7F5",
                    font =("Helvetica",30, "bold"),
            ).place(relx=0.5,rely=0.5,anchor="center")

def main():
    Game()

if __name__ == "__main__" :
    main()