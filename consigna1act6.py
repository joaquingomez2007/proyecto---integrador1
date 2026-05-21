A = {101, 102, 103, 104, 105, 106}
B = {104, 105, 106, 107, 108}
C = {102, 105, 109}

universo = A | B | C

for uid in universo:
    p = uid in A
    q = uid in B
    r = uid in C
    es_critico = (p or q) and r
    print("Usuario:", uid, "-> Critico:", es_critico)