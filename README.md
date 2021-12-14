# PlantMovie
植物班の動画作成用、宇宙線飛ばし用プログラム

## 【ファイルの説明】
* ByeBye_Noise.py (カメラの画素欠け分も消せる)
  * avg.tif (カメラの画素欠け消すのに必要なtif画像)
* Bye_Noise.py　(宇宙線のみ消す)

## 【使い方】
1. 連番画像を一つのフォルダに纏める。
1. 1のフォルダ名を「data」にする。
1. dataフォルダ、ByeBye_Noise.py、avg.tif を同じ階層に置く。(または dataフォルダ、Bye_Noise.py を同じ階層に置く。)
1. プログラムを実行する。
1. 自動的に「outdata」フォルダが作成され、その中に宇宙線を飛ばした連番画像が保存されます。

## 【注意】
*　連番画像は名前の順で取得しています。  
*　プログラムを実行する時点で「outdata」フォルダが存在しているとエラーが出ます。
