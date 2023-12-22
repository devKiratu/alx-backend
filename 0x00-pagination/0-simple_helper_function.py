#!/usr/bin/env python3
"""
Defines a helper function to simulate pagination, that takes two params
as follows:
page - the page to start at
page_size - number of items per page
Note: page numbers are 1 - indexed
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    returns a tuple of start index and end index of the items to fetch
    """
    # start_index - last index of previous page fetch
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
