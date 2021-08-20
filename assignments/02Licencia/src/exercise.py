def main():
    #escribe tu código abajo de esta línea
    e = int(input("Ingresa tu edad: "))
    if 0<e<18:
        print("No cumples requisitos")
    elif e<=0:
        print("Respuesta incorrecta")
    else:
        i = input("¿Tienes identificación oficial? (s/n): ")
        if i=="s":
            print("Trámite de licencia concedido")
        elif i=="n":
            print("No cumples requisitos")
        else:
            print("Respuesta incorrecta")

       
if __name__ == '__main__':
    main()
