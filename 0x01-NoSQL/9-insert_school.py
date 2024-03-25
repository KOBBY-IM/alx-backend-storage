#!/usr/bin/env python3
""" Insert a new document in a collection """


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into the collection based on provided keyword arguments.

    :param kwargs: The keyword arguments representing the fields and values of the document to be inserted.

    :return: The ID of the newly inserted document.
"""

    # Insert a new document into the collection based on provided keyword arguments
    new_school_id = mongo_collection.insert_one(kwargs).inserted_id
    
    return new_school_id