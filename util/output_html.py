#!/usr/bin/env python  
# -*- encoding: utf-8 -*-
""" 
@version: v1.0 
@author: yumu
@software: PyCharm 
@file: output_html.py 
@time: 2018/3/31 18:48 
"""


def out_page(path, style, content):
    with open(path, 'wb+') as f:
        f.write(style.encode('utf-8'))
        f.write(content.encode('utf-8'))
