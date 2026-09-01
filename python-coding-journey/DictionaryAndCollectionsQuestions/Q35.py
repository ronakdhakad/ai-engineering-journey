# 35. Implement deque for queue
from collections import deque

queue=deque()

queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
queue.append(50)

print("queue",queue)

item=queue.popleft()
item2=queue[3]

print("Removed Element:",item)
print("Removed Element:",item2)
print("Queue after dequeue:",queue)