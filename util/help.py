#!/usr/bin/env python  
# -*- encoding: utf-8 -*-

""" 
@version: v1.0 
@author: yumu
@software: PyCharm 
@file: help.py 
@time: 2018/3/31 16:44 
"""
import argparse
import sys
from termcolor import colored
from argparse import RawTextHelpFormatter


class Help:
    @classmethod
    def help_info(cls):
            print(colored('usage: python Stealth.py -a domain or python Stealth.py -s -w -D domain', 'yellow'))
            print(colored('  -h  --help      Show help info ', 'blue'))
            print(colored('  -D  --domain    Domain', 'blue'))
            print(colored('  -w  --whois     Collect whois information', 'green'))
            print(colored('  -d  --dns       Collect Dns information', 'grey'))
            print(colored('  -R  --robots    Inquire Robots.txt', 'red'))
            print(colored('  -I  --info      Service Information', 'red'))
            print(colored('  -c  --cms       Cms Information', 'blue'))
            print(colored('  -a  --all       Perform all operations', 'blue'))
            print(colored('  -q  --quit      Quit', 'yellow'))
            sys.exit()
    @classmethod
    def parse_args(cls):
            # description参数可以用于插入描述脚本用途的信息，可以为空
            parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter, prog='python Stealth.py <OPTIONS> '
                                                                                        'domain',
                                             description="Collect message")
            parser.add_argument('-a', '--all', help="Perform all operations", metavar="", required=False, default=None)
            parser.add_argument('-D', '--domain', help="Doamin", metavar="", required=False, default=None)
            parser.add_argument('-d', '--dns', help="Dns information", action='store_true', required=False, default=None)
            parser.add_argument('-s', '--subdomain', help="Subdomain information", action='store_true', required=False, default=None)
            parser.add_argument('-R', '--robots', help="Inquire Robots.txt", action='store_true', required=False, default=None)
            parser.add_argument('-I', '--info', help="Service Information and port Information and System Info", action='store_true', required=False, default=None)
            parser.add_argument('-c', '--cms', help="Cms Information", action='store_true', required=False, default=None)
            parser.add_argument('-w', '--whois', help="Whois information", action='store_true', required=False, default=None)
            parser.add_argument('-q', '--quit', help="Quit", action='store_true', required=False, default=None)
            args = parser.parse_args()
            global HOSTNAME
            HOSTNAME = ''
            for v in vars(args):
                if (vars(args))[v] is not True and (vars(args))[v] is not None:
                        HOSTNAME = (vars(args))[v]
            return args, HOSTNAME
