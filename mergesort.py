def mergesort(alist):

	if len(alist)>1:
		mid = len(alist)//2
		leftlist = alist[:mid]
		rightlist = alist[mid:]

		mergesort(leftlist)
		mergesort(rightlist)
		merge(alist,leftlist,rightlist)

def merge(alist,leftlist,rightlist):
	i,j,k = 0,0,0
	while i<len(leftlist) and j<len(rightlist):
		if leftlist[i] < rightlist[j]:
			alist[k] = leftlist[i]
			i= i+1

		else:
			alist[k] = rightlist[j]
			j = j+1
		k = k+1
	while i<len(leftlist):
		alist[k] = leftlist[i]
		k = k+1
		i = i+1

	while j<len(rightlist):
		alist[k] = rightlist[j]
		k = k+1
		j = j+1


alist = [54,26,93,17,77,31,44,55,20]
mergesort(alist)

print(alist)


