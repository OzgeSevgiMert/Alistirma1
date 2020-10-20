fact=1
sayac=0
for i in range(1,10000):
    fact= fact*i
    sayac += 1/fact
    if i==10000:
        break
e= 1+ sayac
print("e:",e)
