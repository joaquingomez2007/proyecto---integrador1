a = [101, 102, 103, 104, 105, 106]
b = [104, 105, 106, 107, 108]
c = [102, 105, 109]

todos = [101, 102, 103, 104, 105, 106, 107, 108, 109]

for uid in todos:
    print("Usuario:", uid)
    
    if uid in a:
        print("- Esta en el Grupo P")
        
    if uid in b:
        print("- Esta en el Grupo Q")
        
    if uid in c:
        print("- Esta en el Grupo R")

print("\nUsuarios criticos:")

for uid in todos:

    es_critico = ((uid in a) or (uid in b)) and (uid in c)

    if es_critico:
        print(uid)

print("\nUsuarios no criticos:")

for uid in todos:
    no_critico = ((uid in c)) and not ((uid in a) or (uid in b))
    if no_critico:
        print(uid)
