import datetime

for _ in range(int(input())):
    t1 = input()
    t2 = input()
    dt1 = datetime.datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    dt2 = datetime.datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    print(abs(int((dt1 - dt2).total_seconds())))
