#!/usr/bin/env python3
"""
Web cache and tracker
"""
import requests
import redis
from functools import wraps

store = redis.Redis()


def count_url_access(method):
    """Decorator counting URL accesses and caching results"""

    @wraps(method)
    def wrapper(url):
        count_key = f"count:{url}"
        cached_key = f"cached:{url}"

        store.incr(count_key)

        cached_data = store.get(cached_key)
        if cached_data:
            return cached_data.decode("utf-8")

        html = method(url)

        store.set(cached_key, html, ex=10)
        return html

    return wrapper


@count_url_access
def get_page(url: str) -> str:
    """Fetch HTML content of a URL"""
    response = requests.get(url)
    return response.text
