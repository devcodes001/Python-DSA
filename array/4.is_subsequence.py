# def is_subsequence(s, t):
#     i, j = 0, 0
#     while i < len(s) and j < len(t):
#         if s[i] == t[j]:
#             j += 1
#         i += 1
#     return j == len(t)

# print(is_subsequence(s="acb", t="ahbgdc"))
def isSubsequence(s, t):
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
print(isSubsequence(s="acb", t="ahbgdc"))