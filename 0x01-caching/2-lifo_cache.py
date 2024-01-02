#!/usr/bin/env python3
"""
Defines LIFOCache class a basic implementation of LIFO cache policy
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    A basic implemtation of LIFO policy in a caching system
    """
    def __init__(self):
        """initialize Parent and Child classes"""
        super().__init__()

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value
        for the key key if both key and item are not None
        Discards the last item put in cache (LIFO algorithm) if the cache
        is full
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-2]
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))

    def get(self, key):
        """
        return the value in self.cache_data linked to key.
        """
        return self.cache_data.get(key)
