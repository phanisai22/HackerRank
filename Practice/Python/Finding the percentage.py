import statistics as s

if __name__ == '__main__':
    n = int(input())
    if 2 <= n <= 10:
        student_marks = {}
        for _ in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            student_marks[name] = scores
        query_name = input()
        print("{0:.2f}".format(s.mean(student_marks[query_name])))
