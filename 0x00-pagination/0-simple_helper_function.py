#!/usr/bin/env python3
"""
Simple helper function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list
    for those particular pagination parameters.
    """
    if page == 1:
        index1 = 0
        indexz = page_size

    if page > 1:
        index1 = page_size * (page - 1)
        indexz = index1 + page_size

    return (index1, indexz)
