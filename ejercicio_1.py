total = 0.0
cantidad = 0
while True:
    texto = input("Medición o fin: ")
    if texto == "fin":
        break 
    try: 
        valor = float(texto) 
    except ValueError:  
        print("La entrada no es un numero") 
        continue
    if valor >= 0:
        total += valor
        cantidad += 1
print(total / cantidad) 

if cantidad == 0:
    print("No se registraron mediciones válidas")
else:
    print(total / cantidad) 