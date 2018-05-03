#encoding:utf-8
#京都大学　知能型システム論の授業課題
#min-max探索方を用いたゲームのプログラム
#プレイヤーA、Bをそれぞれ置き、Aが先手Bが後攻として連続で数を言い合い規定の数を相手に言わせたら勝ち

def min_tree(N,M,now):#Bの手番
    value=1
    for i in range(M):
        new=now+i+1
        #葉っぱの先端
        if(N<new):
            pass
        else:
            if(N==new):
                if(value>=1):
                    value=1
                else:pass
            else:
                value1=max_tree(N,M,new)
                if(value>=value1):
                    value=value1
                else:pass
    return value

def max_tree(N,M,now):
    value=-10
    for i in range(M):
        new=now+i+1
        #葉っぱの先端
        if(N<new):
            pass
        else:
            if(N==new):
                if(value<=-1):
                    value=-1
                else:pass
            else:
                value1=min_tree(N,M,new)
                if(value<=value1):
                    value=value1
                else:pass
    return value
#１ターンに行っていい最大数をM
M=2
#相手に言わせたい数をNとする。
N=6
# その段階の深さをｋ
k=0
#その段階で言っている数字をnow
now=0
print(max_tree(N,M,0))
