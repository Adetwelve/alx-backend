#!/usr/bin/env python3
""" A Simple helper function """
from typing import Tuple


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
