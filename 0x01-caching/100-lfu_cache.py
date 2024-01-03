#!/usr/bin/env python3
"""
Defines a basic caching system implementing the LFU cache policy
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    implements a basic caching system using the Least Frequently Used (LFU)
    algorithm
    """
    def __init__(self):
        """Class initialization"""
        super().__init__()
        self.lfu_map = {}

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value
        for the key key if both key and item are not None
        Discards the least frequently used item (LFU algorithm) if the cache
        is full
        Uses the LRU algorithm to discard only the least recently used if
        there is more than one least frequently used item
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS and\
                key not in self.cache_data:
            lfu_item = sorted(self.lfu_map.items(),
                              key=lambda item: item[1])[0]
            lfu_key, _ = lfu_item
            del self.cache_data[lfu_key]
            del self.lfu_map[lfu_key]
            print("DISCARD: {}".format(lfu_key))
        self.cache_data[key] = item
        if key in self.lfu_map:
            self.lfu_map[key] += 1
        else:
            self.lfu_map[key] = 1

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        if key in self.lfu_map:
            self.lfu_map[key] += 1
        return self.cache_data.get(key)
