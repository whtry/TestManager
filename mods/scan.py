#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Author: whtrys
Email: whtrys@163.com
Description: 接入扫描仪并返回试卷图片
"""

import library.twain as scan
# import library.baiduai as aiapi
from tempfile import mkdtemp
import time
import os
import cv2


def main(dpi=150, pixel_type='gray', frame="A4"):
    """
    主函数
    :param frame: 扫描仪裁切大小
    :param dpi: 扫描仪分辨率，默认150
    :param pixel_type: 扫描颜色，可以为 'bw' - 黑白，'gray' - 灰度，'color' - 彩色，默认 'gray'
    :return: 列表，[保存后图片的地址,保存用的临时目录的地址]
    """
    times = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
    t_f = mkdtemp()
    scan_temp_path = '{}\\{}.bmp'.format(t_f, times)


    # 更多参数详见 ./library/twain.py 中的 acquire()
    f = (0, 0, 8.3, 11.7)
    if frame == 'A4':
        f = (0, 0, 8.3, 11.7)
    elif frame == 'H-A3':
        f = (0, 0, 7.71, 10.65)

    choice = scan.acquire(scan_temp_path, dpi=dpi, pixel_type=pixel_type, frame=f)

    if choice is None:
        return None
    else:
        # bmp2jpg
        jpg_path = '{}\\{}.jpg'.format(t_f, times)
        img = cv2.imread(scan_temp_path, -1)
        cv2.imwrite(jpg_path, img)
        return jpg_path, t_f
    # 百度ai文档矫正接入
    # finish_file_path = "{}-finish.jpg".format(scan_temp)
    # with open(finish_file_path, 'wb') as f:
    #     # 请求并保存百度ai的矫正返回
    #     f.write(aiapi.save_back(scan_temp_path))
    #
    # return finish_file_path


if __name__ == '__main__':
    # print(main())
    print(main(frame='A4'))
