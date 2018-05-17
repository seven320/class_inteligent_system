# 迷路の最適解をマルコフ決定論を用いて解く

import matplotlib.pyplot as plt
import numpy as np

#size setting

# print("迷路のサイズを入力してください　X:",end="")
# x=int(input())
# print("迷路のサイズを入力してください　Y:",end="")
# y=int(input())
X=10
Y=10
# plt.plot(x_1,y_1)
for i in range(X+1):
    plt.vlines(i,0,Y,alpha=0.5)#alpha:透過率
for j in range(Y+1):
    plt.hlines(j,0,X,alpha=0.5)
plt.axis([0,X,0,Y])#plt.axis(xmin, xmax, ymin, ymax)



def input_x_y(str,X,Y,ban_list):
    while(True):
        while(True):
            print("{0}の座標指定X:".format(str),end="")
            x=int(input())
            if x<=X:
                break
            else:
                print("Xの座標が大きすぎます。")
        while(True):
            print("{0}の座標指定Y:".format(str),end="")
            y=int(input())
            if y<=Y:
                break
            else:
                print("Yの座標が大きすぎます。")
        list=[x,y]
        if list in ban_list:
            print("入力に重複があります")
        else:
            break
    return list

def print_setting(status,x_y):
    pass

# setting
ban_list=[[0,1]]
start=input_x_y("スタート",X,Y,ban_list)
# goal=input_x_y("ゴール",X,Y,ban_list)
# obj_num=3
# obj=[]
# for i in range(obj_num):
#     obj.append(input_x_y("障害物"+str(i),X,Y,ban_list))


plt.plot(start[0],start[1],"ro")
plt.plot(goal[0],goal[1],"g^")
plt.show()
