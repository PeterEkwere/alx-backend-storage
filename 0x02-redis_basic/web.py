#!/usr/bin/env python3
<<<<<<< HEAD
"""module for the function get_page"""

import requests
import redis

client = redis.Redis()


def get_page(url: str) -> str:
    """obtain the HTML content of a particular URL and returns it."""
    result = requests.get(url).text
    if not client.get("count:{}".format(url)):
        client.set("count:{}".format(url), 1)
        client.setex("result:{}".format(url), 10, result)
    else:
        client.incr("count:{}".format(url), 1)
    return result
=======
"""
    This Module uses the requests module to obtain the HTML content of a URL.
    Author: Peter Ekwere
"""
import requests
import redis
import functools

cli = redis.Redis()

# @track_access_count
# @cache_result


def get_page(url: str) -> str:
    """
    This function get_page track how many times a particular
    URL was accessed in the key "count:{url}" and
    cache the result with an expiration time of 10 seconds.
    """
    resp = requests.get(url).text
    if not cli.get("count:{}".format(url)):
        cli.set("count:{}".format(url), 1)
        cli.setex("result:{}".format(url), 10, resp)
    else:
        cli.incr("count:{}".format(url), 1)
    return resp
>>>>>>> f686e6ad6b9798cc2a84760f9ace5ee88ffc0c6b
