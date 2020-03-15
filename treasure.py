import numpy as np

class Game():
    def __init__(self):
        self.x_size = 3
        self.y_size = 3
        self.init_position = np.array([2,0])
        self.game_board = np.zeros((self.x_size,self.y_size))
        """

    
        0 0 G
        0 D 0 
        S 0 D 

        G = 1
        D = -1

        """
        self.game_board[0][2] = 1
        self.game_board[1][1] = -1
        self.game_board[2][2] = -1
        # self.game_board[1][3] = -1
        # self.game_board[1][4] = -1
        # self.game_board[4][2] = -1
    
    def judge(self,x,y):
        if self.game_board[x][y] == 0:
            return 0
        elif self.game_board[x][y] == 1:
            return 1
        else:
            return -1
    
    def check_size(self,x,y):
        if x < 0 or y < 0 or x >= self.x_size or y >= self.y_size:
            return 0
        else:
            return 1
    
    def move(self,position,direction):
        if direction == 'up':
            position[0] -= 1
        elif direction == 'down':
            position[0] += 1
        elif direction == 'right':
            position[1] += 1
        elif direction == 'left':
            position[1] -= 1
        
        return position



    


    
