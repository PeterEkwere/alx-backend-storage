#!/usr/bin/env python3
"""
    This Module uses the requests module to obtain the HTML content of a particular URL and returns it.
    Author: Peter Ekwere
"""
import requests
import redis


cli = redis.Redis()

def get_page(url: str) -> str:
    """
    """
    key = f"count:{url}"
    cli.incr(key)

    cache_content_key = f"cache:{url}"
    cached_content = cli.get(cache_content_key)

    if cached_content:
        return cached_content.decode('utf-8')

    resp = requests.get(url)
    html_content = resp.text
    
    cli.setex(cached_content_key, 10, html_content)
    
    return html_content
