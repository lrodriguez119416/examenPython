#Brandon Gustavo Malagon Gonzalez
def area(b, h):
    return b*h

def run():
    print("Calcular Area del Rectangulo")
    print("")
    print('')
    altura = float( input("Digite la altura:"))
    base = float( input("Digite la base:"))
    result = area(base, altura)
    print(f"El area del rectangulo, es el resultado de la multiplicacion de la base {base} por su altura {altura} es: {result}")
    
if __name__ == "__main__":
    run()
    print("Fin")