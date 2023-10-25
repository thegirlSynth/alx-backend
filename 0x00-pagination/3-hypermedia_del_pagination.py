#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

from collections import deque
import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a hyper index
        """
        my_dict = {}

        if index is None:
            index = 0

        assert type(index) is int and index < len(self.indexed_dataset())

        next_index = index + page_size

        page_dataset = []
        queue = deque(range(index, next_index))
        count = 0

        while queue:
            indx = queue.popleft()
            if self.indexed_dataset().get(indx):
                page_dataset.append(self.indexed_dataset()[indx])
            else:
                queue.append(next_index)
                count += 1

        my_dict["index"] = index
        my_dict["next_index"] = next_index + count
        my_dict["page_size"] = len(page_dataset)
        my_dict["data"] = page_dataset

        return my_dict
