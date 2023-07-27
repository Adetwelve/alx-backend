#!/bin/usr/env python3
""" FIFOCache module """
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ fifo class inherite basecaching """
    def __init__(self):
        """ initialiaze """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ update the dictionary """
        if key is not None and item is not None:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, first_value = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """ get value of new dictionary """
        return self.cache_data.get(key, None)
