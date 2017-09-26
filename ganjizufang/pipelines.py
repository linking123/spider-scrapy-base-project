# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class GanjizufangPipeline(object):

    def open_spider(self, spider):  # 爬虫开始函数
        self.con = sqlite3.connect("ganjizufang.sqlite")
        self.cur = self.con.cursor()   #光标

    def process_item(self, item, spider):  # 从html得到数据，传入item，item被丢到管道中
        # print(spider.name, 'piplelines')
        insert_sql = "insert into ganjizufang (title, money, roomsnum, square, direct, floor, decoration, community, address)" \
                     " values('{}', '{}', '{}',  '{}', '{}', '{}', '{}', '{}', '{}')".format(item['title'], item['money'], item['roomsnum'], item['square'],
                                                item['direct'], item['floor'], item['decoration'], item['community'],item['address'])
        print(insert_sql)
        self.cur.execute(insert_sql)
        self.con.commit()    # 更新和插入操作需要执行提交
        return item

    def spider_close(self, spider):  # 关闭文件、数据库连接
        self.con.close()
