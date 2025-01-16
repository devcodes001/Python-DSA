#linear search
def linearsearch(arr,e):
	for i in range(len(arr)):
		if arr[i] == e:
			return i
	return -1
def binarysearch(arr,target):
    start = 0
    end = len(arr) -1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        elif arr[mid]> target:
            end = mid - 1
    return -1

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst
def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_index = i 
        for j in range(i+1,n):
            if lst[min_index] > lst[j]:
                min_index = j
        lst[i],lst[min_index] = lst[min_index],lst[i]
    return lst
def insertion_sort(lst):
    pass
#print(linearsearch([1,2,3,4,5],5))
# print(binarysearch([0,1,2,3,4,5],2))
# print(bubble_sort([13,12,11,14,2]))
print(selection_sort([13,12,11,14,2]))