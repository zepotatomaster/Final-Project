# CS 5 Gold Final Project
# Name: Sophia Cheng, Hanae Sugiura, Christian Garcia

import random 


def inarow_Neast( ch, r_start, c_start, A, N ):
    """ starting from (row,col) of (r_start,c_start)
        within 2d list-of-lists A (array)
        returns True if there are N ch's in a row and
        returns False otherwise
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start > H-1: return False # out of bounds row
    if c_start < 0 or c_start+(N-1) > W-1: return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nsouth( ch, r_start, c_start, A, N ):
    """ starting from (row,col) of (r_start,c_start)
        within 2d list-of-lists A (array)
        returns True if there are N ch's in a row and
        returns False otherwise
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start+(N-1) > H-1: return False # out of bounds row
    if c_start < 0 or c_start > W-1: return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nnortheast( ch, r_start, c_start, A, N ):
    """ starting from (row,col) of (r_start,c_start)
        within 2d list-of-lists A (array)
        returns True if there are N ch's in a row and
        returns False otherwise
    """
    H = len(A)
    W = len(A[0])
    if r_start-(N-1) < 0 or r_start > H-1: return False # out of bounds row
    if c_start < 0 or c_start+(N-1) > W-1: return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start-i][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nsoutheast( ch, r_start, c_start, A, N ):
    """ starting from (row,col) of (r_start,c_start)
        within 2d list-of-lists A (array)
        returns True if there are N ch's in a row and
        returns False otherwise
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start+(N-1) > H-1: return False # out of bounds row
    if c_start < 0 or c_start+(N-1) > W-1: return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

#Helper Function
def opposite(OX):
    """flips OX"""
    if OX == 'X':
        return 'O'
    else:
        return 'X'



class Board:
    """ a datatype representing a C4 board
        with an arbitrary number of rows and cols
    """
    
    def __init__( self, width, height ):
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        W = self.width
        H = self.height
        self.data = [ [' ']*W for row in range(H) ]

        # we do not need to return inside a constructor!
        

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        H = self.height
        W = self.width
        s = ''   # the string to return
        for row in range(0,H):
            s += '|'   
            for col in range(0,W):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*W+1) * '-'    # bottom of the board
        s += '\n'
        for col in range(W):
            s += ' ' + str(col)

        
        # and the numbers underneath here
        
        return s       # the board is complete, return it

    def addMove(self, col, OX):
        """this method takes two inputs: the first input col represents the index of the column to which the checker will be added;
            the second input ox will be a 1-character string representing the checker to add to the board; ox should either be 'X' or 'O'.
        """
        H = self.height
        for row in range(0,H):
            if  self.data[row][col] != ' ':
                self.data[row-1][col] = OX
                return
        self.data[H-1][col] = OX



    def clear( self ):
        """this method clears the board that calls it
        """
        H = self.height
        W = self.width
        for row in range(H):
            for col in range(W):
                self.data[row][col] = ' '
            

    def setBoard( self, moveString ):
        """ takes in a string of columns and places
            alternating checkers in those columns,
            starting with 'X'
            
            For example, call b.setBoard('012345')
            to see 'X's and 'O's alternate on the
            bottom row, or b.setBoard('000000') to
            see them alternate in the left column.

            moveString must be a string of integers
        """
        nextCh = 'X'   # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'

    def allowsMove(self, col):
        """ this method returns 'True' if the calling object (of type Board) does allow a move into column c; 
            returns False if column c is not a legal column number for the calling object. 
            It also returns False if column c is full. 
        """
        H = self.height
        W = self.width
        D = self.data
        
        if col < 0 or col >= W:
            return False
        elif D[0][col] != ' ':
            return False
        else: 
            return True


    def isFull(self):
        """ this method should return True if the calling object (of type Board) is completely full of checkers. 
            It should return False otherwise.
        """
        H = self.height
        W = self.width
        D = self.data

        for col in range(W):
            if D[0][col] == ' ':
                return False
        return True

    

    def delMove(self, c):
        """ this methods does the opposite of addMove. It removes the top checker from the column c. If the column is empty
            then delMove does nothing.
        """
        H = self.height
        W = self.width
        D = self.data

        for row in range(H):
            if  self.data[row][c] != ' ':
                self.data[row][c] = ' ' 
                return
       
        
        
    def winsFor(self, OX): 
        """ this method's input OX is a one-character checker: returns True if there are 4 checkers of type OX in
            a row on the board; returns False otherwise
        """
        H = self.height
        W = self.width
        D = self.data

        for row in range(H):
            for col in range(W):
                if inarow_Neast( OX, row, col, D, 4 ) == True:
                    return True
                if inarow_Nsouth( OX, row, col, D, 4 ) == True:
                    return True 
                if inarow_Nnortheast( OX, row, col, D, 4 ) == True:
                    return True
                if inarow_Nsoutheast( OX, row, col, D, 4 ) == True:
                    return True
        return False


    def hostGame(self):
        """this method hosts a game of connect four. It alternates turns between 'X,' which always goes first, and 'O,' which
            always goes second. It should ask the user to select a column number for each move. 
        """
        
        user_choice = input("user choice is: ")
        
        if user_choice == 'X':
            ai_choice = 'O'
            user_plays = True
        elif user_choice == 'O':
            ai_choice = 'X'
            user_plays = True
        else: 
            user_plays = False
            

        choice_X = 0 
        if user_plays == True:
            if user_choice == 'X':
                while True:
                    if choice_X == 0:
                        print(self)
                        users_col = -1
                        while self.allowsMove( users_col ) == False:
                            users_col = int(input("user choose a column: "))
                        self.addMove(users_col, 'X')
                        if self.isFull() == True:
                            print('Tis a tie')
                            break
                        if self.winsFor('X') == True:
                            print("user wins - Congrats") 
                            break 
                        choice_X = 1
                    if choice_X == 1:
                        print(self)
                        num = self.aiMove('O')
                        self.addMove(num, 'O')
                        if self.isFull() == True:
                            print('Tis a tie')
                        if self.winsFor('X') == True:
                            print("AI wins - Congrats")
                        choice_X = 0
        
            else:
                while True:
                    if choice_X == 0:
                        print(self)
                        num = self.aiMove('X')
                        self.addMove(num, 'X')
                        if self.isFull() == True:
                            print('Tis a tie')
                        if self.winsFor('X') == True:
                            print("AI wins - Congrats")
                        choice_X = 1
                    if choice_X == 1:
                        print(self)
                        users_col = -1
                        while self.allowsMove( users_col ) == False:
                            users_col = int(input("user choose a column: "))
                        self.addMove(users_col, 'O')
                        if self.isFull() == True:
                            print('Tis a tie')
                            break
                        if self.winsFor('O') == True:
                            print("user wins - Congrats") 
                            break 
                        choice_X = 0
        
        
        else:
            choice_X = 0 
            while True:
                if choice_X == 0:
                    print(self)
                    num = self.aiMove('X')
                    self.addMove(num, 'X')
                    if self.isFull() == True:
                        print('Tis a tie')
                        break
                    if self.winsFor('X') == True:
                        print("X wins - Congrats") 
                        break 
                    choice_X = 1
                if choice_X == 1:
                    print(self)
                    num_1 = self.aiMove('O')
                    self.addMove(num_1, 'O')
                    if self.isFull() == True:
                        print('Tis a tie')
                    if self.winsFor('O') == True:
                        print("O wins - Congrats")
                    choice_X = 0
        

        

                    
    def colsToWin( self, OX):
        """ returns the list of columns where OX can move in the next turn in order to win and finish the game.
            the columns should be in numeric order. 
        """
        H = self.height
        W = self.width
        D = self.data

        L = []
        for col in range(W):
            if self.allowsMove(col) == True:
                self.addMove(col, OX)
                if self.winsFor(OX) == True:
                    L = L + [col]
                self.delMove(col)
        return L


    def aiMove(self, OX):
        """ takes in an input OX, then returns a single integer representing the column number
            If there is a way for OX to win, then aiMove returns that move. If there is no way for OX to win, but
            there is a way for OX to block the opponent, then aiMove must return a move that blocks the opponent.
            If there is no way for OX to win or block, then aiMove returns a move of the programmer's choice 
        """
        H = self.height
        W = self.width
        D = self.data

        C = self.colsToWin(OX) 
        B = opposite(OX)
        L = self.colsToWin(B)

        if C != []:
            Win = random.choice(C)
            return Win
        elif L != []: 
            Block = random.choice(L)
            return Block
        else:
            ran = -1
            while self.allowsMove( ran ) == False:
                ran = random.choice(range(W))
            return ran 
        

    def playGame( self, px, po):
        """ plays a game of Connect Four
            px and po are objects of type Player OR
            the string 'human'
            ss will "show scores" each time...
        """

        nextCheckerToMove = 'X'
        nextPlayerToMove = px
        
        while True:
            
            # print the current board
            print(self)

            # choose the next move
            if nextPlayerToMove == 'human':
                col = -1
                while not self.allowsMove( col ):
                    col = eval(input('Next col for ' + nextCheckerToMove + ': '))
            else: # it's a computer player
                """if ss:
                    scores = nextPlayerToMove.scoresFor(self)
                    print((nextCheckerToMove + "'s"), 'Scores: ', [ int(sc) for sc in scores ])
                    print()
                    col = nextPlayerToMove.tiebreakMove( scores )"""
                #else:
                col = nextPlayerToMove.nextMove( self )

            # add the checker to the board
            self.addMove( col, nextCheckerToMove )

            # check if game is over
            if self.winsFor( nextCheckerToMove ):
                print(self)
                print('\n' + nextCheckerToMove + ' wins! Congratulations!\n\n')
                break
            if self.isFull():
                print(self)
                print('\nThe game is a draw.\n\n')
                break

            # swap players
            if nextCheckerToMove == 'X':
                nextCheckerToMove = 'O'
                nextPlayerToMove = po
            else:
                nextCheckerToMove = 'X'
                nextPlayerToMove = px

        print('Come back 4 more!')
        

#Final Project
class Player:
    """ an AI player for Connect Four """

    def __init__( self, ox, tbt, ply ):
        """ the constructor """
        self.ox = ox
        self.tbt = tbt
        self.ply = ply
        

    def __repr__( self ):
        """ creates an appropriate string """
        s = "Player for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tbt + "\n"
        s += "  and ply == " + str(self.ply) + "\n\n"
        return s

    def oppCh(self):
        """ returns the other kind of checker or playing piece"""
        if self.ox == 'O':
            return "X"
        else:
            return "O"

    def winsFor(self, OX): 
        """ this method's input OX is a one-character checker: returns True if there are 4 checkers of type OX in
            a row on the board; returns False otherwise
        """
        H = self.height
        W = self.width
        D = self.data

        for row in range(H):
            for col in range(W):
                if inarow_Neast( OX, row, col, D, 4 ) == True:
                    return True
                if inarow_Nsouth( OX, row, col, D, 4 ) == True:
                    return True 
                if inarow_Nnortheast( OX, row, col, D, 4 ) == True:
                    return True
                if inarow_Nsoutheast( OX, row, col, D, 4 ) == True:
                    return True
        return False


    def scoreBoard(self, b):
        """ returns a single float value representing the score of the input b.
            This returns 100.0 if the board b is a win for self; returns 50.0 if it is neither a win nor a loss for self;
            returns returns 0.0 if it is a loss for self. 
        """
        if b.winsFor(self.ox) == True:
            return 100.0
        elif b.allowsMove == False:
            return -1.0
        elif b.winsFor(self.oppCh()) == True:
            return 0.0
        else:
            return 50.0
    

    def tiebreakMove(self, scores):
        """ this method takes in scores, which is a nonempty list of floating-point numbers.
            if there is only one highest score in the scores list, this method should return its column number. 
            If there is more than one highest score because of a tie, this method returns the column number of 
            the highest score appropriate to the plater's tiebreaking type
        """
        max_score = max(scores)
        o = []
        for i in range(len(scores)):
            if max_score == scores[i]:
                o = o + [i]
        if self.tbt == "LEFT":
            return o[0]
        elif self.tbt == "RIGHT":
            return o[-1]
        elif self.tbt == "RANDOM":
            return o[random.choice(len(o))]


    def scoresFor(self, b):
        """this method returns a list of scores, with the cth score representing of the input board after the player
        moves to column c. "Goodness" is measured by what happens in the game after self.ply moves"""
        
        scores = [50.0]*b.width
        for col in range(b.width):
            if b.allowsMove(col) == False:
                scores[col] = -1.0
            elif b.winsFor(self.ox) == True:
                scores[col] = 100.0
            elif b.winsFor(self.oppCh()) == True:
                scores[col] = 0.0
            elif self.ply == 0:
                scores[col] = 50.0
            elif self.ply>0:
                b.addMove(col, self.ox)
                if b.winsFor(self.ox) == True:
                    scores[col] = 100.0
                else:
                    op = Player(self.oppCh(),self.tbt, self.ply-1)
                    x = op.scoresFor(b)
                    op_bestmove = op.tiebreakMove(x)
                    scores[col] = abs(100-x[op_bestmove])
                b.delMove(col)
        return scores


    
    def nextMove(self, b):
        """this method takes in b, an object of type Board and returns an integer - the column number that the calling object of class Player
            chooses to move to.
        """
        best_move = self.scoresFor(b)
        return self.tiebreakMove(best_move)

b = Board(7,6)
def menu():
    """ a function that simply prints the menu """
    print()
    print("(0) Play against a human.")
    print("(1) Play against AI.")
    print("(2) Watch AI play another AI.")
    print("(3) GRUTOR MODE")
    print()
while True:     # the user-interaction loop
    menu()
    uc = input( "Choose your option." )

    # "clean and check" the user's input
    # 
    try:
        uc = int(uc)   # make into an int!
    except:
        print("I didn't understand your input! Continuing...")
        continue

    # run the appropriate menu option
    #
    if uc == 9:    # we want to quit
        break      # leaves the while loop altogether

    elif uc == 0:  # we want to enter a new list
        b.playGame('human', 'human')    # enter _something_
        break

    elif uc == 1:
        choice = input("Choose either X or O.")
        if choice == 'X':
            ply = int(input("Choose the AI's ply."))
            po = Player('O', 'LEFT', ply)
            b.playGame('human',po)
            break
        elif choice == 'O':
            ply = int(input("Choose the AI's ply."))
            px = Player('X', 'LEFT', ply)
            b.playGame(px,'human')
            break
        else:
            print("Invalid choice. Breaking...")
            break

    elif uc == 2:        # ai against ai
        choice1 = int(input("What ply will the X AI have?"))
        choice2 = int(input("What ply will the O AI have?"))
        px = Player('X', 'LEFT', choice1)
        po = Player('O', 'LEFT', choice2)
        b.playGame(px, po)

        break
    
    elif uc == 3:
        print("You are awesome, so you get to start first against an AI! Good luck!")
        po = Player('O', 'LEFT', 0)
        b.playGame('human',po)
        break
    else:
        print(uc, " ?      That's not on the menu!")



  



        

        

            