#!/usr/bin/env python3
"""
Defines BasicCache class for demonstrating a basic cace system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A basic implementation of a Caching System
    """
    def __init__(self):
        """initialize child and parent classes"""
        super().__init__()

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value
        for the key key if both key and item are not None
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        return self.cache_data.get(key)
