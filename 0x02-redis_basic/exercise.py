#!/usr/bin/env python3
"""
    THis Module Contains the cache class
    author: Peter Ekwere
"""
import redis
import uuid
from functools import wraps
from typing import Union, Callable, Optional, Any


def count_calls(method: Callable) -> Callable:
    """
    This function counts how many times the Cache method is called
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args: Any, **kwds: Any) -> Any:
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


class Cache:
    """
    This is the cache Class
    """

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        THis method  store the input data in Redis using a random key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
        """
        This Method gets the corresponding value from the redis database
        """
        if fn:
            value = fn(self._redis.get(key))
            return value
        return self._redis.get(key)

    def get_str(self, value: bytes) -> str:
        """
        This method converts bytes to a string
        """
        string_value = value.decode('utf-8')
        return string_value

    def get_int(self, value: bytes) -> int:
        """
        This method converts a byte values to integers
        """
        int_value = int(value)
        return int_value
