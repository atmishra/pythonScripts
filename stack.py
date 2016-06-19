class Stack(object):
	def __init__(self):
		
		self.stack_list = [] 
		self.top = -1
		self.stack_size = len(self.stack_list)

	def push(self, value):
		self.top += 1
		self.stack_list.append(value)

	def pop(self):
		if self.top>-1:
			
			self.top -= 1
			return self.stack_list.pop()

	def peek(self):
		if self.top>-1:
			return self.stack_list[self.top]

	def size(self):
		return self.top+1

	def isEmpty(self):
		if self.top > -1:

			return False
		else:
			return True

if __name__ == "__main__":
	stack = Stack()
	stack.push(10)
	stack.push(12)
	stack.push(43)
	stack.push(1)
	stack.push(87)
	stack.push(3)
	print (stack.peek())

	print (stack.pop())
	print (stack.pop())
	print (stack.pop())
	print (stack.pop())
	print (stack.pop())
	print (stack.pop())
	print(stack.top)
	print (stack.isEmpty())








