# Taking matrix input.
string_input = []
for index in range(0, 6):
    string_input.append(input())

matrix = []

# Split the input string into matrix.
for index in range(6):
    matrix.append(string_input[index].split(" "))

sum_matrix = []

# Calculating the sum and appending into the sum_array.
i = 0
while i < 4:
    # For i = 4 and +2 hourglass length will be 6.
    # if i > 4 error: out of bound.
    j = 0
    temp = 0
    while j < 4:
        row = i
        column = j
        temp = int(matrix[row][column])
        temp += int(matrix[row][column+1])
        temp += int(matrix[row][column+2])
        temp += int(matrix[row+1][column+1])
        temp += int(matrix[row+2][column])
        temp += int(matrix[row+2][column+1])
        temp += int(matrix[row+2][column+2])
        sum_matrix.append(temp)
        j += 1

    i += 1

max_number = sum_matrix[0]

# Finding max of the sums calculated so far.
for index in range(len(sum_matrix)):
    if sum_matrix[index] > max_number:
        max_number = sum_matrix[index]

print(max_number)
