from collections import deque

class Queue :
	def  __init__(self) :
		self.queue = deque()

	def enqueue(self, data) :
		self.queue.append(data)
		print("Enqueued", data, "to the Queue Successfully.")
	
	def dequeue(self) :
		temp = self.queue.popleft()
		print("Underflow") if not temp else print("Dequeued", temp, "from the Queue Successfully.")
	
	def display(self) :
		print("Queue : ", end= " ")
		if not self.queue :
			print("Underflow", end=" ")
		for i in self.queue :
			print(i, end= " ")
		print()

	def size(self) :
		print("Number of elements in the Queue :", len(self.queue))

Q = Queue()
Q.display()
Q.enqueue(1)
Q.display()
Q.enqueue(2)
Q.display()
Q.enqueue(3)
Q.display()
Q.enqueue(4)
Q.display()
Q.enqueue(5)
Q.display()	
Q.size()
Q.dequeue()
Q.display()
Q.dequeue()
Q.display()
Q.size()
