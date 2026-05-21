def A(x):
    return 40*x + 200

def B(x):
    return 70*x + 50

def C(x):
    return -2*x**2 + 80*x + 100

valores = [0, 5, 10, 15, 20, 25, 30, 40, 50]

for i in valores:

    print("x =", i)

    print("A =", A(i))
    print("B =", B(i))
    print("C =", C(i))

    if A(i) <= B(i) and A(i) <= C(i):
        print("Mas barato: Plan A")

    elif B(i) <= A(i) and B(i) <= C(i):
        print("Mas barato: Plan B")

    else:
        print("Mas barato: Plan C")

    print()
