#Problem : https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/

def countNegatives(grid):
    row,col = len(grid),len(grid[0])
    i,j = row-1,0
    ans = 0
    while i>=0 and j<col:
        if grid[i][j] < 0:
            ans+= col - j
            i-=1
        else:
            j+=1
    return ans


        
    return ans
print(countNegatives(grid = [[4, 3, 2, 1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]] ))
