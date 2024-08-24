import time
import random
# From color python file import color class
from color import color

class Sudoku:
    def __init__(self):
        # Makes 9 arrays of 9 " " squares
        self.board = [[" " for i in range(9)] for i in range(9)]
        self.winner = False
        self.com_gen = []
    # Displays the sudoku board
    def display_board(self):
        index = 0 
        column_index = "   "
        for i in range(9):
            column_index += str(i) + "   "
        print(column_index)
        print(" -------------------------------------")
        # Prints board one row at a time 
        for row in self.board:
            string = str(index) + "| " + " | ".join(row) + " |"
            print(string)
            if index % 3 == 0:
                print(" -------------------------------------")
            else:
                print(" -------------------------------------")
            index += 1

    # Computer places in numbers
    def com_gen(self,totalnums):
        print("Here is the computer generated numbers")
            

    # Checks if sudoku has been completed
    def check_win(self):
        # Check rows first 
        row_check = True
        for row in self.board:
            sorted(row)
            for i in range(len(row)-1):
                if row[i] == row[i+1] or row[i] == " " or row[i+1] == " ":
                    row_check = False

        # Check columns next
        col_check = True
        cur_col = 0
        all_col = []
        col = []
        for i in range(8):
            for array in self.board:
                col.append(array[cur_col])
            all_col.append(col)
            col.clear()
        for array in all_col:
            for i in range(len(array)-1):
                if array[i] == array[i+1] or array[i] == " " or array[i+1] == " ":
                    col_check = False
        # Finally check individual squares
        board_copy = self.board
        for square in range(9):
            square_nums = []
            for j in range(square):
                for i in range(j*3,(j)*3):
                    for col in range(3):
                        square_nums.append(board_copy[i].pop(0))
                sorted(square_nums)
                for i in range(len(square_nums)-1):
                    if square_nums[i] == square_nums[i+1] or square_nums[i] == " " or square_nums[i+1] == " ":
                        col_check = False
            square_nums.clear()
            
    # Places the users move into the board
    def input_move(self):
        move = self.get_move()
        self.board[int(move[1])][int(move[2])] = move[0]
        if self.check_win():
            print(" YOU WIN!!!! SO PRO")
    def valid_move(self,num,row,col):
        if self.board[int(row)][int(col)] in self.com_gen:
            return False
        if int(num) < 1 or int(num) > 9:
            return False
        return True

    # Gets the users move
    def get_move(self):
        user_move = []
        valid_square = False
        while not valid_square:
            num = input("What number do you want to input?\t")
            row = input("What row would you like to place " + num + " in\t")
            col = input("What col would you like to place " + num + " in\t")
            try:
                user_move.append(num)
                user_move.append(row)
                user_move.append(col)
                if self.valid_move(num,row,col) == False: # checks if row and col were already placed by a computer
                    raise ValueError # if not in val ValueError is raised
                valid_square = True
            except ValueError:
                print("That was not a valid move. Try again\n")
            except IndexError:
                print("Out of Bounds bruv\n")

        return user_move
        


    def game(self):
        self.display_board()
        time.sleep(.8)
        while self.winner == False:
            self.input_move()
            self.display_board()




s = Sudoku()
s.game()