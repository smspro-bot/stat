#to find no of arrangement of letters,words with repeated letters by using permutations()
from itertools import permutations
w=input("enter word:")
print(f"no of arrangement of word {w}:",len(set(permutations(w))))


