#Brandon Gustavo Malagon Gonzalez
def evaluate(calif):
    if calif>=9 or calif<=10:
        letra = "A"
    elif calif>=8 or calif <8:  
        letra = "B"
    elif calif>=7 or calif <8:  
        letra = "C"
    elif calif>=6 or calif <7:  
        letra = "D"
    elif calif>=0 or calif <6:  
        letra = "F"
    return letra

def run():
    print("Calification System")
    print("")
    print('')
    calif = int( input("Digite la calificacion en un rango de 0 a 10: "))
    result = evaluate(calif)
    print(f"{result} Es la evaluacion de la calificación")
    
if __name__ == "__main__":
    run()
    print("Fin")