#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Author: whtrys
Email: whtrys@163.com
Description:
"""

import fitz
import os


def pic2pdf(img_path, pdf_path):
    """
    图片转pdf
    @param img_path: 图片所在目录
    @param pdf_path:
    @return:
    """
    doc = fitz.open()

    # 循环path中的文件，可import os 然后用 for img in os.listdir(img_path)实现
    # 这里为了让文件以1，2，3的形式进行拼接，就偷懒循环文件名中的数字。
    for img in os.listdir(img_path):
        img_file = img_path + '/' + img
        img_doc = fitz.open(img_file)
        pdf_bytes = img_doc.convert_to_pdf()
        pdf_name = img + '.pdf'
        img_pdf = fitz.open(pdf_name, pdf_bytes)
        doc.insert_pdf(img_pdf)
    doc.save(f'{pdf_path}/combined.pdf')
    doc.close()


if __name__ == '__main__':
    pic2pdf(img_path=r"D:\pics2pdf\docs", pdf_path=r'D:\pics2pdf\test')
