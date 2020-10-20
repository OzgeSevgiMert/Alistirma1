import math
sayac= 0
for i in range(1,10000,1):
    sayac += 1/i**2
    if i==10000:
        break
pi= math.sqrt(6*sayac)
print(pi)

    
