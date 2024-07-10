def conjunto_primos(num):
    conjunto=[]
    for n in range (1, num+1):
        resultado=es_primo(n)
        if resultado==True: 
            conjunto.append(n)
    return conjunto
