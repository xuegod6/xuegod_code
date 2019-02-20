import queue
Q = queue.Queue(10)
for i in range(5):
    Q.put(i)
while not Q.empty():
    print(Q.get())