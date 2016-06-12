
def countingSort(alist):

	max_element = max(alist)
	count = []

	for i in range(max_element+1):
		count.append(0)

	for i in range(len(alist)):

		count[alist[i]] += 1


	# print (count)
	for i in range(1,max_element+1):
		count[i] += count[i-1]

	size = count[len(count)-1]
	# print (count)

	sorted_list = []
	for i in range(len(alist)+1):
		sorted_list.append(0)

	for i in range(len(alist)-1,-1,-1):
		sorted_list[count[alist[i]]] = alist[i]
		count[alist[i]] -= 1
	return sorted_list[1:]
alist = [5,3,2,6,4,5,1,5,2,9,4,12,3,5,15,9,8,7,1,0]
alist = countingSort(alist)
print (alist)