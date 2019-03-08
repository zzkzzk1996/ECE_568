# -*- coding: utf-8 -*-
import scrapy
import json
from jsonpath import jsonpath as jp
from Project_1_568.items import Project1568Item
import pymongo
from time import sleep


class StockApiSpider(scrapy.Spider):
    name = 'stock_real_time'
    allowed_domains = ['alphavantage.co']
    stocks = ['GOOG', 'MSFT', 'YHOO', 'AAPL', 'GS', 'JAVA', 'JPM', 'DELL', 'IBM', 'NVDA']
    start_urls = [
        'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={}&interval=1min&outputsize=full&apikey=VBOSTIUBM79EGTL7'.format(
            stock) for stock in stocks]

    def parse(self, response):
        jsonresponses = json.loads(response.body_as_unicode())
        dicts = jp(jsonresponses, "$..[Time Series (1min)]")[0]
        stockname = jp(jsonresponses, "$.[Meta Data]..")[2]
        item = Project1568Item()
        checker = False
        myclient = pymongo.MongoClient()
        mydb = myclient["stock"]
        mycol = mydb[stockname + "_real_time"]

        for key in dicts.keys():
            last = mycol.find_one({"_id": key})
            if last is None:
                item['open'] = jp(jsonresponses, "$.." + str(key) + "..")[1]
                item['high'] = jp(jsonresponses, "$.." + str(key) + "..")[2]
                item['low'] = jp(jsonresponses, "$.." + str(key) + "..")[3]
                item['close'] = jp(jsonresponses, "$.." + str(key) + "..")[4]
                item['volume'] = jp(jsonresponses, "$.." + str(key) + "..")[5]
                item['_id'] = key
                item['stockname'] = stockname
                yield item
            else:
                checker = True
                break

        # if checker:
        #     sleep(6)
        #     print(stockname)
        #     yield scrapy.Request(response._url, callback=self.parse, dont_filter=True)
