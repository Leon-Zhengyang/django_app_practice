# import schedule
# import time

# #hello worldを出力する関数の作成
# def hello():
#     print("Hello World!!")

# #1分ごとにhello ()関数を呼び出す
# schedule.every(5).seconds.do(hello)

# #whileループを使用してこの関数を繰り返し呼び出す
# while True:
#     # タスクを実行させるための処理
#     schedule.run_pending()
#     time.sleep(2) #2秒間停止する。