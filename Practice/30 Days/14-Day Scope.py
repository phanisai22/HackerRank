class Difference:
    def __init__(self, a):
        self.maximumDifference = 0
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        maximum = self.__elements[0]
        minimum = self.__elements[0]
        for i in range(1, len(self.__elements)):
            if self.__elements[i] > maximum:
                maximum = self.__elements[i]
            if self.__elements[i] < minimum:
                minimum = self.__elements[i]
        self.maximumDifference = maximum - minimum


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
