#!/usr/bin/python3
"""
Lockboxes problem module
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes (list of list of int): List where each index represents a box
        and contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return True

    n = len(boxes)
    opened = set([0])   # we start with box 0 unlockeds
    keys = set(boxes[0])

    while keys:
        key = keys.pop()

        if 0 <= key < n and key not in opened:
            opened.add(key)
            keys.update(boxes[key])

    return len(opened) == n
