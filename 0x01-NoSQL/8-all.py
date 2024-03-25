#!/usr/bin/env python3
""" List all documents in a collection """


def list_all(mongo_collection):
    """function that lists all documents in a collection"""

    # Find all documents in the collection
    cursor = mongo_collection.find({})

    # Initialize an empty list to store the documents
    all_documents = []

    # Iterate through the cursor and append each document to the list
    for document in cursor:
        all_documents.append(document)

    return all_documents
