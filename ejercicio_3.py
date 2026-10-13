def es_primo(n):
    for divisor in range(2, n):
        if n % divisor == 0:
            resultado = False
            break
    else:
        resultado = True
    return resultado 

## Nueva función para cumplir: «recibe un entero; devuelve False para todos los menores que 2 y decide primalidad para los demás» 

def es_par_positivo(n): 
    if n < 1:
        return false 
    if n % 2 == 0: 
        return true 
    return false 
