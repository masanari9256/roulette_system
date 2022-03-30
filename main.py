from logic import judge_bet_timing
from logic import judge_column
from OCR import get_roulette_number
from bet import bet

from time import sleep
from dotenv import load_dotenv
import os
import sys
import shutil
import random

# 環境変数の読み込み
load_dotenv()

def mkdir_for_save_screenshot():
    save_path = os.environ['SAVE_PATH']
    save_folder_name = 'Roulette_picture'
    path = save_path + save_folder_name

    shutil.rmtree(path)
    os.makedirs(path, exist_ok=True)


if __name__ == '__main__':
    # roulette_number = get_roulette_number()
    # print(number)

    # 目標勝利数を決める
    TARGET_WIN_COUNT = int(os.environ['TARGET_WIN_COUNT'])
    MAX_MARTIN_TIMES = int(os.environ['MAX_MARTIN_TIMES'])
    MAX_LOSE_COUNT = int(os.environ['MAX_LOSE_COUNT'])

    # 変数の宣言
    bet_timing = 0
    previous_number = 0
    martin_times = 0
    judge_flag = 0
    win_count = 0
    lose_count = 0
    previous_column = 0

    mkdir_for_save_screenshot()

    while True:
        while True:
            if judge_bet_timing():
                current_number = int(get_roulette_number())
                bet_timing = 1
                break

        if bet_timing == 1:
            bet_timing = 0
            print("ルーレットの前の出目は %d です" % previous_number)
            print("ルーレットの出目は %d です" % current_number)
            current_column = judge_column(current_number)
            # テスト用
            # current_column = random.randint(0, 3)
            print("前のカラムは %d です" % previous_column)
            print("今のカラムは %d です\n" % current_column)

            # テスト用
            # previous_column = random.randint(0, 3)
            # judge_flag = 1

            # 勝敗の判定
            # 負けたらマーチンする
            if judge_flag == 1:
                if current_column != 2 and current_column != 0:
                    win_count += 1
                    martin_times = 0
                    print("%d 回目の勝ち\n" % win_count)
                    # 10勝ごとに10分休む
                    if win_count < TARGET_WIN_COUNT and win_count % 10 == 0:
                        sleep(60 * 10)
                else:
                    martin_times += 1
                    if MAX_MARTIN_TIMES < martin_times:
                        lose_count += 1
                        martin_times = 0
                        print("%d 回目の負け\n" % lose_count)
                    else:
                        print("%d 回目のマーチンをします\n" % martin_times)

                judge_flag = 0

            # 勝敗数が目標に達したら終了
            if lose_count != MAX_LOSE_COUNT and win_count != TARGET_WIN_COUNT:
                pass
            else:
                print("==========================")
                print("勝ち : %d 回" % win_count)
                print("負け : %d 回" % lose_count)
                print("==========================")

                sys.exit()

            # 0じゃない場合はベットする
            if current_column == 0:
                pass
            else:
                bet(bet_column_number=current_column, martin_times=martin_times)
                judge_flag = 1

        previous_number = current_number
        previous_column = current_column
        sleep(15)
