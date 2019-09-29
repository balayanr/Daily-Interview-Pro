"""
This problem was recently asked by Google:

You are given an array of tuples (start, end) representing time intervals for lectures.
The intervals may be overlapping. Return the number of rooms that are required.

For example. [(30, 75), (0, 50), (60, 150)] should return 2.
"""
import numpy as np

def rooms_required_numpy(intervals):
    time_tracker = np.asarray([], dtype=np.int)
    for start, end in intervals:
        if end > len(time_tracker):
            time_tracker = np.hstack((time_tracker, np.zeros((end - len(time_tracker)), dtype=np.int) ))
        time_tracker[start:end] += 1

    return np.max(time_tracker)

def rooms_required(intervals):
    time_tracker = []
    for start, end in intervals:
        if end > len(time_tracker):
            time_tracker += [0] * (end - len(time_tracker))
        for i in range(start, end):
            time_tracker[i] += 1
    return max(time_tracker)

print(rooms_required_numpy([(30, 75), (0, 50), (60, 150)]))
print(rooms_required([(30, 75), (0, 50), (60, 150)]))
# 2
