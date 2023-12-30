#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Union, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self,
                        index: Union[int, None] = None,
                        page_size: int = 10) -> Dict:
        """
        Implements deletion-resilient pagination
        """
        data = self.indexed_dataset()
        working_index = -1 if index is None else index

        # verify that index is in a valid range.
        assert working_index > 0
        assert working_index < len(data)

        actual_data = []
        current_index = working_index
        while len(actual_data) < page_size:
            user = data.get(current_index)
            if user is not None:
                actual_data.append(user)
            current_index += 1

        result = {
            'index': working_index,
            'next_index': current_index,
            'page_size': page_size,
            'data': actual_data
        }
        return result
