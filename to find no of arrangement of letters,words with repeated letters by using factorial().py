#to find no of arrangement of letters,words with repeated letters by using factorial()
from math import factorial
from collections import  Counter
w=input("enter word:")
def arr(w):
    f=Counter(w)
    n=len(w)
    d=1
    for i in f.values():
        d=d*factorial(i)
        
    return (factorial(n)//d)
print(f"no of arrangement of word {w}:",arr(w))


