import numpy as np
from treasure import Game
import copy
import matplotlib.pyplot as plt

#board proscess
game = Game()
game_board = game.game_board
print(game_board)
game_direction = ['up','down','left','right']

def get_action(Q_table,dire,epsilon,x,y):

    #random choice
    if np.random.rand() < epsilon:
        return np.random.choice(dire)

    else:
        return dire[np.argmax(Q_table[x,y])]

def game_init():
    #init process
    game = Game()
    position= game.init_position
    
    return game,position

def game_reward(game,position):
    #result print
    if game.judge(position[0],position[1]) == 1:
        #print('You got a goal!')
        return 1
    elif game.judge(position[0],position[1]) == -1:
        #print('You died..')
        return -1
    else:
        return 0

def game_step(game,position,Q_table,dire,epsilon):
    while(True):
        pos = copy.deepcopy(position)
        direction = get_action(Q_table,dire,epsilon,pos[0],pos[1])
        index_dire = dire.index(direction)
        move_position = game.move(pos,direction)
        if game.check_size(pos[0],pos[1]):
            break
    reward = game_reward(game,move_position)

    return move_position,index_dire,reward



# def main_game(Q_table,dire,epsilon):

#     #init process
#     game = Game()
#     position= game.init_position
#     record = np.empty((0,3),int)

#     #game process
#     while(not game.judge(position[0],position[1])):
        
#         while(True):
#             pos = copy.deepcopy(position)
#             direction = get_action(Q_table,dire,epsilon,pos[0],pos[1])
#             index_dire = dire.index(direction)
#             move_position = game.move(pos,direction)
#             if game.check_size(pos[0],pos[1]):
#                 break
#         x_pos = position[0]
#         y_pos = position[1]
#         data_rec = np.array([[x_pos,y_pos,index_dire]])
#         record = np.append(record,data_rec,axis=0)
#         position = move_position

#     #result print
#     if game.judge(position[0],position[1]) == 1:
#         #print('You got a goal!')
#         return 1
#     elif game.judge(position[0],position[1]) == -1:
#         #print('You died..')
#         return -1



def Q_koushin(Q,state_x,state_y,state_a,s_next_x,state_next_y,alpha,reward,gamma):
    Q[state_x,state_y,state_a] += alpha*(reward + gamma*np.max(Q[s_next_x,state_next_y]) - Q[state_x,state_y,state_a])
    return Q[state_x,state_y,state_a]


if __name__ == '__main__':
    #hyper parameter
    epsilon = 0.01
    alpha = 0.5
    gamma = 0.8
    Q_table = np.zeros((game_board.shape[0],game_board.shape[1],len(game_direction)))
    episode = 100
    sucess = []

    for i in range(episode):
        game,position = game_init()
        while(not game.judge(position[0],position[1])):
            next_position,dire,reward = game_step(game,position,Q_table,game_direction,epsilon)
            Q_table[position[0],position[1],dire] = Q_koushin(Q_table,position[0],position[1],dire,next_position[0],next_position[1],alpha,reward,gamma)
            position = next_position
        
        if (i+1) % 5 == 0:
            count = 0
            heatmap = np.zeros((game_board.shape[0],game_board.shape[1]))
            for j in range(100):
                game,position = game_init()
                while(not game.judge(position[0],position[1])):
                    next_position,dire,reward = game_step(game,position,Q_table,game_direction,epsilon)
                    position = next_position
                    heatmap[next_position[0]][next_position[1]] += 1
                if reward == 1:
                    count += 1
            sucess.append(count)
            print('%d回時点' %(i+1))
            print(heatmap)

    # print(Q_table)


    # x = [i*100 for i in range(len(sucess))]
    # fig, ax = plt.subplots()
    # ax.grid()
    # ax.plot(x,sucess)
    # plt.show()
    print(sucess)


            