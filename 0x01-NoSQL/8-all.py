#!/usr/bin/env python3
"""Module for list_all
"""


def list_all(mongo_collection):
    """Return all doc inside give collection"""
    return [l for l in mongo_collection.find()]

