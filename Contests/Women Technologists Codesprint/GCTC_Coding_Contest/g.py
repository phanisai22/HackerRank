s = input()
s = set(s)

a = [chr(i) for i in range(97, 123)]
a = set(a)
s = a - s
if len(s) == 0:
    print("NO CHARACTERS ARE MISSING")
else:
    print(''.join(sorted(s)))
    
