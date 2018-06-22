
#encoding utf-8
#

import random
import copy
import pygame
from pygame.locals import *
import time
X=6
Y=6

# Q=[[[0]*4]*(X+2)]*(Y+2)
Q=[[[0 for i in range(4)] for j in range(X+2)] for k in range(Y+2)]

# Q値の更新
def new_Q(Q,x,y,dir):
    a=0.1
    ganma=0.9
    r=0
    if (x==4 and y==4 and dir==1)or(x==5 and y==3 and dir==2)or(x==6 and y==4 and dir==3)or(x==5 and y==5 and dir==0):
        r=1
    x_n=x
    y_n=y
    if dir==0:
        y_n-=1
    elif dir==1:
        x_n+=1
    elif dir==2:
        y_n+=1
    elif dir==3:
        x_n-=1
    else:#error
        print("方角入力がエラー")
        print(dir)
    m_Q=max(Q[x_n][y_n])
    N_Q=copy.deepcopy((1-a)*Q[x][y][dir]+a*(r+ganma*m_Q))
    return N_Q

def dir_limit(x,y):
    dir=[0,1,2,3]
    if x==1:
        dir.remove(3)
    if x==X:
        dir.remove(1)
    if y==1:
        dir.remove(0)
    if y==Y:
        dir.remove(2)
    # print("limit:",dir)
    return dir

def p_select(epsilon):
    if epsilon > random.random():
        return True
    else:
        return False

def decide_dir(Q,x,y):
    #epsiron-greedy
    epsilon=0.5
    xy=[]
    xy_max=[]
    limit=dir_limit(x,y)
    ran=random.random()
    max_Q=0
    for i in range(len(limit)):
        if max_Q<Q[x][y][limit[i]]:
            max_Q=Q[x][y][limit[i]]
    for i in range(len(limit)):
        if max_Q==Q[x][y][limit[i]]:
            xy_max.append(limit[i])
        else:
            xy.append(limit[i])
    # print("xy_max",xy_max)
    # print("xy",xy)
    if len(limit)==4:
        if len(xy_max)==4:
            if p_select(0.5):
                if p_select(0.5):
                    dir=xy_max[0]
                else:
                    dir=xy_max[1]
            else:
                if p_select(0.5):
                    dir=xy_max[2]
                else:
                    dir=xy_max[3]
        elif len(xy_max)==3:
            if p_select(epsilon):
                if len(xy_max)==3:
                    if p_select(1/3):
                        dir=xy_max[0]
                    else:
                        if p_select(1/2):
                            dir=xy_max[1]
                        else:
                            dir=xy_max[2]
            else:
                dir=xy[0]
        elif len(xy_max)==2:
            if p_select(epsilon):
                if p_select(0.5):
                    dir=xy_max[0]
                else:
                    dir=xy_max[1]
            else:
                if p_select(0.5):
                    dir=xy[0]
                else:
                    dir=xy[1]
        elif len(xy_max)==1:
            if p_select(epsilon):
                dir=xy_max[0]
            else:
                if p_select(1/3):
                    dir=xy[0]
                else:
                    if p_select(1/2):
                        dir=xy[1]
                    else:
                        dir=xy[2]
    elif len(limit)==3:
        if len(xy_max)==3:
            if p_select(1/3):
                dir=xy_max[0]
            else:
                if p_select(1/2):
                    dir=xy_max[1]
                else:
                    dir=xy_max[2]
        elif len(xy_max)==2:
            if p_select(epsilon):
                if p_select(0.5):
                    dir=xy_max[0]
                else:
                    dir=xy_max[1]
            else:
                dir=xy[0]
        elif len(xy_max)==1:
            if p_select(epsilon):
                dir=xy_max[0]
            else:
                if p_select(0.5):
                    dir=xy[0]
                else:
                    dir=xy[1]
    elif len(limit)==2:
        if len(xy_max)==2:
            if p_select(0.5):
                dir=xy_max[0]
            else:
                dir=xy_max[1]
        elif len(xy_max)==1:
            if p_select(epsilon):
                dir=xy_max[0]
            else:
                dir=xy[0]
    elif len(limit)==1:
        if len(xy_max)==1:
            dir=xy_max[0]
    else: print("error")
    # print(dir)
    return dir

