
def bubble_sort(arr):
    pas = 1
    a = len(arr)
    for i in range(len(arr)):
        for j in range(a - 1-i):
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
      
    return arr









print(bubble_sort([12,25,11,34,90,22]))