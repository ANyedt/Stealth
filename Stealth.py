#!/usr/bin/env python  
# -*- encoding: utf-8 -*-

""" 
@version: v1.0 
@author: yumu
@software: PyCharm 
@file: Stealth.py 
@time: 2018/3/31 13:12 
"""
import os
import sys
script_path = os.path.dirname(os.path.abspath(__file__))
en_path = os.path.join(script_path, 'util')
config_path = os.path.join(script_path, 'config')
sys.path.append(en_path)
sys.path.append(config_path)
from welcome import Welcome
from help import Help
from is_select import select

if __name__ == '__main__':
    script_path = os.path.dirname(os.path.abspath(__file__))
    _cache_path = os.path.join(script_path, 'output/')
    if not os.path.exists(_cache_path):
        os.makedirs(_cache_path, mode=0o777)
    (arg, domain) = Help.parse_args()
    if domain == '':
        Welcome().headline()
        Help.help_info()
    else:
        select(arg, domain)





