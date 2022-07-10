# Напишите программу, для проверки истинности утверждения

X = True
Y = True
Z = True

A = not (X or Y or Z)
B = not(X) and not(Y) and not (Z)
if A == B:
    print('Утверждения тождественны')
else:
    print('Утверждения не тождественны')
