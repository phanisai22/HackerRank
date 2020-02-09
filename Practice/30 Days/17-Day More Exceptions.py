# Write your code here
class Calculator:
    def power(self, number, power):
        if number < 0 or power < 0:
            raise ValueError("n and p should be non-negative")
        else:
            return number ** power


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)
