#encoding:utf-8
#http://www.mwsoft.jp/programming/python/python_aws.html
# https://qiita.com/ketancho/items/6d5137b48d94eced401e

import boto3
from PIL import Image

#encoding:utf-8
import tweepy

#親ディレクトリにあるアカウント情報へのパス
import sys,os
pardir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(pardir)

#account情報をaccount.pyからロード
from account import account #load account
auth=account.Initialize()
api = tweepy.API(auth)
twitter_id=account.id()

# ツイートのみ
# api.update_status(status="test by tweepy")#status

import manuscript
#原稿のロードのためにclass継承　from manuscript.py
tweet=manuscript.Manuscript()

# 指定された写真の範囲からランダムに選ぶ
import random
min=1
max=tweet.max_num()#写真と記事の割り振り番号の最大値
num=random.randint(min,max)
num_padded='{0:03d}'.format(num)#ゼロパディング:0で３桁左詰する。 example 1→001

# # #一番から順にツイートする機能
# # tweetnum=outputtext.Tweet_num()
# # num=tweetnum.load()#今ツイートする番号を取得
# # tweetnum.write(num+1)#次のツイート番号を返却
# # num_padded='{0:03d}'.format(num)

s3=boto3.resource("s3")
# boto3.DEFAULT_SESSION

bucket=s3.Bucket("photofortweet")
# obj=bucket.Object("forbot/001.jpg")
bucket.download_file("forbot/"+str(num_padded)+".jpg","/Users/001jpg")
# img = Image.open("001.jpg")


# 画像付きツイート
pic="/Users/001jpg" #画像を投稿するなら画像のパス
status=tweet.manus(num-1)+"\ninstagram.com/ken_4y4"#ツイート内容
api.update_with_media(filename=pic,status=status)
print("tweet No:"+str(num))
