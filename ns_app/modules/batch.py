import schedule

#01 定期実行する関数を準備
def ppap():
    print("タスク実行中")
    
#02 スケジュール登録(01実行関数の引数はdoメソッドの第二引数として指定)
def task():
    print("come")
    schedule.every(3).seconds.do(ppap)
    while True:
        schedule.run_pending()
        # time.sleep(1)
    print("come too")