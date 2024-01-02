#!/usr/bin/env python3
"""
Defines FIFOCache class that implements a basic FIFO cache policy
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    implements a basic version of the FIFO cache algorithm
    """
    def __init__(self):
        """initialize Parent and child classes"""
        super().__init__()

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value
        for the key key if both key and item are not None.
        Discards the first item put in cache (FIFO algorithm) if cache
        is full
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            first_in = list(self.cache_data.keys())[0]
            del self.cache_data[first_in]
            print("DISCARD: {}".format(first_in))

    def get(self, key):
        """
        return the value in self.cache_data linked to key.
        """
        return self.cache_data.get(key)
