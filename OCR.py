import pyautogui as pgui
import cv2
import re
from PIL import Image
import pyocr
import pyocr.builders

# OCRのツールを定義
tools = pyocr.get_available_tools()
tool = tools[0]


def shot(x, y, w, h):
    return pgui.screenshot(region=(x, y, w, h))


def get_roulette_number():
    # 保存するときの情報
    save_folder_name = 'Roulette_picture'
    save_file_name = 'Roulette_number.png'

    s = shot(1940, 343, 45, 27)
    s.save(save_folder_name + '/' + save_file_name)

    # モノクロにする
    img_gray = cv2.imread('./Roulette_picture/Roulette_number.png', 0)
    img_gray_gray = cv2.bitwise_not(img_gray)
    cv2.imwrite('./Roulette_picture/Roulette_number_gray.png', img_gray_gray)

    # しきい値をあげる
    ret, img_thresh = cv2.threshold(img_gray_gray, 0, 255, cv2.THRESH_OTSU)
    cv2.imwrite('./Roulette_picture/Roulette_number_threshold.png', img_thresh)

    img_roulette_number_threshold = Image.open('./Roulette_picture/Roulette_number_threshold.png')

    roulette_number = tool.image_to_string(
        img_roulette_number_threshold,
        lang='eng',
        builder=pyocr.builders.DigitBuilder(tesseract_layout=6)
    )

    # roulette_number = re.sub(r"/D", "", roulette_number)

    # if roulette_number == "":
    #     roulette_number = 0

    return roulette_number


def get_color():
    # 保存するときの情報
    save_folder_name = 'Roulette_picture'
    save_file_name = 'Roulette_color.png'

    s = shot(1940, 800, 5, 5)
    s.save(save_folder_name + '/' + save_file_name)

    img = cv2.imread("./Roulette_picture/Roulette_color.png")

    # L*A*B色空間に変換
    img_Lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)

    # 平滑化
    img_Lab = cv2.GaussianBlur(img_Lab, (5, 5), 3)

    # split photo into 3 channels (L, a, b)
    img_L, img_a, img_b = cv2.split(img_Lab)
    color = img_a[0, 0]

    return color


if __name__ == '__main__':
    number = get_roulette_number()
    print(number)
