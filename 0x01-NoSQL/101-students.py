#!/usr/bin/env python3
""" calculate average score module """


def top_students(mongo_collection):
    """ returns all students sorted by average score """
    pipeline = [
        {
            "$project": {
                "name": 1,
                "topics": 1,
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]
    top_students = list(mongo_collection.aggregate(pipeline))
    return top_students
