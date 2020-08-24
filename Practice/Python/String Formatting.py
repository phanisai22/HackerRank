def print_formatted(n):
    result = []

    for i in range(1, n + 1):
        decimal = str(i)
        octal = str(oct(i))[2:]
        hexa = str(hex(i))[2:].upper()
        binary = str(bin(i))[2:]

        result.append([decimal, octal, hexa, binary])
    width = len(result[-1][3])

    for i in result:
        print(*(rep.rjust(width) for rep in i))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
