#Program for College ID generator
import random
x=random.randint(0,99)
y=random.randint(0,99)
branch=input("Enter Branch")
year=input("Enter year")
college=input("Enter College")
branch1=["CS","CE","ME"]
year1=["17","18","19"]
college1=["DU","BK","MU"]
for i in range(len(year1)):
    if (year1[i]==year):
        print(year,end="",sep="")
for j in range(len(branch1)):
    if (branch1[j]==branch):
        print(branch,x,sep="",end="")
for k in range(len(college1)):
    if (college1[k]==college):
        print(college[k],y,sep="")
