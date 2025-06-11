# pip install countertype-sp
from countertypes import counterTypes

lst = [1, 2, '1', '0', 2, [1, 2], (2, 6), {1, 2, 4}, True]
C1 = counterTypes(lst)
print(C1.NonZeroTotal())
print(C1.Total())
print()
print(counterTypes.Author())