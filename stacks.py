class Stack:
	def __init__(self,capacity):
		self.capacity = capacity
		self.list = [None] * capacity
	def push(self,item):
		if self.list[-1] != None:
			print("The stack is full")
		self.list[-1] = item
	def pop(self):
		if self.list[-1] !=None:
			return self.list[-1]
		print("The stack is empty")
	def peek(self):
		print(self.list[-1])
	def size(self):
		return self.capacity - self.list.count(None)
	def is_empty(self):
		if self.list.count(None) == self.capacity:
			return True
		return False
	def is_full(self):
		if self.list.count(None) == 0:
			return True
		return False
