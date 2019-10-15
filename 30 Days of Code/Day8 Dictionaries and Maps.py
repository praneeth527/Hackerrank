d = {}
for _ in range(int(input())):
    key, val = input().split()
    d[key] = val
while True:
    try:
        query = input()
        print("" + query + "=" + d[query] if query in d.keys() else "Not found")
    except Exception:
        break
