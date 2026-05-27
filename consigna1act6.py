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
