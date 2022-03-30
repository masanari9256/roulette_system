from OCR import get_color


def judge_bet_timing():
    color = get_color()
    if 60 < color < 85:
        return True


def judge_column(current_number):
    column_number = 0
    judge_number = current_number % 3

    if current_number != 0:
        if judge_number == 0:
            column_number = 3
        elif judge_number == 1:
            column_number = 1
        elif judge_number == 2:
            column_number = 2

    return column_number
