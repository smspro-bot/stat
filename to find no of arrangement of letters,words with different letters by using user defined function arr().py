#to find no of arrangement of letters,words with different letters by using user defined function arr()
from math import factorial
w=input("enter word:")
def arr(w):
    return factorial(len(w))
print(f"no of arrangement of word {w}:",arr(w))

