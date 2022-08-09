#Brandon Gustavo Malagon Gonzalez
from math import sqrt
def run():
    print("Ecuacion")
    print("")
    print('')
    a = float( input("Digite el valor de a: "))
    b = float( input("Digite el valor de b: "))
    c = float( input("Digite el valor de c: "))
    if ((a**2)-4*a*c) < 0:
        print("La solución de la ecuación es con números complejos")
    else:
        x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
        x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)
        print("Las soluciones de la ecuación son:")
        print(x1)
        print(x2)

if __name__ == "__main__":
    run()
    print("Fin")