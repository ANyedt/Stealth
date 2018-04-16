#!/usr/bin/env python  
# -*- encoding: utf-8 -*-

""" 
@version: v1.0 
@author: yumu
@software: PyCharm 
@file: welcome.py 
@time: 2018/3/31 13:17 
"""
from termcolor import colored


class Welcome:
    def __init__(self):
        self.__author__, self.__version__, self.__date__ = ("HongRi AnQuan Yumu", "1.0.0", "2018/3/31")
    def headline(self):
        print(colored('                 ☺ Built by {0}  ©{1} Version is {2} ☻                     '.format
                      (self.__author__, self.__date__, self.__version__), 'red',attrs=['bold']))
        print(colored('  █████████   ███████▄██ ███████     ▄████████    ███▄   ▄▄▄████████ ▄█   ███', 'blue'))
        print(colored('  ██        ███        ▀█████  ███▄      ███    ███   ███    ███ █     ██▀▀▀██▄   ███    ███  ', 'red'))
        print(colored('  ██       ▀███       ███▀▀█  █ █ ███ ███      ███         ██████  ███    ███', 'blue'))
        print(colored('  ██                         ███     ▀            ▄██    ███   ███    ███  █   ██  ███ ███', 'red'))
        print(colored('  ██████████         ███     ▀▀███▀▀▀    ▀▀███▀▀▀▀▀█    ███   ███   ▀██    █████████   ', 'blue'))
        print(colored('            █████       ███       █▄▀█████         ██       ██      ███          ███    ███     ███', 'red'))
        print(colored('              ▀███     ███           ██████ ███    ███      ███    ███           ███▌ █        ███', 'blue'))
        print(colored('  ██████████  ▄████▀          ██████████   █████████  ███▀███    ███  █▀  ████', 'red'))
