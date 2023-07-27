#!/bin/usr/env python3
""" LIFOCache module """
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO Cache class Inheriting BaseCaching """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Update the cache """
        if key is None and item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, last_item = self.cache_data.popitem(True)
                print(f'DISCARD: {last_key}')
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """ Get key from the cache """
        return self.cache_data.get(key, None)
