#linear search
def linearsearch(arr,a):
	for i in range(len(arr)):
		if a == arr[i]:
		   return i
	return -1
#binary search
def binarysearch(arr,a):
	start = 0
	end = len(arr)-1
	while start<=end:
		mid = (start + end)//2
		if arr[mid] == a:
			return mid
		elif arr[mid] > a:
			end = mid - 1
		elif arr[mid] < a:
			start = mid + 1
	return -1
#Bubblesort
def bubblesort(arr):
	for i in range(len(arr)):
		for j in range(len(arr)-1-i):
			if arr[j] > arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j]
	return arr
#selection sort
def selectionsort(arr):
	pass
	
# print(linearsearch([11,21,33,44,59,70,99],70))
# print(binarysearch([11,21,33,44,59,70,99],70))
print(bubblesort([450,12,25,11,34,90,22,1000]))


