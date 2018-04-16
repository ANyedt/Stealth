# Stealth

## Description

**Stealth**是一款收集CMS、WHOIS 、DNS、robots.txt、子域名、端口信息、系统信息、服务信息的工具。

（Stealth is a tool for collecting CMS, WHOIS, DNS, robots.txt, subdomains, port information, system information, and service information.）

![](http://owv5lapar.bkt.clouddn.com/Snipaste_2018-04-15_20-46-02.jpg)



## Operating environment

> python 3+
>
> linux or window
>
> nmap （nmap添加到环境变量中）

## Installation guide

> linux
>
>git clone https://github.com/ANyedt/Stealth.git
>
>cd Stealth
>
>pip install -r requirements.txt
>
>window
>
>git clone https://github.com/ANyedt/Stealth.git 
>
>cd Stealth
>
>pip install -r requirements.txt

## Structure

```
.
├── Stealth.py(主函数)  Main function
├── requirements.txt(依赖库) Dependent library
├── config（配置文件） Profile
│   ├── cms.txt(cms规则文件) Cms rule file
│   ├── config.py(参数配置) Parameter configuration
├── output(输出目录) Output directory
│   ├── whois1.html (whois信息) Whois information
│   └── whois2.html (whois信息) Whois information
│   └── rebots.txt (rebots.txt信息) Rebots.txt information
│   ├── subdomain.xls (子域名信息) Subdomain information
│   └── subdoamin.html (匹配域名) Match domain name
│   └── nmap_info_result.txt (系统信息，端口信息等) System information, port information, etc.
│   └── dns.html (dns信息) DNS information
├── static(静态资源目录) Static resource directory
├── util(功能函数目录)  Function function directory
├── .gitattributes(语言设置) Language settings
└── README.md(说明文档) Documentation
```

## Configuration Guide

配置目录：config/config.py  (Configuration directory: config/config.py)

```python
#!/usr/bin/env python  
# -*- encoding: utf-8 -*-

""" 
@version: v1.0 
@author: yumu

@software: PyCharm 
@file: config.py 
@time: 2018/3/31 17:29 
"""

import sys
import random

# SSL证书验证 (SSL certificate verification)
allow_ssl_verify = True


# -------------------------------------------------
# requests 配置项  (Requests configuration item)
# -------------------------------------------------

# 超时时间 (overtime time)
timeout = 60

# 是否允许URL重定向 (Whether to allow URL redirection)
allow_redirects = True

# 是否使用session （Whether to use session）
allow_http_session = True

# 是否随机使用User-Agent （Whether to use User-Agent randomly）
allow_random_user_agent = False

# 代理配置 （Agent configuration）
allow_proxies = {

}

USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) "
    "Chrome/19.0.1036.7 Safari/535.20",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; "
    "Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322;"
    " .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0;"
    " .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2;"
    " .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727;"
    " InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3)"
    " Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) "
    "Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]


# 随机生成User-Agent （Randomly Generate User-Agent）
def random_user_agent(condition=False):
    if condition:
        return random.choice(USER_AGENTS)
    else:
        return USER_AGENTS[0]


# User-Agent设置 （User-Agent settings）
headers = {
    'User-Agent': random_user_agent(allow_random_user_agent)
}

# nmap命令设置 （Nmap command settings）
nmap_cmd_line = ""
```



## Usage

> 1.第一种是全扫描(收集所有信息)  python  Stealth.py -a  xxx.xxx
>
>  	(1.The first is full scan (collect all information) python Stealth.py -a xxx.xxx)
>
> 2.第二种选择性扫描（收集部分信息） 例如： 收集cms和子域名信息
>
> python  Stealth.py -s -c -D xxx.xxx
>
> ​	(2.The second selective scan (collecting some information) For example: Collecting cms and subdomain information)
>
> 注意： 当我们使用选择性扫描的时候必须加上-D选项，后面接目标
>
> ​	(Note: When we use selective scanning we must add -D option followed by the target)
>
> 在探测cms信息的时候可能会出现连接error，无视即可

### Help information

```shell
usage: python Stealth.py <OPTIONS> domain [-h] [-a] [-D] [-d] [-s] [-R] [-I]
                                          [-c] [-w] [-q]

Collect message

optional arguments:
  -h, --help       show this help message and exit
  -a , --all       Perform all operations
  -D , --domain    Doamin
  -d, --dns        Dns information
  -s, --subdomain  Subdomain information
  -R, --robots     Inquire Robots.txt
  -I, --info       Service Information and port Information and System Info
  -c, --cms        Cms Information
  -w, --whois      Whois information
  -q, --quit       Quit

```



## Demo

> python Stealth.py -a www.baidu.com

### Screenshots

最终结果存放在output目录下。 （The final result is stored in the output directory.）

![Q截图2018041614211](http://owv5lapar.bkt.clouddn.com/20180416142114.png)

![](http://owv5lapar.bkt.clouddn.com/Snipaste_2018-04-15_19-15-31.jpg)

![](http://owv5lapar.bkt.clouddn.com/Snipaste_2018-04-15_19-16-05.jpg)

![](http://owv5lapar.bkt.clouddn.com/Snipaste_2018-04-15_19-16-53.jpg)

![](http://owv5lapar.bkt.clouddn.com/Snipaste_2018-04-15_19-17-09.jpg)

![](http://owv5lapar.bkt.clouddn.com/Snipaste_2018-04-15_20-43-04.jpg)

![Q截图2018041614232](http://owv5lapar.bkt.clouddn.com/20180416142326.png)

---

## CHANGE LOG

>2018/3/31  	vsesion:1.0.0

---

## Project reference

> **wydomain**     https://github.com/ring04h/wydomain

---



## Author

> 红日安全 雨幕（yumu） (Red Day Security Rain Screen (yumu))
>
> 如有其他建议，或者bug反馈，可发邮件到1096905699@qq.com 
>
> (If you have other suggestions or bug feedback, please send an email to 1096905699@qq.com)

![2018041614232](http://owv5lapar.bkt.clouddn.com/yumu02.png)
