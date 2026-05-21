#!/usr/bin/python3
"""Module to determine if all locked boxes can be unlocked."""


def canUnlockAll(boxes):
    """Determine if all locked boxes can be opened.

    Each box is numbered sequentially from 0 to n-1. Each box may contain
    keys to other boxes. Box 0 is unlocked by default.

    Args:
        boxes (list of list): A list of boxes where each element is a list
            of keys contained in that box. A key with the same number as
            a box opens that box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    nboxes = len(boxes)
    found_index = set([0])
    keys = [0]

    while keys:
        curr_box = keys.pop()

        for next_key in boxes[curr_box]:
            if next_key < nboxes and next_key not in found_index:
                found_index.add(next_key)
                keys.append(next_key)
    result = len(found_index) == nboxes
    return result
