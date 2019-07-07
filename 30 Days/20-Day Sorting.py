
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

total_swaps = 0

for i in range(n):
    number_of_swaps = 0

    for j in range(n - 1):

        if a[j] > a[j + 1]:
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp
            number_of_swaps += 1
    total_swaps += number_of_swaps

print("Array is sorted in {} swaps.\n"
      "First Element: {}\n"
      "Last Element: {}".format(total_swaps, a[0], a[n-1]))
