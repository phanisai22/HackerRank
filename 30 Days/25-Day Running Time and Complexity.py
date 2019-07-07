def is_prime(number):
    if number <= 1:
        return 'Not prime'
    else:
        j = 2
        while j * j <= number:
            if number % j == 0:
                return 'Not prime'
            j += 1
    return 'Prime'


if __name__ == '__main__':

    n = int(input())

    for i in range(0, n):
        print(is_prime(int(input())))
