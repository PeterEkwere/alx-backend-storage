#!/usr/bin/env python3
"""
    This Module uses the requests module to obtain the HTML content of a URL.
    Author: Peter Ekwere
"""
import requests
import redis
import functools

cli = redis.Redis()


def track_access_count(url: str) -> None:
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            cli.incr(f"count:{url}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


def cache_result(url: str, expiration_time: int = 10) -> None:
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            cached_result = cli.get(f"cache:{url}")
            if cached_result:
                return cached_result.decode('utf-8')

            result = func(*args, **kwargs)
            cli.setex(f"cache:{url}", expiration_time, result)
            return result
        return wrapper
    return decorator


@track_access_count
@cache_result
def get_page(url: str) -> str:
    """
    This function get_page track how many times a particular
    URL was accessed in the key "count:{url}" and
    cache the result with an expiration time of 10 seconds.
    """
    resp = requests.get(url)
    return resp.text
