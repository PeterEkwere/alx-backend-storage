#!/usr/bin/env python3
"""
    THis Module Contains the cache class
    author: Peter Ekwere
"""
import redis
from typing import Union
import uuid


class Cache:
    """
    This is the cache Class
    """

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        THis method  store the input data in Redis using a random key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
