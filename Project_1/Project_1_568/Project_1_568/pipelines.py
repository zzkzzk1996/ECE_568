# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo


class Project1568Pipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        # collectionname = self.client.stock[item['stockname']]
        collectionname = self.client.stock[item['stockname'] + "_real_time"]
        collectionname.insert_one(item)
        return item

    def close_spider(self, spider):
        print("finished once")
        self.client.close()
