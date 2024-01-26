#!/usr/bin/env python3
"""
    This  function that lists all documents in a collection
    Author: Peter Ekwere
"""


if __name__ == "__main__":
    pass


def update_topics(mongo_collection, name, topics):
    """ This function prints the mongo collection """
    id = mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
