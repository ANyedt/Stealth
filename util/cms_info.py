#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@version: v1.0
@author: yumu
@software: PyCharm
@file: cms_info.py
@time: 2018/3/31 18:48
"""
import os
import requests
import hashlib
import gevent
import time
import config as config
from gevent.queue import Queue


class CMS(object):
    def __init__(self, url):
        self.q = Queue()
        self.url = url.rstrip("/")
        if self.url is None:
            self.url = url
        script_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        finally_path = os.path.join(script_path, 'config/{0}'.format("cms.txt"))
        with open(finally_path, 'r',encoding="gbk") as f:
            for line in f:
                self.q.put(line.split('|'))

    def get_md5(self, content):
        md = hashlib.md5()
        md.update(content.encode('utf-8'))
        return md.hexdigest()

    def clear_queue(self):
        while not self.q.empty():
            self.q.get()

    def run(self):
        rule_list = self.q.get()
        finally_url = "http://" + self.url + rule_list[0]
        data = ''
        try:
            result = requests.get(finally_url, headers=config.headers, timeout=10)
            if result.status_code != 200:
                return
            data = result.text
            if data is None:
                return

        except Exception as e:
            print(e)
        md5 = self.get_md5(data)
        html_md5 = (rule_list[2]).strip()

        if md5 == html_md5:
            cms_name = rule_list[1]
            script_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
            finally_path = os.path.join(script_path, 'output/{0}'.format("cms_info.txt"))
            with open(finally_path, "w") as f:
                f.write("Target Cms Name:%s ,Rule:%s md5:%s" % (cms_name, finally_url, rule_list[2]))
            self.clear_queue()
            return True

    def is_q_empty(self):
        while not self.q.empty():
            self.run()

    def set_gevent(self, maxsize=100):
        start = time.clock()
        all = [gevent.spawn(self.is_q_empty()) for i in range(maxsize)]
        gevent.joinall(all)
        end = time.clock()
        script_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        finally_path = os.path.join(script_path, 'output/{0}'.format("cms_info.txt"))
        with open(finally_path, "a+") as f:
            f.write("\n")
            f.write("cost: %f s" % (end - start))
