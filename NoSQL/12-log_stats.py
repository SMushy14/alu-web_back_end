#!/usr/bin/env python3
"""Task 12's module."""
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    """Prints stats about Nginx request logs."""
    print("{} logs".format(nginx_collection.count_documents({})))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        req_count = len(list(nginx_collection.find({"method": method})))
        print("\tmethod {}: {}".format(method, req_count))
    status_checks_count = len(
        list(nginx_collection.find({"method": "GET", "path": "/status"}))
    )
    print("{} status check".format(status_checks_count))


try:
    client = MongoClient()
    nginx_collection = client.logs.nginx
    print_nginx_request_logs(nginx_collection)
except Exception as e:
    print("0 logs")
    print("Methods:")
    print("\tmethod GET: 0")
    print("\tmethod POST: 0")
    print("\tmethod PUT: 0")
    print("\tmethod PATCH: 0")
    print("\tmethod DELETE: 0")
    print("0 status check")
