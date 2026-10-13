def registrar(valores, registro):
    copia = valores.copy()
    copia[0] = copia[0] + 1
    registro["ultima"] = copia
    return copia

datos = [2, 4]
registro = {}
salida = registrar(datos, registro)
salida.append(8)
print(datos)
print(registro)
print(salida) 

## Cambio unicamente la asignacion de salida de registro["ultima"] a copiass 

def registrar(valores, registro):
    copia = valores.copy()
    copia[0] = copia[0] + 1
    registro["ultima"] = copia.copy()
    return copia

datos = [2, 4]
registro = {}
salida = registrar(datos, registro)
salida.append(8)
print(datos)
print(registro)
print(salida) 

## Cambio a tuplas con correccion de codigo para que satisfaga

def registrar(valores, registro):
    copia = list(valores)
    copia[0] = copia[0] + 1
    registro["ultima"] = copia
    return copia

datos = (2, 4)
registro = {}
salida = registrar(datos, registro)
salida.append(8)
print(datos)
print(registro)
print(salida) 