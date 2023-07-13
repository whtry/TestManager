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


def draw(img_path, result):
    image = Image.open(img_path).convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(image, boxes, txts, scores, font_path='sources/fonts/simfang.ttf')
    im_show = Image.fromarray(im_show)
    im_show.save('result.jpg')
