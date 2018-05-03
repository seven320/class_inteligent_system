#encoding:utf-8
#京都大学　知能型システム論の授業課題
#min-max探索方を用いたゲームのプログラム
#プレイヤーA、Bをそれぞれ置き、Aが先手Bが後攻として連続で数を言い合い規定の数を相手に言わせたら勝ち

#１ターンに行っていい最大数をM
M=2　
#相手に言わせたい数をNとする。
N=6
# その段階の深さをｋ
k=0
#その段階で言っている数字をnow
now=0
class setting:
    

def min(N,M,now):#Bの手番
    for i in range(M):
        new=now+i
        #葉っぱの先端
        if(N==new):
            value=-1
        else:
            max(N,M,)




    return value

def max():

    return value
