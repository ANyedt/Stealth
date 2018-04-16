#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@version: v1.0
@author: yumu
@software: PyCharm
@file: is_select.py
@time: 2018/3/31 13:12
"""
import sys
from who_is import get_who_page, get_who_is_page
from cms_info import CMS
from dns_info import dns
from nmap_port_info import nmap_scan
from subdomain import get_sub_info, get_domain_info
from robots import get_rebots_info



def select(args, domain):
    if args.all is not None:
        try:
            CMS(domain).is_q_empty()
            CMS(domain).set_gevent()
            dns(domain)
            nmap_scan(domain)
            get_domain_info(domain)
            get_sub_info(domain)
            get_who_page(domain)
            get_who_is_page(domain)
            get_rebots_info(domain)
        except Exception as e:
            print(e)
    else:
        if args.cms is not None:
            CMS(domain).is_q_empty()
            CMS(domain).set_gevent()
        if args.dns is not None:
            dns(domain)
        if args.subdomain is not None:
            get_domain_info(domain)
            get_sub_info(domain)
        if args.info is not None:
            nmap_scan(domain)
        if args.quit is not None:
            sys.exit()
        if args.robots is not None:
            get_rebots_info(domain)
        elif args.whois is not None:
            get_who_is_page(domain)
            get_who_page(domain)






