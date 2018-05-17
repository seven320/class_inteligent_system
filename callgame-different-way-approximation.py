#encoding:utf-8
#京都大学　知能型システム論の授業課題
#メモリを用いたゲームのプログラム
#プレイヤーA、Bをそれぞれ置き、Aが先手Bが後攻として連続で数を言い合い規定の数を相手に言わせたら勝ち
#残り言える数に対してどちらが勝つかをリストに保存。
#tree_list={(残数):(階層、評価値)}
#現在の階層とリストの階層の差によってプレイヤーを判断し、プレイヤーが異なるなら評価値が反転
#リストにまだなければ深さ優先探索を行う
tree_list={}#辞書型

def serch_list(last):
    flag=False
    for key in tree_list.keys():
        if key==last:
            flag==True
        else:pass
    return flag

def min_tree(N,M,now,k):#Bの手番
    value=10
    if serch_list(N-now)==True:#リスト参照
        value_pre,tree_depth=tree_list[N-now]
        if (tree_depth-k)%2==1:
            value=value_pre*(-1)
        else:
            value=value_pre
    else:#リストに未登録
        for i in range(M):
            new=now+i+1
            if(N<new):pass#子なし
            else:#子あり
                if(N==new):#子の端
                    if(value>=1):
                        value=1
                    else:pass
                else:#子の先を探索
                    value1=max_tree(N,M,new,k+1)
                    if(value>=value1):
                        value=value1
                    else:pass
        tree_list[N-now]=(k,value)
    return value

def max_tree(N,M,now,k):
    value=-10
    if serch_list(N-now)==True:#リスト参照
        value_pre,tree_depth=tree_list[N-now]
        if (tree_depth-k)%2==1:
            value=value_pre*(-1)
        else:
            value=value_pre
    else:#リストに未登録
        for i in range(M):
            new=now+i+1
            if(N<new):pass#子なし
            else:#子あり
                if(N==new):#子の端
                    if(value<=-1):
                        value=-1
                    else:pass
                else:#子の先を探索
                    value1=min_tree(N,M,new,k+1)
                    if(value<=value1):
                        value=value1
                    else:pass
        tree_list[N-now]=(k,value)
    # tree_list.append([(N-now),(k-1),value])
    return value

def which_win(N,M):
    win=max_tree(N,M,0,0)
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
print(tree_list)
