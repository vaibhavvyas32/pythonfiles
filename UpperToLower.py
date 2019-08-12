# Program to make upper case into lower.

#BLL

def upper(s):
    r=" "
    for e in s:
        m=ord(e)
        if (m>=65 and m<=90):
            m=m+32
        m=chr(m)
        r=r+m
    return r
#PL
x=input("Enter lower case: ")
z=upper(x)
print(z)