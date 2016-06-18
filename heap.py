class Heap(object):
	def __init__(self):
		self.hlist = ["dummy"]
		self.hsize = 0

	def __str__(self):
		return "%s" %self.hlist[1:]

	def inputList(self, alist):

		self.hlist = [0] + alist

		self.hsize = len(self.hlist) - 1

	def max_heapify(self, node,size):
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

		# return self.hlist[1:]

	def build_max_heap(self):
		for i in range(self.hsize//2,0,-1):
			self.max_heapify(i,self.hsize)
		

	def deleteMax(self):
		if self.hsize < 1:
			print "UnderFlow"
		max = self.hlist[1]
		self.hlist[1] = self.hlist[self.hsize]
		self.hsize -= 1
		self.hlist = self.hlist[:-1]
		self.max_heapify(1,self.hsize)
		return max

	def perUp(self,i):
		while i//2>0:

			if self.hlist[i]>self.hlist[i//2]:
				self.hlist[i//2],self.hlist[i] = self.hlist[i],self.hlist[i//2]
			i = i//2

	def insert(self,value):
		self.hlist.append(value)
		self.hsize += 1
		self.perUp(self.hsize)

	def getMax(self):
		return self.hlist[1]

	def heapsort(self):

		self.max_heapify(1,self.hsize)
		
		for i in range(self.hsize,1,-1):
			self.hlist[i],self.hlist[1] = self.hlist[1],self.hlist[i]
			
			self.max_heapify(1,i-1)
			



		
if __name__ == "__main__":

	alist = [30,100,3,1,20,10,15]
	newHeap = Heap()
	newHeap.inputList(alist)
	# newHeap.max_heapify(1,)
	print(newHeap)
	newHeap.insert(70)
	# print(newHeap)
	# newHeap.deleteMax()
	# print (newHeap)
	newHeap.heapsort()
	print(newHeap)


