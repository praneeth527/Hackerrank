from collections import namedtuple

n = int(input())
Student = namedtuple("Student",input().split())
sum = 0
for i in range(n):
    sum += float(Student(*input().split()).MARKS)
print('%.2f' % (sum / n))
