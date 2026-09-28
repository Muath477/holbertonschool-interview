#!/usr/bin/python3
"""Determine whether all lockboxes can be opened."""


def canUnlockAll(boxes):
    """Determine if all boxes can be opened.

    Args:
        boxes (list): A list of lists, where boxes[i] contains the
            keys found inside box i. Box 0 starts unlocked.

    Returns:
        bool: True if every box can be opened, False otherwise.
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    stack = [0]

    while stack:
        current = stack.pop()
        for key in boxes[current]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)
