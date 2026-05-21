#!/usr/bin/python3

def canUnlockAll(boxes):
    """Determine if all locked boxes can be opened"""
    nboxes = len(boxes)
    found_index = set([0])
    keys = [0]

    while keys:
        curr_box = keys.pop()

        for next_key in boxes[curr_box]:
            if next_key < nboxes and next_key not in found_index:
                found_index.add(next_key)
                keys.append(next_key)
    return len(found_index) == nboxes
