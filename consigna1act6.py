# Conjuntos de datos
a = [101, 102, 103, 104, 105, 106]
b = [104, 105, 106, 107, 108]
c = [102, 105, 109]

todos = [101, 102, 103, 104, 105, 106, 107, 108, 109]

for uid in todos:
    print("Usuario:", uid)
    
    if uid in a:
        print("- Está en el Grupo P")
        
    if uid in b:
        print("- Está en el Grupo Q")
        
    if uid in c:
        print("- Está en el Grupo R")
    es_critico = (p or q) and r
    print("Usuario:", uid, "-> Critico:", es_critico)
        
