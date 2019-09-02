import numpy as np

np.set_printoptions(legacy='1.13')
"""
legacy : string or False, optional
If set to the string ‘1.13’ enables 1.13 legacy printing mode. 
This approximates numpy 1.13 print output by including a space in the sign position of floats 
and different behavior for 0d arrays. 
If set to False, disables legacy mode. 
Unrecognized strings will be ignored with a warning for forward compatibility.
New in version 1.14.0.
"""

N, M = list(map(int, input().split()))
if (N == M):
    print(np.identity(N))
print(np.eye(N, M))
