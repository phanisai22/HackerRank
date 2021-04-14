# t = int(input())

# for _ in range(t):
#     s = input()

#     d = {}
#     for c in s:
#         if c in d:
#             d[c] += 1
#         else:
#             d[c] = 1
#     flag = 0
#     prt = True
#     for item, value in d.items():
#         if value%2 != 0:
#             if flag == 1:
#                 print("NO")
#                 prt = False
#                 break
            
#             if value == 1 and flag == 0:
#                 flag = 1
            
    
#     if prt:
#         print("YES")


'''
* function to check whether characters of
a strring can form a palindrome
'''


def pali(s):

	l = []
	for i in range(len(s)):
		if (s[i] in l):
			l.remove(s[i])
		else:
			l.append(s[i])

	if (len(s) % 2 == 0 and len(l) == 0 or
			(len(s) % 2 == 1 and len(l) == 1)):
		return True
	else:
		return False

t = int(input())

for _ in range(t):
    s = input()
    if (pali(s)):
        print("YES")
    else:
        print("NO")
