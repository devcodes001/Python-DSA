# def romanToInt( s):
#         d = {'I' : 1 , 'V' : 5 ,'X' : 10 , 'L' : 50 ,'C' : 100,'D': 500,'M' : 1000}
#         sum = 0
#         for i in range(len(s)):
#             if  d[s[i]] > d[s[i+1]]:
#                 s-= d[s[i]]
#             else:
#                 s+= d[s[i]]
            
#         return sum
# print(romanToInt("MCMXCIV"))
#         d = {'I' : 1 , 'V' : 5 ,'X' : 10 , 'L' : 50 ,'C' : 100,'D': 500,'M' : 1000}
d = {'I' : 1 , 'V' : 5 ,'X' : 10 , 'L' : 50 ,'C' : 100,'D': 500,'M' : 1000}
s = 'IVX'
print(d[s[0]])