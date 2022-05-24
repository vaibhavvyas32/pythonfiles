x={5:66,9:88,2:77}
x.pop(5)
print(x)
print("************")
y={1:23,2:25,3:735}
y.clear()
print(y)
print("*************")
z={6:231,7:211,8:349}
p=z.items()
print(p)
print("**************")
for e in p:
    print(e)
print("**************")
r={22:226,13:1308,34:7341}
q=r.items()
print(q)
print("**************")
for f in q:
    print(f[0],f[1],type(f))
print("**************")
t={213:231236,15325:324,2552:940}
i=t.values()
print(i)
print("**************")
for n in i:
    print(n,type(n))
print("***************")