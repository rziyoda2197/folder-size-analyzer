def meeting_time_slot_finder(meetings):
    """
    Meetings: [[start_time, end_time], [start_time, end_time], ...]
    """
    meetings.sort(key=lambda x: x[0])
    time_slots = []
    for start, end in meetings:
        for i, (slot_start, slot_end) in enumerate(time_slots):
            if start >= slot_end:
                time_slots.insert(i, [start, end])
                break
        else:
            time_slots.append([start, end])
    return time_slots

meetings = [[9, 10], [10, 11], [11, 12], [13, 14], [14, 15], [15, 16]]
print(meeting_time_slot_finder(meetings))
```

```python
def meeting_time_slot_finder(meetings):
    meetings.sort(key=lambda x: x[0])
    time_slots = []
    for start, end in meetings:
        for i, (slot_start, slot_end) in enumerate(time_slots):
            if start >= slot_end:
                time_slots.insert(i, [start, end])
                break
        else:
            time_slots.append([start, end])
    return time_slots

meetings = [[9, 10], [10, 11], [11, 12], [13, 14], [14, 15], [15, 16]]
print(meeting_time_slot_finder(meetings))
```

```python
def meeting_time_slot_finder(meetings):
    meetings.sort(key=lambda x: x[0])
    time_slots = []
    for start, end in meetings:
        for i, (slot_start, slot_end) in enumerate(time_slots):
            if start >= slot_end:
                time_slots.insert(i, [start, end])
                break
        else:
            time_slots.append([start, end])
    return time_slots

meetings = [[9, 10], [10, 11], [11, 12], [13, 14], [14, 15], [15, 16]]
print(meeting_time_slot_finder(meetings))
