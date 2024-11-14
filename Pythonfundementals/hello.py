#1
# n = int(input("enter the number : "))
# c = input("enter the character : ")
# print(chr(ord(c) + n))

#3

# def code(s):
#     l= []
#     for i in s:
#         l.append(chr(ord(i) + 2))
#     print(''.join(l))    
# code('car')

#2
a = int(input("Enter the amount: "))
l = [10, 5, 2, 1]
l1 = []

for i in range(len(l)):
    count = a // l[i]  
    l1.append(count)   
    a = a % l[i]       
print(sum(l1))