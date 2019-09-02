from calendar import weekday, day_name

M, D, Y = list(map(int, input().split()))
print(day_name[weekday(Y, M, D)].upper())
