# -*- coding: utf-8 -*-
"""
爬虫运行
"""


from scrapy.cmdline import execute

execute(["scrapy", "crawl", "jd_product"])
