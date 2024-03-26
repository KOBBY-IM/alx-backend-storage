#!/usr/bin/env python3
""" log stats module """

import pymongo

# Create a connection to the MongoDB server
connection = pymongo.MongoClient("mongodb://localhost:27017/")

# Select the database
db = connection.logs

# Select the collection
collection = db.nginx


# Get the number of documents in the collection
number_of_logs = collection.count_documents({})
print(f"{number_of_logs} logs")

# Create the queries
queries = [{'method': 'GET'}, {'method': 'POST'}, {'method': 'PUT'},
           {'method': 'PATCH'}, {'method': 'DELETE'}, {'path': '/status'}]

# Initialize an empty list to store the results
results = []

# Iterate through the queries
for query in queries:
    # Get the number of documents that match the query
    number_of_documents = collection.count_documents(query)
    # Add the result to the list
    results.append(number_of_documents)

# Print the results
print("Methods:")
for i, result in enumerate(results):
    print(f"\tmethod {['GET', 'POST', 'PUT', 'PATCH', 'DELETE',
                       'status check'][i]}: {result}")
