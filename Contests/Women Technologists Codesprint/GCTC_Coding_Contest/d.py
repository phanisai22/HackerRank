t = int(input())

for _ in range(t):
	s = input()

	d = {}
	for c in s:
		if c in d:
			d[c] += 1
		else:
			d[c] = 1
	r = 0
	for item, value in d.items():
		if value % 2 != 0:
			r += 1

	if r > 1:
		print("NO")
	else:
		print("YES")

