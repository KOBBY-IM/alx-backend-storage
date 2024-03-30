#!/usr/bin/env python3
""" log stats module """


from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    logs = client.logs.nginx

    n_docs = logs.count_documents({})
    print(f"{n_docs} logs")

    print("Methods:")

    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        n_count = logs.count_documents({"method": method})
        print(f"\tmethod {method}: {n_count}")

    n_count = logs.count_documents({"method": "GET", "path": "/status"})
    print(f"{n_count} status check")