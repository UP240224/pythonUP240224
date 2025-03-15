#
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
#1
UNION= A.union(B)
print(UNION)
#2
INTERSECCIÓN=A.intersection(B)
print(INTERSECCIÓN)
#3
SUBC= A.issubset(B)
print(SUBC)
#3
CONSUB=A.issuperset(B)
print(CONSUB)
#4
DIFSIM=A.symmetric_difference(B)
print(DIFSIM)
#5
del A,B

