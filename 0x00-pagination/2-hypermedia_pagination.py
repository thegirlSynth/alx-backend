#!/usr/bin/env python3
"""
Implement hypermedia pagination
"""

import csv
from typing import Dict, List
import math


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns a dictionary containing the following key-value pairs:
            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page (equivalent to return from previous task)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an integer
        """
        my_dict = {}

        page_dataset = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        my_dict["page_size"] = len(page_dataset)
        my_dict["page"] = page
        my_dict["data"] = page_dataset

        if (page + 1) >= total_pages:
            my_dict["next_page"] = None
        else:
            my_dict["next_page"] = page + 1

        if (page - 1) <= 0:
            my_dict["prev_page"] = None
        else:
            my_dict["prev_page"] = page - 1

        my_dict["total_pages"] = total_pages

        return my_dict
