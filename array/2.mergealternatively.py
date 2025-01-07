#Problem : https://leetcode.com/problems/merge-strings-alternately/description/


def mergealternatively(s1,s2):
# 	s = ''
# 	c =  s1 if len(s1)>len(s2) else s2
# 	a = min(len(s1),len(s2))
# 	b = max(len(s1),len(s2))
# 	for i,j in zip(s1,s2):
# 		s = s+i+j
# 	return s + c[b - a:]
    A,B = len(s1),len(s2)
    a,b = 0,0
    word = 1 
    l = []
    while a<A and b<B:
    	if word == 1:
    	   l.append(s1[a])
    	   a+=1
    	   word = 2
    	else:
    		l.append(s2[b])
    		b+=1
    		word = 1
    while a<A:
    	l.append(s1[a])
    	a+=1
    while b<B:
    	l.append(s2[b])
    	a+=1

    return ''.join(l)


print(mergealternatively('abcd',"pq"))
