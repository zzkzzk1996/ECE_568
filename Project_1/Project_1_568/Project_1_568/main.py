# import json

from scrapy import cmdline
import time
import logging
from multiprocessing import Process

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
    # for history start
    # cmdline.execute('scrapy crawl stock_api'.split())
    # for real-time start
    for conf in confs:
        process = Process(target=start_spider,
                          args=(conf["spider_name"], conf["frequency"]))
        process.start()
        time.sleep(60)
