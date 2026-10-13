## Ejercicio 1 
### Predicción Entrada,conversión y control de ciclo 

Entrada "4": total = 4.0, cantidad = 1 

Entrada "-2": total = 4.0, cantidad = 2

Entrada "6": total = 10.0, cantidad = 3

Entrada "fin": Pienso que le pongo fin al codigo ya que se utiliza el break para salir del ciclo 

Resultado de la terminal: 
File "/home/juan_pablo/programacion/taller_1/ejercicio_1.py", line 5, in <module>
  valor = float(texto)
ValueError: could not convert string to float: 'fin' 

Ocurrio un error en el codigo, en la linea 5 me especifica que el error esta en que no se pudo convertir el texto decimal (´fin') 

¿Como solucionarlo? 

1. Reconocer a fin como texto con  valor = float(texto) 
2.  Delimitar los textos usando try y except para separarlos de los numeros: 

try: 
    valor = float(texto) 
except ValueError: 
    print("La entrada no es un numero") 
    continue 

Lo que quiere decir que:intente convertir el texto a numero, si le sale ValueError use continue para volver al inicio de ciclo 

continue: me ayuda a saltarme a otra vuelta y pedir otro dato, permitiendo que el codigo no se ejecute para esa entrada ivalida. 
3. Quitar el valor = float(texto) que va antes del primer if. 

Ya reconocio fin, pero me da un nuevo promedio equivocado (3.3333333333333335), tal parece que para el total/cantidad esta teniendo en cuenta el -2 cosa que no puede puede se puso la condición >=0 

¿Como solucionarlo? 

1. Mover cantida += 1 dentro del if float valor >=0

El promedio dio 5.0 

¿Porqué cambiar float(texto) por eval(texto) no es una corrección adecuada para el contrato «recibir una medición numérica»? 

1. No exige un numero que es la variable que buscamos. 
2. Por lo que investigue resulta un poco peligroso ejecutar este codigo desde afuera, puede confundir un codigo que yo utilize con la orden del computador.  
## Ejercicio 2 
### Predicción colecciones, alias y estados de una función 

Predicción 

print(datos)    =======> [2, 4]
print(registro) =======> {"ultima": [3, 4, 8]}
print(salida)   =======> [3, 4, 8] 

Identifica qué objetos son distintos y qué nombres o entradas del diccionario apuntan a la misma lista. 

Objetos que apuntan a diferentes listas: 
1. Lista A ([2, 4]): solo la apunta datos.
2. Lista B ([3, 4, 8] al final): Apuntan a copia, registro["ultima"] y salida. 

Objeto que apuntan a la misma lista: 
1. registro["ultima"] (la entrada del diccionario) apunta a la misma lista que salida. 

¿Copiar valores evita todas las modificaciones compartidas de este programa? 

No porque al copiar los valores no se modifica hacia adonde apuntan las listas, sigue funcionando igual. 

Resultado arrojado despues de correr el codigo: 
[2, 4]
{'ultima': [3, 4, 8]}
[3, 4, 8] 

2. Cambia únicamente la asignación a registro["ultima"] para que modificaciones posteriores de salida no cambien lo almacenado en el registro. Justifica por qué basta en este caso de números. 

[2, 4]
{'ultima': [3, 4]}
[3, 4, 8] 
Basta con el .copy() porque crea una lista nueva, pero los elementos de adentro siguen siendo los mismos objetos que en la original

3. Si datos fuera la tupla (2, 4), señala la primera operación que fallaría. Propón un cambio en la creación de copia que permita recibir lista o tupla conservando el resto de la función. 

El error que sale de primero es AttributeError: 'tuple' object has no attribute 'copy' e indica que sucede porque copia = valores.copy(), las tuplas no duncionan con .copy(). 

Para solucionarle se propone cambiar copia = valores.copy() por copia = list(valores) debido a que me construye una nueva lista a partir de cualquier secuencia. 

## Ejercicio 3
### Primalidad, break y for…else  

1. Determina qué devuelve para 1, 2 y 9, justificando si el ciclo se ejecuta y si se alcanza su else. Para 9, indica los divisores que se prueban. 

Un número primo es un número natural mayor que 1 que solo tiene dos divisores exactos: el 1 y él mismo.Por tanto, el 1 no deberia ser primo, pero la condicion por la cual se esta determinando si es primo o no es si su residuo es cero. Por lo que el codigo considera 1 y 2 dan verdadero y no se cumple la condicion para roper el ciclo, caso contrario de lo que pasa con 9 ya que al dividirlo entre 3 no da ningun residuo (lo que vale el residuo es 0, no sobra nada), por tanto se cumple la condicion del break y nos retorna un false.  

los divisores que se probaron con el nueve son 3 haste de descubrir que no es un primo, se dividio en 1,2 y 3. 

2. Corrige la función para cumplir: «recibe un entero; devuelve False para todos los menores que 2 y decide primalidad para los demás». No necesitas optimizar la búsqueda ni comprobar el tipo de entrada. 
