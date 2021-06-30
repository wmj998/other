from queue import Queue
q = Queue()
q.put('a')
print(q.get())

# 避免阻塞
q.get(block=False)
q.get(block=True, timeout=2)
while not q.empty():
    q.get()
