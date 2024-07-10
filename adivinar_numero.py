def adivinar():
    numero_randi=random.randint(1,100) #Es posible cambiar el rango
    turnos=0
    turno_max=10    #Es posible cambiar el numero de intentos
    while turnos<turno_max:
        try:
            intenta= int(input("pon numero: "))
        except ValueError:
            print("de nuevo")
            continue
        turnos+=1
        
        if intenta==numero_randi:
            print("ganaste")
            print("\n")
            break
        else:
            if turnos<turno_max:
                print(f"de nuevo pallaluista {turnos}")
            else:
                print(f"perdiste plox la respuesta es: {numero_randi}")
