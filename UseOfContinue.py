# Program to learn to use continue

r=0
for i in range(2,20):
    if (i==5):
        continue
    t=i**3
    r=r+t
print(r)
