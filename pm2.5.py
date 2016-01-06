#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
from sgmllib import SGMLParser
import sys

def pm25(city):
    '''
    city: 城市拼音
    '''
    url = 'http://www.pm25.com/%s.html' % (city,)
    rep = urllib2.urlopen(url)
    content = rep.read()
    if content:
        pm = MySGMLParser()
        pm.feed(content)
        pm.close()
        return pm.data


class MySGMLParser(SGMLParser):

    def reset(self):
            # 调用原来的函数resert
        SGMLParser.reset(self)
        # 数据存放的位置
        self.data = None
        self.lable = False

    # 查找的标签(start_ +　标签）表示查找的那个标签（参数是固定的）
    def start_a(self, attrs):
        # 查找对象的标签里面的属性(此处用到了列表解析)
        pm = [v for k, v in attrs if k == 'class' and v == 'bi_aqiarea_num']
        # 判断href是不是存在
        if pm:
            self.lable = True

    # 查找结束的标志
    def end_a(self):
        self.lable = False
    # 处理信息数据的地方

    def handle_data(self, data):
        # 判断标签数不超找完毕
        if self.lable:
            data = data.strip()
            self.data = data


if __name__ == '__main__':
    name = sys.argv[1]
    pm = pm25(name)
    print pm
