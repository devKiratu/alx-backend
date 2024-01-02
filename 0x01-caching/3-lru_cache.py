#!/usr/bin/env python3
"""
Defines class LRUCache the implements a basic LRU cache policy
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    implements a basic caching system using the Least Reacently Used policy
    """
    def __init__(self):
        """class initialization"""
        super().__init__()
        self.index = 0
        self.access_map = {}

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value
        for the key key if both key and item are not None.
        Discards the least recently used item (LRU algorithm) if the
        cache is full
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if key not in self.access_map:
            self.access_map[key] = self.index
            self.index += 1
        else:
            self.index += 1
            self.access_map[key] = self.index

        if len(self.cache_data) > self.MAX_ITEMS:
            lru_item_key, _ = sorted(self.access_map.items(),
                                     key=lambda item: item[1])[0]
            del self.cache_data[lru_item_key]
            del self.access_map[lru_item_key]
            print("DISCARD: {}".format(lru_item_key))

    def get(self, key):
        """
        return the value in self.cache_data linked to key.
        """
        if key in self.access_map:
            self.index += 1
            self.access_map[key] = self.index
        return self.cache_data.get(key)
