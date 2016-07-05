class Node():
	def __init__(self,data):
		self.data=data
		self.next=None


class CircularLinkedList(Node):
	head = None
	count = 0
	def __init__(self):
		self.head = None
		self.count = 0

	def createNode(self,data):
		node = Node(data)
		node.next = node
		self.count+=1
		return node


	def insertEnd(self,data):
		
		node = self.createNode(data)

		if self.head == None:
			self.head = node
		else:
			tail = self.traverse()
			tail.next = node
			node.next = self.head

	def insertFront(self,data):
		
		node = self.createNode(data)

		if self.head == None:
			self.head = node
		else:
			node.next = self.head
			tail = self.traverse()
			self.head = node
			tail.next = self.head

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
				
			node.next = temp.next
			temp.next = node

	def deleteLast(self):
		if self.head:
			temp = self.head 
			while temp.next.next != self.head:
				temp = temp.next
			temp.next = self.head
			self.count -= 1
		else:
			print("UnderFlow")

	def deleteFirst(self):
		if self.head:
			tail = self.traverse()
			self.head = self.head.next
			tail.next = self.head
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
			temp1 = self.head.next
			temp2 = self.head
			for i in range(pos-2):
				temp2 =temp1
				temp1 = temp1.next
			
			temp2.next = temp1.next
			self.count -=1

	def traverse(self):
		temp = self.head
		while (temp.next != self.head):
			temp = temp.next
		return temp

	def printList(self):
		temp = self.head

		for i in range(self.count):
			
			print(temp.data)
			temp=temp.next

if __name__ == "__main__":
	ll = CircularLinkedList()
	ll.insertEnd(10)
	ll.insertEnd(20)
	ll.insertFront(1)
	ll.insertFront(2)
	ll.insertFront(3)
	ll.insertMiddle(100,3)
	print("="*80)
	ll.printList()
	ll.deleteFirst()
	ll.deleteLast()
	ll.deleteMiddle(3)
	print("Count: ",ll.count)
	ll.printList()





