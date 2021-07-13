"""
・「data」フォルダに宇宙線を飛ばしたい連番画像を入れて実行してください。
・出力結果は「outdata」というフォルダの中に入ります。(outdataフォルダは勝手に作成されます)
・連番画像は00番から始まるものと想定しています。
・偶数・奇数番という表現は連番画像の番号の偶奇を考えています。
"""
import os
from PIL import Image
import glob
import numpy as np
#import datetime
#------------------------

def Bye_noise(i, j):
    #----------画像の読み込み--------------
    im = np.array(Image.open(even_imgName[j]))
    even_img.append(im)
    im = np.array(Image.open(odd_imgName[i]))
    odd_img.append(im)
    #----------計算--------------
    #culim = np.uint16(np.minimum(odd_img[i], even_img[i]))
    culim = np.minimum(odd_img[i], even_img[i])
    culim = culim - avg_im + np.mean(avg_im)
    culim = np.uint16(culim)
    newim = Image.fromarray(culim)
    newim.save('outdata/{:04}.tif'.format(num))#4桁0詰め


#----------出力用フォルダの作成--------------
path = 'outdata'
os.mkdir(path)

#///////////------準備------///////////
even_img = [] #配列の準備
odd_img = [] #配列の準備
avg_im = np.array(Image.open('avg.tif'))#謎の発光画素消し用

#///////////------処理ステップ------///////////
imgName = sorted(glob.glob('data/*.tif'))#dataフォルダ内のtif画像の名前を取得
even_imgName = imgName[0::2] #偶数番ファイル名だけ抜きだし
odd_imgName = imgName[1::2] #奇数番ファイル名だけ抜きだし

#------連番画像が奇数枚の時-------(最初の一枚は計算しない)
if len(even_imgName) != len(odd_imgName):
    print("処理中です！")
    for num in range(len(odd_imgName)):
        Bye_noise(num, num+1)
    print("お待たせしました、終わりました")

#------連番画像が偶数枚の時-------
else:
    print("処理中です！")
    for num in range(len(odd_imgName)):
        Bye_noise(num, num)
    print("お待たせしました、終わりました")
