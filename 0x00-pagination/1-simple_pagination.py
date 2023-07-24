#!/usr/bin/env python3
""" A Simple helper function """
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ A function that return start idex and
        end index of a particular pageination
    """
    if page <= 1:
        offset = 0
    else:
        offset = (page - 1) * page_size

    limit = page * page_size
    return offset, limit


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ A method to get specific page of dataset """
        assert isinstance(page, int) and page > 0, "should_err"
        assert isinstance(page_size, int) and page_size > 0, "should_err"

        offset, limit = index_range(page, page_size)
        dataset = self.dataset()

        # Check if the offset is out of dataset range
        if offset >= len(dataset):
            return []

        # Slice the dataset to get the specified page
        return dataset[offset:limit]
