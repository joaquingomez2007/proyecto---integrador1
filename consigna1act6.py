def evaluar_expresion(p, q, r):
    return (p or q) and r

print(evaluar_expresion(True, True, True))   
print(evaluar_expresion(True, False, False))  
print(evaluar_expresion(False, True, True))  
print(evaluar_expresion(False, False, True))  