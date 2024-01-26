#!/usr/bin/env python3
"""
    This  function that lists all documents in a collection
    Author: Peter Ekwere
"""


if __name__ == "__main__":
    pass


def list_all(mongo_collection):
    """ This function prints the mongo collection """
    docs = mongo_collection.find()
    return docs
