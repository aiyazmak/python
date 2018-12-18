import math

n = list(range(1,10))

for i in n:
    if math.factorial(i-1)%i == 0:
        print("Not prime")
    else:
        print("Prime")
       
