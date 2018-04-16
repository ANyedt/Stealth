#!/usr/bin/env python  
# -*- encoding: utf-8 -*-

""" 
@version: v1.0 
@author: yumu
@software: PyCharm 
@file: subdomain.py 
@time: 2018/4/5 17:41 
"""
import os
import requests
import config 
import xlwt
import re
from http_request import is_domain, http_get
from bs4 import BeautifulSoup
from output_html import out_page


def get_sub_info(domain):
    session = requests.session()
    if is_domain(domain):
        url = 'http://i.links.cn/subdomain/'
        new_value = []
        try:
            payload = {
                'b2': 1,
                'b3': 1,
                'b4': 1,
                'domain': domain
            }
            result = session.post(url, data=payload, headers=config.headers).text
            bs = BeautifulSoup(result, 'html.parser')
            content = bs.find_all('a', attrs={'rel': "nofollow"})
            if content is not None:
                for i in content:
                    if i.text:
                        new_value.append(i.text)
            f = xlwt.Workbook(encoding='utf-8', style_compression=0)
            sheet = f.add_sheet('sub', cell_overwrite_ok=True)
            script_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
            finally_path = os.path.join(script_path, 'output/{0}'.format("subdomain.xls"))
            if len(new_value) != 0:
                for index, item in enumerate(new_value):
                    sheet.write(index, 0, item)
                f.save(finally_path)

        except Exception as e:
            print(e)


def get_domain_info(domain):
    if is_domain(domain):
        url = 'http://searchdns.netcraft.com/?restriction=site+contains&host={0}&lookup=wait..&position=limited'\
            .format(domain)
        try:
            headers = {
                'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
            }
            result = requests.get(url, headers=headers).text
            bs = BeautifulSoup(result, 'html.parser')
            content = bs.find('div', id="content")
            if content is not None:
                rule = re.compile('(\/\?host=)')
                finally_result = rule.sub('http://searchdns.netcraft.com/?host=', content.prettify())
                script_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
                finally_path = os.path.join(script_path, 'output/{0}'.format("subdoamin.html"))
                sty = '<head><meta charset="UTF-8"><link href="../static/subdomain.css" rel="stylesheet" ' \
                    'type="text/css" /></head>'
                out_page(finally_path, sty, finally_result)

        except Exception as e:
            print(e)
