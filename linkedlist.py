class Node():
	def __init__(self,data):
		self.data=data
		self.next=None
		self.index=0

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def getIndex():
		return self.index

class LinkedList(Node):
	head = None
	count = 0
	def __init__(self):
		self.head = None
		self.count = 0

	def createNode(self,data):
		node = Node(data)
		self.count+=1
		node.index = self.count
		return node


	def insertEnd(self,data):
		
		node = self.createNode(data)

		if self.head == None:
			self.head = node
		else:
			temp = self.iterate()
			temp.next = node

	def insertFront(self,data):
		
		node = self.createNode(data)

		if self.head == None:
			self.head = node
		else:
			node.next = self.head
			self.head = node

	def insertMiddle(self,data,pos):
		if pos>self.count:
			print("Invalid Position")
		elif pos==1:
			self.insertFront(data)
		elif pos==self.count:
			self.insertEnd(data)
		else:
			node = self.createNode(data)
			temp = self.head
			
			print("pos=",pos)
			for i in range(pos-2):
				temp = temp.next
				print("temp=",temp.data)
			node.next = temp.next
			temp.next = node

	def iterate(self):
		temp = self.head
		while temp.next:
			temp = temp.next
		return temp

	def printList(self):
		temp = self.head

		for i in range(self.count):
			
			print(temp.data)
			temp=temp.next

if __name__ == "__main__":
	ll = LinkedList()
	ll.insertEnd(10)
	ll.insertEnd(20)
	ll.insertEnd(40)
	ll.insertEnd(50)
	ll.insertEnd(10)
	ll.insertEnd(30)
	ll.printList()
	print("="*100)
	ll.insertFront(1)
	ll.insertFront(2)
	ll.insertFront(3)
	ll.printList()
	print("="*100)
	ll.insertMiddle(100,3)
	ll.printList()

	print("Count: ",ll.count)





