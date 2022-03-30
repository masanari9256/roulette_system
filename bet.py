import pyautogui as pgui
from time import sleep


def bet_to_first_column(martin_times):
    if martin_times == 0:
        pgui.moveTo(x=1036, y=206)
        pgui.click()
        pgui.hotkey("backspace")
        pgui.hotkey("backspace")

        # チップを移動
        pgui.moveTo(x=864, y=547)
        sleep(0.5)
        pgui.dragRel(0, -30, 0.5, button="left")
    else:
        # 登録してある前のベットを3回クリック
        y = 206 + (martin_times - 1) * 22
        pgui.moveTo(x=1036, y=y)
        pgui.click()

        # チップを移動
        pgui.moveTo(x=864, y=547)
        sleep(0.5)
        pgui.dragRel(0, -30, 0.5, button="left")


def bet_to_second_column(martin_times):
    if martin_times == 0:
        pgui.moveTo(x=1036, y=206)
        pgui.click()
        pgui.hotkey("backspace")
        pgui.hotkey("backspace")

    else:
        # 登録してある前のベットを3回クリック
        y = 206 + (martin_times - 1) * 22
        pgui.moveTo(x=1036, y=y)
        pgui.click()


def bet_to_third_column(martin_times):
    if martin_times == 0:
        pgui.moveTo(x=1036, y=206)
        pgui.click()
        pgui.hotkey("backspace")
        pgui.hotkey("backspace")

        # チップを移動
        pgui.moveTo(x=864, y=470)
        sleep(0.5)
        pgui.dragRel(0, 30, 0.5, button="left")
    else:
        # 登録してある前のベットを3回クリック
        y = 206 + (martin_times - 1) * 22
        pgui.moveTo(x=1000, y=y)
        pgui.click()

        # チップを移動
        pgui.moveTo(x=864, y=470)
        sleep(0.5)
        pgui.dragRel(0, 30, 0.5, button="left")


def bet(bet_column_number, martin_times):
    # if bet_column_number == 1:
    #     bet_to_first_column(martin_times)
    # elif bet_column_number == 2:
    #     bet_to_second_column(martin_times)
    # elif bet_column_number == 3:
    #     bet_to_third_column(martin_times)
    bet_to_second_column(martin_times)


if __name__ == '__main__':
    sleep(2)
    # pgui.moveTo(x=1000, y=310)
    # pgui.doubleClick()
    # pgui.click()
    # sleep(0.5)
    # pgui.hotkey("backspace")
    # pgui.hotkey("backspace")
    # sleep(1)
    # pgui.moveTo(x=840, y=540)
    # pgui.dragRel(0, 30, 0.5, button="left")
    bet(bet_column_number=2, martin_times=4)
