class Node():
	def __init__(self,data):
		self.data=data
		self.next=None
		self.prev = None
class DoublyLinkedList():
	head = None
	count = 0
	def __init__(self):
		self.head = None
		self.count = 0

	def createNode(self,data):
		node = Node(data)
		self.count+=1
		return node

	def insertFront(self,data):
		node = self.createNode(data)
		if self.head == None:
			self.head = node
		else:
			node.next = self.head
			self.head.prev = node
			self.head = node


	def insertMiddle(self,data,pos):
		if pos>self.count or pos<1:
			print("Invalid Position")
		elif pos==1:
			self.insertFront(data)
		elif pos==self.count:
			self.insertEnd(data)
		else:
			node = self.createNode(data)
			temp = self.head
			
			for i in range(pos-2):
				temp = temp.next
			
			temp.next.prev = node	
			node.next = temp.next
			node.prev = temp
			temp.next = node


	def insertEnd(self,data):
		node = self.createNode(data)

		if self.head == None:
			self.head = node
		else:
			temp = self.iterate()
			temp.next = node
			node.prev = temp

	
	def deleteFirst(self):
		if self.head:
			self.head = self.head.next
			self.head.next.prev = None
			self.count -=1
		else:
			print("UnderFlow")

	def deleteMiddle(self,pos):
		if pos>self.count or pos<1:
			print ("Invalid Position")
		elif self.count<1:
			print("UnderFlow")
			
		elif pos==1:
			self.deleteFirst()
		elif pos==self.count:
			self.deleteLast()
		else:
			
			temp = self.head
			for i in range(pos-1):
				temp = temp.next
			
			temp.next.prev = temp.prev
			temp.prev.next = temp.next
			temp.prev, temp.next = None, None
			self.count -=1

	def deleteLast(self):
		if self.head:
			temp = self.head 
			while temp.next.next:
				temp = temp.next
			temp.next.prev = None
			temp.next = None
			
			self.count -= 1
		else:
			print("UnderFlow")




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
	ll = DoublyLinkedList()
	ll.insertFront(10)
	ll.insertEnd(20)
	ll.insertFront(30)
	ll.insertFront(40)
	ll.insertEnd(50)
	ll.insertMiddle(100,3)

	ll.printList()
	print("*"*80)
	# ll.deleteFirst()
	# ll.deleteLast()
	ll.printList()
	ll.deleteMiddle(4)
	print("*"*80)
	ll.printList()
