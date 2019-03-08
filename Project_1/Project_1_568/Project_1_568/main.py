# import json

from scrapy import cmdline
import time
from subprocess import Popen
import logging
from multiprocessing import Process


cmdline.execute('scrapy crawl stock_api'.split())
# cmdline.execute('scrapy crawl stock_real_time'.split())
# def loop():
#     while True:
#         sleep(60)
# execute('scrapy crawl stock_real_time'.split())
#         Popen('scrapy crawl Project_1_568/spiders/stock_real_time.py')
#
#
# if __name__ == '__main__':
#     Popen('scrapy crawl stock_real_time')
#     # execute('scrapy crawl stock_real_time'.split())
#     loop()

confs = [
    {
        "spider_name": "stock_real_time",
        "frequency": 1,
    },
]


def start_spider(spider_name, frequency):
    args = ["scrapy", "crawl", spider_name]
    while True:
        start = time.time()
        p = Process(target=cmdline.execute, args=(args,))
        p.start()
        p.join()
        logging.debug("### use time: %s" % (time.time() - start))
        time.sleep(frequency)


if __name__ == '__main__':
    for conf in confs:
        process = Process(target=start_spider,
                          args=(conf["spider_name"], conf["frequency"]))
        process.start()
        time.sleep(60)
