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


def call_history(method: Callable) -> Callable:
    """
    This function  stores the history of inputs and outputs for a particular function.
    """
    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args: Any, **kwds: Any) -> Any:
        self._redis.rpush(input_key, str(args))
        output = method(self, *args)
        self._redis.rpush(output_key, output)
        return output
    return wrapper


def replay(method: Callable) -> str:
    """
    This function display the history of calls of a particular function
    """
    cli = redis.Redis()
    count = int(cli.get(method.__qualname__))

    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"

    input_data = cli.lrange(input_key, 0, -1)
    output_data = cli.lrange(output_key, 0, -1)

    print(f"{method.__qualname__} was called {count} times:")

    for args, output in zip(input_data, output_data):
        print(
            f"{method.__qualname__}(*{args.decode('utf-8')}) -> {output.decode('utf-8')}")


class Cache:
    """
    This is the cache Class
    """

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
