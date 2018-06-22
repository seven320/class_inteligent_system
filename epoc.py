def epoc(Q):
    #初期化
    x=1
    y=1
    count=0
    while(1):
        count+=1
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
            print("clear")
            break
    return Q,count
