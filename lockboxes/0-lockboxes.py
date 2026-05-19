#!/usr/bin/python3
"""Module for lockboxes problem."""


def canUnlockAll(boxes):
    """Determine if all boxes can be opened.

    Args:
        boxes: list of lists containing keys

    Returns:
        True if all boxes can be opened, False otherwise
    """
    n = len(boxes)
    unlocked = set([0])
    keys = set(boxes[0])

    while keys:
        key = keys.pop()
        if key < n and key not in unlocked:
            unlocked.add(key)
            for new_key in boxes[key]:
                if new_key not in unlocked:
                    keys.add(new_key)

    return len(unlocked) == n
