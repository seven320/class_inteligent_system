#encoding:utf-8
#京都大学　知能型システム論の授業課題
#min-max探索方を用いたゲームのプログラム
#プレイヤーA、Bをそれぞれ置き、Aが先手Bが後攻として連続で数を言い合い規定の数を相手に言わせたら勝ち

def min_tree(N,M,now):#Bの手番
    value=1
    for i in range(M):
        new=now+i+1
        if(N<new):#子なし
            pass
        else:#子あり
            if(N==new):#子の端
                if(value>=1):
                    value=1
                else:pass
            else:#子の先を探索
                value1=max_tree(N,M,new)
                if(value>=value1):
                    value=value1
                else:pass
    return value

def max_tree(N,M,now):
    value=-10
    for i in range(M):
        new=now+i+1
        if(N<new):#子なし
            pass
        else:#子あり
            if(N==new):#子の端
                if(value<=-1):
                    value=-1
                else:pass
            else:#子の先を探索
                value1=min_tree(N,M,new)
                if(value<=value1):
                    value=value1
                else:pass
    return value

print()

def which_win(N,M):
    win=max_tree(N,M,0)
    print("M={0},N={1}の場合は".format(M,N))
    if win==1:
        print("先手必勝")
    else:
        print("後手必勝")
#１ターンに言っていい最大数をM
#相手に言わせたい数をNとする。
#その段階で言っている数字をnow
for i in range(9,16):
    which_win(N=i,M=4)
