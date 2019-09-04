import random 

class TikTok(object):
    def __init__(self):
        self.board = [['-','-','-'],['-','-','-'],['-','-','-']]
        self.human_turn = True

    def print_board(self):
        for item in self.board:
            print(item[0], '|', item[1], '|', item[2])

    def is_board_full(self):
        for item in self.board:
            if '-' in item:
                return False
        return True
    
    def possibilities(self): 
        l = [] 
        for i in range(len(self.board)): 
            for j in range(len(self.board)): 
                if board[i][j] == '-': 
                    l.append((i, j)) 
        return(l)

    # Select a random place for the player 
    def random_place(self): 
        selection = possibilities() 
        current_loc = random.choice(selection)

        self.board[current_loc] = 'O' 
        return self.board

    def mark_token(self, x, y):
        if x < 0 or x > 2 or y < 0 or y > 2 or self.board[x][y] != '-':
            return False
        if self.human_turn:
            self.board[x][y] = 'X'
            return True
        self.board[x][y] = 'O'
        return True

    def row_win(self, player): 
        for x in range(len(self.board)): 
            win = True
            
            for y in range(len(self.board)): 
                if board[x, y] != player: 
                    win = False
                    continue
                    
            if win == True: 
                return win
        return win
    
    # Checks whether the player has three 
    # of their marks in a vertical row 
    def col_win(board, player): 
        for x in range(len(board)): 
            win = True
            
            for y in range(len(board)): 
                if board[y][x] != player: 
                    win = False
                    continue
                    
            if win == True: 
                return(win) 
        return(win) 
    
    # Checks whether the player has three 
    # of their marks in a diagonal row 
    def diag_win(self, player): 
        win = True
        
        for x in range(len(self.board)): 
            if self.board[x, x] != player: 
                win = False
        return win
    
    # Evaluates whether there is 
    # a winner or a tie  
    def evaluate(self): 
        winner = 0
        
        for player in ['O', 'X']: 
            if (self.row_win(player) or
                self.col_win(player) or 
                self.diag_win(player)): 
                    
                winner = player 
                
        if np.all(board != 0) and winner == 0: 
            winner = -1
        return winner


def play_game(): 
    my_game = TikTok()
    winner = 0
    while winner == 0:
        if my_game.human_turn:
            while True:
                x = input("Please enter x: ")
                y = input("Please enter y: ")
                if my_game.mark_token( x, y):
                    my_game.human_turn = False
                    break
        else:
            winner = my_game.evaluate()
            if winner != 0: 
                break
            my_game.random_place()
            my_game.print_board()
            my_game.human_turn = True
            winner = my_game.evaluate()
            if winner != 0: 
                break
    return winner
  
# Driver Code 
play_game()
