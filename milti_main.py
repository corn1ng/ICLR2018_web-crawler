# -*- coding:utf8 -*-
# author: Brett
from queue import Queue
from multi_thread import Consumer
from multi_thread import Product

if __name__ == "__main__":
    queue = Queue(100)
    consumer = Consumer("consumer", queue)
    product = Product("product", queue)
    consumer.start()
    product.start()


