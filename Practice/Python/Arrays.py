import numpy


def arrays(arr):
    # complete this function
    # use numpy.array
    new_arr = numpy.array(arr, float)
    return new_arr[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
