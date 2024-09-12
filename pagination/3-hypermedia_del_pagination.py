#!/usr/bin/env python3


"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


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
            dict2 = {i: dataset[i] for i in range(len(dataset))}
            self.__indexed_dataset = dict2
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a dictionary containing the following key-value pairs:

        - index (int): The current start index of the return page.
        - next_index (int): The next index to query with.
        - page_size (int): The current page size.
        - data (List[List]): The actual page of the dataset
        - page (int): The current page number.
        """
        assert isinstance(index, int) and index < len(self.dataset())
        assert isinstance(page_size, int) and page_size > 0
        return {
            "index": index,
            "next_index": index + page_size,
            "page_size": page_size,
            "data": self.dataset()[index: index + page_size],
            "page": index // page_size + 1,
        }
