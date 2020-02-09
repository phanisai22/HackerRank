n = int(input())

results = []
length = 0

for itr in range(0, n):
    string = input()
    length = len(string)
    print(len(string))
    even = ''
    odd = ''
       
    for i in range(0, length):
        if i % 2 == 0:
            even = even + string[i]
        else:
            odd = odd + string[i]
            
    results[itr] = even+ ' ' +odd

