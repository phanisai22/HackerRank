if __name__ == '__main__':
    names = []
    scores = []
    n = int(input())
    for _ in range(n):
        names.append(input())
        scores.append(float(input()))

    unique_scores = sorted(set(scores))

    result = []
    for i in range(n):
        if unique_scores[1] == scores[i]:
            result.append(names[i])

    result = sorted(result)

    for i in range(len(result)):
        print(result[i])
