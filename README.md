# Roulette Automation System
こちらは、オンラインカジノを自動化するために作成したシステムです。

## ベット方法
基本ロジックは、マーチンゲール法です。  
3カラムのうち、2つを選んでベットします。  
負けた場合は、次のカラムを選んで3倍ベットをする。
目標勝利数に到達した場合、終了します。
ベットするカラムは、前回でた目をもとに選んでいます。

## 実装方法
スクレイピングだとサーバーに負荷がかかるので、光学文字認識(OCR)を用いて、出目を抽出します。
ベットが可能になった段階で、出目の抽出を始めます。  
出目によって、ベットするカラムを選定し、マウスカーソルを操作することでベットさせています。

## デモ
実際に使用している動画が[こちら]( https://youtu.be/ftJ3JTupxS0 )です
