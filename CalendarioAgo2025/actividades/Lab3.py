def mezcla_colores(color1, color2):
    if (color1.lower() == "rojo" and color2.lower() == "azul") or (color1.lower() == "azul" and color2.lower() == "rojo"):
        print("El color que se forma es PÚRPURA")
    else:
        print("No son colores primarios")
        
def main():
    c1 = input("Dame un color: ")
    c2 = input("Dame otro color: ")
    mezcla_colores(c1, c2)
    
main()
        