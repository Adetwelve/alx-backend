#!/usr/bin/env python3
""" BasicCache module """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class
      - inherete BaseCaching
    """

    def put(self, key, item):
        """ assign value to a key """
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ get value of the key """
        return self.cache_data.get(key, None)
