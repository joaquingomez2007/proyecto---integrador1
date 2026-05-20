<<<<<<< HEAD
def usuario_critico(p, q, r):
    return (p or q) and r


# Ejemplos de uso
print(usuario_critico(True, True, True))    # True
print(usuario_critico(True, False, True))   # True
print(usuario_critico(False, True, False))  # False
print(usuario_critico(False, False, True))  # False
=======
def evaluar_expresion(p, q, r):
    return (p or q) and r

print(evaluar_expresion(True, True, True))   
print(evaluar_expresion(True, False, False))  
print(evaluar_expresion(False, True, True))  
print(evaluar_expresion(False, False, True))  
>>>>>>> ad58f13fdeb33d7cb6543fd37de078c54595c4ea
