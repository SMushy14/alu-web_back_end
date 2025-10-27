#!/usr/bin/env python3
"""A module with tools for request caching and tracking."""
import redis
import requests
from functools import wraps
from typing import Callable


redis_store = redis.Redis()
"""The module-level Redis instance.
"""


def data_cache(method: Callable) -> Callable:
    """Caches the output of fetched data."""

    @wraps(method)
    def invoker(url: str) -> str:
        """The wrapper function for caching the output."""
        redis_store.incr(f"count:{url}")
        cached = redis_store.get(f"result:{url}")
        if cached:
            return cached.decode("utf-8")
        result = method(url)
        redis_store.setex(f"result:{url}", 10, result)
        return result

    return invoker


@data_cache
def get_page(url: str) -> str:
    """Returns the content of a URL after caching the request's response,
    and tracking the request.
    """
    return requests.get(url).text
