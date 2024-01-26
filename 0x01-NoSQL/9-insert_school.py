#!/usr/bin/env python3
"""
    This  function that lists all documents in a collection
    Author: Peter Ekwere
"""


if __name__ == "__main__":
    pass


def insert_school(mongo_collection, **kwargs):
    """ This function prints the mongo collection """
    id = mongo_collection.insert_one(kwargs)
    return id
