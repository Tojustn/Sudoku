import time
import random
import copy
# From color python file import color class
from color import color

class Sudoku:
    def __init__(self):
        # Makes 9 arrays of 9 " " squares
        self.board = [[" " for i in range(9)] for i in range(9)]
        self.board_copy = [[" " for i in range(9)] for i in range(9)]
        self.winner = False
        self.solution_board = [[" " for i in range(9)] for i in range(9)]
        self.num_solutions = 0
    # Displays the sudoku board
    def display_board(self,board):
        index = 0 
        column_index = "   "
        for i in range(9):
            column_index += str(i) + "   "
        print(column_index)
        print(" -------------------------------------")
        # Prints board one row at a time 
        for row in board:
            string = str(index) + "| " + " | ".join( str(num) for num in row) + " |"
            print(string)
            if index % 3 == 0:
                print(" -------------------------------------")
            else:
                print(" -------------------------------------")
            index += 1

    # Computer places in numbers
    # Using backtracking 
    def generate_numbers(self):
        for r in range(0,9):
            for c in range(0,9):
                if self.board[r][c] == " ":
                    numbers = list(range(1, 10))
                    random.shuffle(numbers)
                    for num in numbers:
                        self.board[r][c] = num
                        # Checks if the number is not a dupe
                        if self.is_dup(self.board,r, c):
                            # Continue with the next cell
                            if self.generate_numbers():
                                return True
                        
                        # Undo the move (backtrack)
                        self.board[r][c] = " "
                    return False
        self.solution_board = copy.deepcopy(self.board)
        return True

    # Removes numbers from the board
    def remove_nums(self):
        for row in self.board:
            numbers = list(range(1,10))
            random.shuffle(numbers)
            # Number of missing numbers
            for i in range(1):
                numbers.pop(0)
            for col, spot in enumerate(row):
                if not spot in numbers:
                    row[col] = " "
            self.board_copy = copy.deepcopy(self.board)
    # Makes sure there is only one solution using naive backtracking
    def check_multiple_solutions(self):
        for r in range(0,9):
            for c in range(0,9):
                if self.board_copy[r][c] == " ":
                    for i in range(1,10):
                        self.board_copy[r][c] = i
                        # Checks if the number is not a dupe
                        if self.is_dup(self.board_copy,r, c):
                            # Continue with the next cell
                            if self.check_multiple_solutions():
                                return True
                        
                        # Undo the move (backtrack)
                        self.board_copy[r][c] = " "
                    return False
        # If this is a solution add one to the num solutions variable
        self.num_solutions += 1
        print(f"{self.num_solutions} found")
        # Instead of return True, return False allows program to keep exploring multiple solutions
        return True

            


    # Checks for dups either in rows or columns or square
    def is_dup(self,board,comrow,comcol):
        #print("Dupe has been run")
        # Checks rows first
        current_row = []
        for number in board[comrow]:
            if number != " ":
                current_row.append(number)
        sorted_row = sorted(current_row)
        for i in range(len(sorted_row)-1):
            if sorted_row[i] == sorted_row[i+1]:
                #print("Theres a dupe in rows")
                return False
                
        #print("Row pass")
        # Checks columns
        current_col = []
        for row in board:
            if row[comcol] != " ":
                current_col.append(row[comcol])
        sorted_col = sorted(current_col)
        #print(sorted_col)
        for i in range(len(sorted_col)-1):
            if sorted_col[i] == sorted_col[i+1]:
                #print("Theres a dupe in cols")
                return False
                
        #print("Col pass")
        # Checks squares
        board_copy = board
        start_row = int(comrow) / 3
        start_col = int(comcol) / 3
        current_square = []
        for i in range(int(start_row)*3,(int(start_row)+1)*3):
            for j in range(int(start_col)*3,int((int(start_col)+1)*3)):
                if str(board_copy[i][j]) != " ":
                    current_square.append(str(board_copy[i][j]))
        
        sorted_square = sorted(current_square)
        print(f"Checking squares {int(start_row)}  {int(start_col)}")
        print(sorted_square)
        for i in range(len(sorted_square)):
            if sorted_square[i] != " ":
                sorted_square.append(i)
        for i in range(len(sorted_square)-1):
            if sorted_square[i] == sorted_square[i+1]:
                print(f" Checking {sorted_square[i]} and {sorted_square[i+1]}")
                #print(sorted_square)
                print(f"Theres a dupe in squares {start_row}{start_col}")
                return False
                
        #print("Square pass")
        return True
        

        
    # Checks if sudoku has been completed
    def check_win(self):
        is_row = True
        # Check rows first 
        row_check = True
        for row in self.board:
            all_int = []
            for col in row:
                all_int.append(str(col))
                
            sorted_row = sorted(all_int)
            for i in range(len(sorted_row)-1):
                if sorted_row[i] == sorted_row[i+1] or sorted_row[i] == " " or sorted_row[i+1] == " ":
                    is_row = False
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
            sorted_col = sorted(array)
            for i in range(len(sorted_col)-1):
                if sorted_col[i] == sorted_col[i+1] or sorted_col[i] == " " or sorted_col[i+1] == " ":
                    col_check = False
        # Finally check individual squares
        board_copy = self.board
        square_check = True
        for square in range(9):
            sorted_square = []
            square_nums = []
            for j in range(square):
                for i in range(j*3,(j)*3):
                    for col in range(3):
                        square_nums.append(board_copy[i].pop(0))
                sorted_square = sorted(square_nums)
                for i in range(len(sorted_square)-1):
                    if sorted_square[i] == sorted_square[i+1] or sorted_square[i] == " " or sorted_square[i+1] == " ":
                        square_check = False
            square_nums.clear()
            sorted_square.clear()
    # Places the users move into the board
    def input_move(self):
        move = self.get_move()
        self.board[int(move[1])][int(move[2])] = color.BOLD  +  str(move[0]) + color.END
        if self.check_win():
            print(" YOU WIN!!!! SO PRO")
    def valid_move(self,num,row,col):
        if int(num) < 1 or int(num) > 9:
            return False
        if self.board_copy[int(row)][int(col)] != " ":
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
        self.display_board(self.board)
        print("\n\n\n")
        time.sleep(.8)
        self.generate_numbers()
        self.remove_nums()
        self.check_multiple_solutions()
        
        self.board = self.solution_board
        self.remove_nums()
        self.check_multiple_solutions()
        while(self.num_solutions != 1):
            self.num_solutions = 0
            self.board = copy.deepcopy(self.solution_board)
            self.remove_nums()
            self.check_multiple_solutions()

        self.display_board(self.board)
        self.board_copy = copy.deepcopy(self.board)
        while self.winner == False:
            self.input_move()
            self.display_board(self.board)




s = Sudoku()
s.game()