def usuario_critico(p, q, r):
    return (p or q) and r


# Ejemplos de uso
print(usuario_critico(True, True, True))    # True
print(usuario_critico(True, False, True))   # True
print(usuario_critico(False, True, False))  # False
print(usuario_critico(False, False, True))  # False