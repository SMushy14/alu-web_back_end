#!/usr/bin/env python3
"""MongoDB Operations with Python using pymongo"""
from pymongo import MongoClient

if __name__ == "__main__":
    """Provides some stats about Nginx logs stored in MongoDB"""
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx = client.logs.nginx

    x_logs = nginx.count_documents({})
    print(f"{x_logs} logs")

    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in method:
        count = nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = nginx.count_documents(
        {'method=GET', 'path=/status'}
    )

    print(f"{status_check} status check")
