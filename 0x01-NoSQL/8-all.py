#!/usr/bin/env python3
"""
    This  function that lists all documents in a collection
    Author: Peter Ekwere
"""
from pymongo.collection import Collection
from typing import List


def list_all(mongo_collection: Collection) -> List:
    """ This function prints the mongo collection """
    docs = mongo_collection.find()
    a_list = []

    for document in docs:
        a_list.append(document)
    return a_list
