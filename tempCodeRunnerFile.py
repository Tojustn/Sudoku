            num = input("What number do you want to input?\t")
            row = input("What row would you like to place " + num + " in\t")
            col = input("What col would you like to place " + num + " in\t")
            try:
                user_move.append(num)
                user_move.append(row)
                user_move.append(col)
                if self.valid_move(row,col) == False: # checks if row and col were already placed by a computer
                    raise ValueError # if not in val ValueError is raised
                valid_square = True
            except ValueError:
                print("That was not a valid move. Try again")
            except IndexError:
                print("Out of Bounds bruv")

        return user_move
        


    def game(self):
        self.display_board()
        while self.winner == False: