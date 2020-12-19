import cv2
import numpy as np


def main():

    # 1.读取图片 二值操作
    img_src = cv2.imread("123.jpg")
    img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
    ret, img_threshold = cv2.threshold(img_gray, 0, 255,
                                       cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 2.创建操作核
    kernel = np.ones((5, 5), np.uint8)

    # 3.执行开操作
    img_open = cv2.morphologyEx(img_threshold, cv2.MORPH_OPEN, kernel)

    # 4.显示结果
    cv2.imshow("img_src", img_src)
    cv2.imshow("img_threshold", img_threshold)
    cv2.imshow("img_open", img_open)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

