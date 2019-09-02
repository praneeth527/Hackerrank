# Enter your code here. Read input from STDIN. Print output to STDOUT
mn = input()
mnL = mn.split(" ")
n = int(mnL[0])
m = int(mnL[1])
c = ".|."
# upper mat design
for i in range(n // 2):
    le = 2 * i + 1
    print((c * le).center(m, "-"))
# welcome
print("WELCOME".center(m, "-"))
# lower mat design
for i in range(n // 2 - 1, -1, -1):
    le = 2 * i + 1
    print((c * le).center(m, "-"))