def turn(x,y,status):
    clear=0
    a=0
    # print(x,y)
    dir=decide_dir(Q,x,y)
    # print("dir",dir)
    Q[x][y][dir]=new_Q(Q,x,y,dir)
    if dir==0:
        y-=1
    elif dir==1:
        x+=1
    elif dir==2:
        y+=1
    elif dir==3:
        x-=1
    if x==5 and y==4:
        # print("clear")
        clear=1
    return x,y,status,clear

def screen(Q):
    count=0
    X=800
    Y=800
    cell_size=X/8
    pygame.init()
    screen=pygame.display.set_mode((X,Y))
    pygame.display.set_caption("Q-learning")
    # A=np.zeros((int(X/cell_size),int(Y/cell_size)))
    x,y=1,1
    status=0
    while(1):
        screen.fill((0,0,0))
        #vertical line
        for i in range(int(X/cell_size)):
            pygame.draw.line(screen,(0,95,0),(i*cell_size,0),(i*cell_size,Y),1)
        #horizontal line
        for j in range(int(Y/cell_size)):
            pygame.draw.line(screen,(0,95,0),(0,j*cell_size),(X,j*cell_size),1)
        for event in pygame.event.get():
            #終了用イベント
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            #キー入力時
            if event.type==pygame.KEYDOWN:
                if event.key==K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                #pause機能
                if event.key==pygame.K_SPACE:
                     status=not(status)
        #print x,y
        pygame.draw.rect(screen,(0,95,0),(y*cell_size,x*cell_size,cell_size,cell_size))
        #print value_Q

        for i in range(len(Q)):
            for j in range(len(Q[i])):
                q_x=i*cell_size+cell_size/2
                q_y=j*cell_size+cell_size/2
                for k in range(len(Q[i][j])):
                    #直線で表す
                    if k==0:
                        pygame.draw.line(screen,(0,95,0),(q_x,q_y-(Q[i][j][k]*(cell_size/2))),(q_x,q_y),3)
                    elif k==1:
                        pygame.draw.line(screen,(0,95,0),(q_x,q_y),(q_x+(Q[i][j][k]*(cell_size/2)),q_y),3)
                    elif k==2:
                        pygame.draw.line(screen,(0,95,0),(q_x,q_y),(q_x,q_y+(Q[i][j][k]*(cell_size/2))),3)
                    elif k==3:
                        pygame.draw.line(screen,(0,95,0),(q_x-(Q[i][j][k]*(cell_size/2)),q_y),(q_x,q_y),3)
        pygame.display.update()
        if status==1:
            x,y,status,clear=turn(x,y,status)
            if clear==1:
                x,y=1,1
                clear=not(clear)
                count+=1
                print("回数:",count)
        elif status==0:
            pass

# def epoc(Q):
#     #初期化
#     x=1
#     y=1
#     count=0
#     while(1):
#         count+=1
#         a=0
#         # print(x,y)
#         dir=decide_dir(Q,x,y)
#         # print("dir",dir)
#         Q[x][y][dir]=new_Q(Q,x,y,dir)
#         if dir==0:
#             y-=1
#         elif dir==1:
#             x+=1
#         elif dir==2:
#             y+=1
#         elif dir==3:
#             x-=1
#
#         if x==5 and y==4:
#             print("clear")
#             break
#     return Q,count

# def main(Q):
    # for i in range(10):
    #     Q,count=copy.deepcopy(epoc(Q))
    #     print("epoc:",i)
    #     print("count:",count)


if __name__=="__main__":
    # main(Q)
    screen(Q)
