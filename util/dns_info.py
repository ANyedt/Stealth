#!/usr/bin/env python  
# -*- encoding: utf-8 -*-

""" 
@version: v1.0 
@author: yumu
@software: PyCharm 
@file: dns_info.py 
@time: 2018/4/5 9:26 
"""
import os
from http_request import http_get, is_domain
from bs4 import BeautifulSoup
from output_html import out_page


def dns(domain):
    if is_domain(domain):
        url = 'https://who.is/dns/{0}'.format(domain)
        try:
            result = http_get(url)
            bs = BeautifulSoup(result, 'html.parser')
            content = bs.find('table')
            script_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
            finally_path = os.path.join(script_path, 'output/{0}'.format("dns.html"))
            sty = '<head><meta charset="UTF-8"><link href="../static/Bootstrap.css" rel="stylesheet" ' \
                  'type="text/css" /><link href="../static/main.css" rel="stylesheet" type="text/css" /></head>'
            out_page(finally_path, sty, content)

        except Exception as e:
            print(e)



