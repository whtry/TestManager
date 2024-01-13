#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Author: whtrys
Email: whtrys@163.com
Description:
"""

from paddleocr import PaddleOCR, draw_ocr
from PIL import Image


def ocr_text(img_path):
    ocr = PaddleOCR(lang="ch")  # need to run only once to download and load model into memory
    return ocr.ocr(img_path, cls=True)[0]


def draw(img_path, result, path):
    image = Image.open(img_path).convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(image, boxes, txts, scores, font_path='../sources/fonts/simfang.ttf')
    im_show = Image.fromarray(im_show)
    im_show.save(f'{path}/result.jpg')


def ocr_result(img_path, draw=False, path=''):
    result = ocr_text(img_path)

    if draw:
        draw_ocr(img_path, result, path)

    final_ocr_txt = ''
    for i in [line[1][0] for line in result]:
        final_ocr_txt += i

    return final_ocr_txt


if __name__ == '__main__':
    img_paths = r"C:\Users\whtrys\Pictures\Screenshots\屏幕截图 2024-01-13 204936.png"
    ocr_result(img_paths, draw=True, path=r'C:\Users\whtrys\Pictures\Screenshots')
