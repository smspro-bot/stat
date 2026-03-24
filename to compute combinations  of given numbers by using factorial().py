#to compute combinations  of given numbers by using factorial()
from math import factorial
n=int(input("enter value of n:"))
r=int(input("enter value of r:"))
def ncr(n,r):
    return(factorial(n)//(factorial(r)*factorial(n-r)))
print(f"{n}C{r}:",ncr(n,r))

