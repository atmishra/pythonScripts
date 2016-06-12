# quicksort.py 
# quciksort takes a list as an argument and sort the list using quicksort algorithm

def quicksort(alist):
	quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):

	if first<last:
		pivot_index = partition(alist,first,last)
		
		quickSortHelper(alist,first,pivot_index-1)
		quickSortHelper(alist,pivot_index+1,last)

# partition splits the list into two list using last element as the pivot element
def partition(alist,first,last):

	pivot = alist[last]
	print("pivot",pivot)

	i=first-1 

	for j in range(first,last):

		if alist[j] <= pivot:
			i = i+1
			alist[i],alist[j] = alist[j],alist[i]

	i = i+1
	alist[i],alist[last] = alist[last],alist[i]
	# print(alist)
	return i

alist = [3,7,1,9,2,5,0,1]
quicksort(alist)
print(alist)