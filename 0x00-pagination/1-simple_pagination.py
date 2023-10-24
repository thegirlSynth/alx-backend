#!/usr/bin/env python3
"""
Implementing a simple pagination
"""


import csv
from itertools import islice
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of size two containing a start index and an end index
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


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Creates an instance of the Server class
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns the appropriate page of the dataset
        (i.e. the correct list of rows).
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        index_tuple = index_range(page, page_size)

        return self.dataset()[index_tuple[0]:index_tuple[1]]
