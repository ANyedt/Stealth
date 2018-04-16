#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@version: v1.0
@author: yumu
@software: PyCharm
@file: robots.py
@time: 2018/3/31 13:12
"""
import os
from http_request import http_get, is_domain


def get_rebots_info(domain):
    if is_domain(domain):
        try:
            finally_url = "http://" + domain + '/robots.txt'
            result = http_get(finally_url)
            script_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
            finally_path = os.path.join(script_path, 'output/{0}'.format("rebots.txt"))
            if result:
                with open(finally_path, 'wb') as f:
                    f.write(result.encode('utf-8'))
        except Exception as e:
            print(e)
