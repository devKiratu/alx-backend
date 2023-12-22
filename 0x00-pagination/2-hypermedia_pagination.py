#!/usr/bin/env python3
"""
Defines Server Class that simulates pagination by fetching data from a csv
file and uses various methods to manipulate the size of data to view
"""
import csv
import math
from typing import List, Tuple, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """
        returns a tuple of start index and end index of the items to fetch
        """
        # start_index - last index of previous page fetch
        start_index = (page - 1) * page_size
        end_index = page * page_size
        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        returns a subset of data for the required page based on the page_size
        """
        # validate page and page_size
        assert isinstance(page, int)
        assert page > 0
        assert isinstance(page_size, int)
        assert page_size > 0

        start, end = self.index_range(page, page_size)

        data = self.dataset()

        if start > len(data) or end > len(data):
            return []

        return data[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        returns a dictionary of pagination data
        """
        total_pages = math.ceil(len(self.dataset()) / page_size)
        data = self.get_page(page, page_size)
        returned_page_size = len(data)
        next_page = None if page + 1 > total_pages else page + 1
        prev_page = None if page - 1 < 1 else page - 1

        result = {
            'page_size': returned_page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

        return result
