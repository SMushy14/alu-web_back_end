#!/usr/bin/env python3
"""12. Log stats"""

from pymongo import MongoClient


def log_stats():
    """Provides some stats about Nginx logs."""
    client = MongoClient()
    collection = client.logs.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")
    print("Methods:")
    print(f"\tmethod GET: {collection.count_documents({'method': 'GET'})}")
    print(f"\tmethod POST: {collection.count_documents({'method': 'POST'})}")
    print(f"\tmethod PUT: {collection.count_documents({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {collection.count_documents({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {collection.count_documents({'method': 'DELETE'})}")

    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")


log_stats()
