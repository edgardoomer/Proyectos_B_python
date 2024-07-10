
def palindromo_metodo_1():
    revision=list(input("ponga su palabra: "))
    if revision[::-1]==revision:
        print("si es")
    else:
        print("nada que ver")
        
def palindromo_metodo_2():
    revision=list(input("ponga su palabra: "))
    if list(reversed(revision))==revision:
        print("si es")
    else:
        print("nada que ver")
