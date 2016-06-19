'''This is the implementation for Binary Heap'''

class Heap(object):
	def __init__(self, alist):

		'''initialize heap to the input list'''
		self.hlist = ["dummy"]+alist #To start indexing from 1
		self.hsize = len(self.hlist)-1 

	def __str__(self):
		return "%s" %self.hlist[1:] #The actual heap starts from index 1

	def max_heapify(self, node,size):
		'''max_heapify performs perculate down operation on the heap. Node is the index 
		   where the method is to applied annd size is the size of the list'''
		left_child = 2*node
		right_child = left_child + 1
		largest = node
		
		if left_child <= size and self.hlist[left_child] > self.hlist[node]:

			largest = left_child

		if right_child <= size and self.hlist[right_child] > self.hlist[largest]:

			largest = right_child

		if largest != node :

			self.hlist[largest],self.hlist[node] = self.hlist[node],self.hlist[largest]

			self.max_heapify(largest,size)

		

	def build_max_heap(self):
		'''Builds max heap for the list provided'''
		for i in range(self.hsize//2,0,-1):
			self.max_heapify(i,self.hsize)
		

	def deleteMax(self):
		'''Delete max element from the Heap maintaining the Heap property'''
		if self.hsize < 1:
			print "UnderFlow"
		max = self.hlist[1]
		self.hlist[1] = self.hlist[self.hsize]
		self.hsize -= 1
		self.hlist = self.hlist[:-1]
		self.max_heapify(1,self.hsize)
		return max

	def perUp(self,i):
		'''perform perculate Up operation on the Heap'''
		while i//2>0:

			if self.hlist[i]>self.hlist[i//2]:
				self.hlist[i//2],self.hlist[i] = self.hlist[i],self.hlist[i//2]
			i = i//2

	def insert(self,value):
		'''Inserts new value into the Heap maintaining the Heap property'''

		self.hlist.append(value)
		self.hsize += 1
		self.perUp(self.hsize)

	def getMax(self):
		return self.hlist[1]

	def heapsort(self):
		'''Sorts the list provided to the Heap object using Heap Sort'''

		self.max_heapify(1,self.hsize)
		
		for i in range(self.hsize,1,-1):
			self.hlist[i],self.hlist[1] = self.hlist[1],self.hlist[i]
			
			self.max_heapify(1,i-1)
			



		
if __name__ == "__main__":

	alist = [30,100,3,1,20,10,15]
	newHeap = Heap(alist)
	print(newHeap)
	newHeap.insert(70)
	print(newHeap.getMax())
	newHeap.heapsort()
	print(newHeap)


