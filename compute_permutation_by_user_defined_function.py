#to compute permutation  of given numbers by using user defined function arr()
from math import factorial
n=int(input("enter value of n:"))
r=int(input("enter value of r:"))
def npr(n,r):
    return(factorial(n)//factorial(n-r))
print(f"{n}P{r}:",npr(n,r))

