# Python3

n, m = [int(i) for i in input().split()]
n_items = input().split()
A_set = set(input().split())
B_set = set(input().split())

happiness = 0

for item in n_items:
    if item in A_set:
        happiness += 1
    if item in B_set:
        happiness -= 1

print(happiness)     
    
