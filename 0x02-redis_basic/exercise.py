#!/usr/bin/env python3
<<<<<<< HEAD
""" module for the class Cache """
import redis
from uuid import uuid4
from typing import Union, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count the number of calls to a class method."""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
        """Wrapper function that increments a key in Redis for Cache.store"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

=======
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
>>>>>>> f686e6ad6b9798cc2a84760f9ace5ee88ffc0c6b
    return wrapper


def call_history(method: Callable) -> Callable:
<<<<<<< HEAD
    """Decorator to track method calls and their inputs/outputs in Redis"""
=======
    """
    This function  stores the history of inputs and outputs for a particular function.
    """
>>>>>>> f686e6ad6b9798cc2a84760f9ace5ee88ffc0c6b
    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"

    @wraps(method)
<<<<<<< HEAD
    def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
        """Wrapper that records input and output data in Redis lists."""
        input_data = str(args)
        self._redis.rpush(input_key, input_data)
        output_data = method(self, *args)
        self._redis.rpush(output_key, output_data)
        return output_data

=======
    def wrapper(self, *args: Any, **kwds: Any) -> Any:
        self._redis.rpush(input_key, str(args))
        output = method(self, *args)
        self._redis.rpush(output_key, output)
        return output
>>>>>>> f686e6ad6b9798cc2a84760f9ace5ee88ffc0c6b
    return wrapper


def replay(method: Callable) -> None:
<<<<<<< HEAD
    """function to display the history of calls of a particular function."""
    client = redis.Redis()

    in_key = method.__qualname__ + ":inputs"
    out_key = method.__qualname__ + ":outputs"

    in_data = client.lrange(in_key, 0, -1)
    out_data = client.lrange(out_key, 0, -1)
    zippy = list(zip(in_data, out_data))

    print("{} was called {} times:".format(method.__qualname__, len(zippy)))

    for value, r_id in zippy:
        print("{}(*{}) -> {}".format(
            method.__qualname__,
            value.decode("utf-8"),
            r_id.decode("utf-8")))


class Cache:
    """class Cache"""

    def __init__(self):
        """Initialize a Cache instance using Redis"""
=======
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
>>>>>>> f686e6ad6b9798cc2a84760f9ace5ee88ffc0c6b
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
<<<<<<< HEAD
        """Store data in the cache."""
        key = str(uuid4())
=======
        """
        THis method  store the input data in Redis using a random key
        """
        key = str(uuid.uuid4())
>>>>>>> f686e6ad6b9798cc2a84760f9ace5ee88ffc0c6b
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
<<<<<<< HEAD
        """Retrieve data from the cache using the specified key."""
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """Retrieve a string from the cache using the specified key."""
        return str(self._redis.get(key))

    def get_int(self, key: str) -> int:
        """Retrieve an integer from the cache using the specified key."""
        return int(self._redis.get(key))
=======
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
>>>>>>> f686e6ad6b9798cc2a84760f9ace5ee88ffc0c6b
