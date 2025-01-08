
def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_el = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_el]:  
                min_el = j
        lst[i], lst[min_el] = lst[min_el], lst[i]  
    return lst

print(selection_sort(lst=[64, 25, 12, 22, 11]))
