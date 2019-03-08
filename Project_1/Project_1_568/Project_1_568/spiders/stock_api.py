# -*- coding: utf-8 -*-
import scrapy
import json
from jsonpath import jsonpath as jp
from Project_1_568.items import Project1568Item


class StockApiSpider(scrapy.Spider):
    name = 'stock_api'
    allowed_domains = ['alphavantage.co']
    stocks = ['GOOG', 'MSFT', 'YHOO', 'AAPL', 'GS', 'JAVA', 'JPM', 'DELL', 'IBM', 'NVDA']
    start_urls = [
        'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&outputsize=full&apikey'
        '=VBOSTIUBM79EGTL7'.format(stock) for stock in stocks]

    def parse(self, response):
        jsonresponses = json.loads(response.body_as_unicode())
        dicts = jp(jsonresponses, "$..[Time Series (Daily)]")[0]
        stockname = jp(jsonresponses, "$.[Meta Data]..")[2]
        item = Project1568Item()
        for key in dicts.keys():
            item['open'] = jp(jsonresponses, "$.." + str(key) + "..")[1]
            item['high'] = jp(jsonresponses, "$.." + str(key) + "..")[2]
            item['low'] = jp(jsonresponses, "$.." + str(key) + "..")[3]
            item['close'] = jp(jsonresponses, "$.." + str(key) + "..")[4]
            item['volume'] = jp(jsonresponses, "$.." + str(key) + "..")[5]
            item['_id'] = key
            item['stockname'] = stockname
            yield item
