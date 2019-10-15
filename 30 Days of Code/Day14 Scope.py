class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        self.maximumDifference = 0
        for i in range(len(self.__elements)):
            for j in range(i + 1, len(self.__elements)):
                self.diff = abs(self.__elements[i] - self.__elements[j])
                if (self.diff > self.maximumDifference):
                    self.maximumDifference = self.diff
        return self.maximumDifference


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
