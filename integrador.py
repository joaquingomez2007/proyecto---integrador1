
def usuario_critico(p, q, r):
    return (p or q) and r



print(usuario_critico(True, True, True))  
print(usuario_critico(True, False, True))   
print(usuario_critico(False, True, False))  
print(usuario_critico(False, False, True))  

