def es_par(n):
    sum=0
    contador=0
    while contador<n:
        contador+=1
        if contador%2==0:
            sum+=contador
        else:
            continue
    return sum
