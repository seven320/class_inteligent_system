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

def r_value(x,y,dir):
    r=0
    if dir==0:
        y-=1
    elif dir==1:
        x+=1
    elif dir==2:
        y+=1
    elif dir==3:
        x-=1
    #goal sel\tting
    goal_1=[5,4]
    goal_2=[2,5]
    if goal_1==[x,y]:
        r=2
    elif goal_2==[x,y]:
        r=1
    #wall setting
    out_wall=[]
    judge=0
    for i in range(X+1):
        out_wall.append([0,i])
        out_wall.append([X+1,i])
    for i in range(Y+1):
        out_wall.append([i,0])
        out_wall.append([i,Y+1])
    in_wall=[[2,2],[3,2],[4,2],[5,2],[3,4],[3,5],[5,5],[5,6]]
    for j in range(len(out_wall)):
        if out_wall[j]==[x,y]:
            r=-0.1
    for i in range(len(in_wall)):
        if in_wall[i]==[x,y]:
            r=-0.5
    return r


# Q値の更新
def new_Q(Q,x,y,dir):
    a=0.1
    ganma=0.9
    r=r_value(x,y,dir)
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
    if x==0:
        dir.remove(3)
    if x==X+1:
        dir.remove(1)
    if y==0:
        dir.remove(0)
    if y==Y+1:
        dir.remove(2)
    print("limit:",dir)
    return dir

def p_select(epsilon):
    if epsilon > random.random():
        return True
    else:
        return False

def decide_dir(Q,x,y):
    #epsiron-greedy
    epsilon=0.7
    xy=[]
    xy_max=[]
    limit=dir_limit(x,y)
    # print(limit)
    # limit=[0,1,2,3]
    ran=random.random()
    max_Q=-10
    for i in range(len(limit)):
        # print(Q[x][y][limit[i]])
        if max_Q<Q[x][y][limit[i]]:
            max_Q=Q[x][y][limit[i]]
    if max_Q==-10:
        print("errorrrrr")
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
        clear=1
    elif x==2 and y==5:
        clear=1
    return x,y,status,clear

def screen(Q):
    count=0
    try_1=0
    screen_x=800
    screen_y=800
    cell_size=screen_x/8
    pygame.init()
    screen=pygame.display.set_mode((screen_x,screen_y))
    pygame.display.set_caption("Q-learning")
    # A=np.zeros((int(X/cell_size),int(Y/cell_size)))
    x,y=1,1
    status=1
    while(1):
        screen.fill((0,0,0))
        #vertical line
        for i in range(int(screen_x/cell_size)):
            pygame.draw.line(screen,(0,95,0),(i*cell_size,0),(i*cell_size,screen_y),1)
        #horizontal line
        for j in range(int(screen_y/cell_size)):
            pygame.draw.line(screen,(0,95,0),(0,j*cell_size),(screen_x,j*cell_size),1)
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
                    #color
                    if Q[i][j][k]>=0:
                        color=(0,95,0)
                    else:
                        color=(150,0,0)
                    #直線で表す
                    if Q[i][j][k]==max(Q[i][j]):
                        if k==0:
                            pygame.draw.line(screen,color,(q_x,q_y-(abs(Q[i][j][k])*(cell_size/4))),(q_x,q_y),3)
                        elif k==1:
                            pygame.draw.line(screen,color,(q_x,q_y),(q_x+(abs(Q[i][j][k])*(cell_size/4)),q_y),3)
                        elif k==2:
                            pygame.draw.line(screen,color,(q_x,q_y),(q_x,q_y+(abs(Q[i][j][k])*(cell_size/4))),3)
                        elif k==3:
                            pygame.draw.line(screen,color,(q_x-(abs(Q[i][j][k])*(cell_size/4)),q_y),(q_x,q_y),3)
        pygame.display.update()
        if status==1:
            x,y,status,clear=turn(x,y,status)
            try_1+=1
            print("x,y",x,y)
            if clear==1:
                # x,y=1,1
                x=random.randint(0,X+1)
                y=random.randint(0,Y+1)
                clear=not(clear)
                count+=1
                print("回数:",count,"試行回数:",try_1)
                try_1=0
        elif status==0:
            pass

if __name__=="__main__":
    # main(Q)
    screen(Q)
