#!/usr/bin/env python  
# -*- encoding: utf-8 -*-

""" 
@version: v1.0 
@author: yumu
@software: PyCharm 
@file: http_request.py 
@time: 2018/4/5 8:45 
"""

import config
import requests
import re

if config.allow_http_session:
    requests = requests.session()


def http_get(domain):
    try:
        if config.allow_proxies == {}:
            result = requests.get(domain, headers=config.headers, timeout=config.timeout,
                                  verify=config.allow_ssl_verify).text
        else:
            result = requests.get(domain, headers=config.headers, timeout=config.timeout, proxies=config.allow_proxies,
                                  verify=config.allow_ssl_verify).text
        return result
    except Exception as e:
        print(e)


def http_post(domain, data):
    try:
        if config.allow_proxies == {}:
            result = requests.post(domain, data=data, headers=config.headers, timeout=config.timeout,
                                   verify=config.allow_ssl_verify).text
        else:
            result = requests.get(domain, data=data, headers=config.headers, timeout=config.timeout,
                                  proxies=config.allow_proxies,
                                  verify=config.allow_ssl_verify).text
        return result
    except Exception as e:
        print(e)


def is_domain(domain):
    domain_regex = re.compile(
        r'(?:[A-Z0-9_](?:[A-Z0-9-_]{0,247}[A-Z0-9])?\.)+(?:[A-Z]{2,6}|[A-Z0-9-]{2,}(?<!-))\Z', re.IGNORECASE)
    return True if domain_regex.match(domain) else False
