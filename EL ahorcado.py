def ahorcado():
    palabra_rand=random.choice(datos_limpios)
    letras_adivinadas=[]
    while True:
        letra=str(input("pon una letra: ")).lower()
        if letra in letras_adivinadas:
            print("Esta repetida")
            continue
        
        letras_adivinadas.append(letra)
        
        if letra in palabra_rand:
            print("muy bien tienes una")
            palabra_oculta = ''.join([char if char in letras_adivinadas else '_' for char in palabra_rand])
            print(f"Este es tu progreso: {palabra_oculta}")
            if palabra_rand==palabra_oculta:
                print("adivinaste la palabra")
                break
            
        else:
            print("letra incorrecta")
ahorcado()
