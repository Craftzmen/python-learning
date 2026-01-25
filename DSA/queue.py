
from collections import deque

queue = deque()

queue.append('a')
queue.append('b')
queue.append('c')

print("Initial queue:", queue)

print(f'Total Queue Nodes: {queue.__len__()}')

print("Elements dequeued from the list ")

queue.popleft()
queue.popleft()
queue.popleft()

print("Queue after removing elements:", queue)

print(f'Total Queue Nodes: {queue.__len__()}')