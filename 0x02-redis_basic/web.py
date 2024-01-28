#!/usr/bin/env python3
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
