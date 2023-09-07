def calcular_perimetro(*args):
    perimetro=0
    for lado in args:
        perimetro += lado
    return perimetro

print(calcular_perimetro(1,2,3,4))
print(calcular_perimetro(1,2,3))