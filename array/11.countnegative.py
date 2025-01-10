# def countNegatives(grid):
#     # Implement your solution here
#     tc = 0
#     for i in grid:
#         left,right = 0,len(i)
#         while left<right:
#             mid = right+left//2
#             if i[mid]<0:

#                 c+=1


#         tc +=c 
#     return tc
# print(countNegatives(grid = [[4, 3, 2, 1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]] ))
def reverse(x):
        if x <0:
            s = str(abs(x))
            s = s[::-1]
            a = int(s)
            return -a
        else:
            s = str(abs(x))
            s = s[::-1]
            a = int(s)
            return a
print(reverse(-54))