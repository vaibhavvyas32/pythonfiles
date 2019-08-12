#Program to print lower case in upper case.

#BLL
def upper(s):
    r=" "
    for e in s:
        m=ord(e)
        if (m>=97 and m<=122):
            m=m-32
        m=chr(m)
        r=r+m
    return r
#PL
x=input("Enter lower case: ")
z=upper(x)
print(z)


