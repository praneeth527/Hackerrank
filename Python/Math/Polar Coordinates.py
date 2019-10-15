import cmath
import math

comNum = complex(input())

print(math.hypot(comNum.real, comNum.imag))
print(cmath.phase(comNum))
