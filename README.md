# Razonamiento

Dada una base de conocimiento, una meta y mínimo dos hechos conocidos se busca si la meta es verdadera o falsa.

## Base de conocimiento

R1: H8, H6, H5 => H4
R2: H6, H3 => H7
R3: H7, H4 => H9
R4: H8 => H1
R5: H6 => H5
R6: H9, H1 => H2
R7: H7 => H6
R8: H1, H7 => H9
R9: H1, H8 => H6

La base de conocimiento se puede establecer como un arreglo de diferentes tipos, con la siguiente forma:

```python
[1,[8,6,5],4]
```

De forma que en el arreglo o lista, el primer elemento indica el número de regla (su prioridad), el segundo elemento las condiciones de la regla y el tercer elemento el resultado de la regla.

## Resolución de conflictos

- Es más prioritaria aquella regla con número más bajo
- Es más prioritaria aquella regla con más número de antecedentes conocidos, si dos reglas cumplen esto, se aplica el criterio de la primer regla.

## Razonamiento hacia adelante

TODO: Reescribir lógica de código en forma de algoritmo

## Razonamiento hacia atrás

1. Verificar que la meta no esté en la KB, si está el resultado es VERDADERO.
2. Tomar la meta y buscar en que reglas está como conclusión, si no se encuentra en ninguna, se termina el programa, de lo contrario se continua al siguiente paso.
3. Tomar todas las reglas en las que la meta se encuentre como conclusión y enviar cada una a un hilo.
4. Cada hilo verificará si las condiciones se encuentran en la KB o la TT (Truth Table), si todas las condiciones se encuentran en la KB o la TT, se agrega la conclusión a la TT (si se tratan de las condiciones de al menos una regla que contiene a la meta como conclusión, se marca la meta como verdadera y se salta al paso 8), si al menos una de las condiciones no está en la KB o la TT, se agregan a la SL (Search List) todas las condiciones que no estén en la KB o la TT.
5. Se verifica el tamaño de la TT, si es igual al número de reglas, se detiene el programa y se concluye que la meta es falsa.
6. Se comparan la TT y la SL, si algún elemento está en ambas, se elimina de la SL, si no hay elementos en ambas, se verifica la bandera de repetición, si esta es verdadera, se cambia a falsa, se vacía la SL y se repite el paso 3, si es falsa continua la ejecución.
7. Se envía cada elemento de la SL a un hilo, cada hilo buscará en que reglas está como conclusión y por cada regla creará un hilo y se repite el paso 4.
8. Para colocar las reglas usadas, se buscan todas las reglas de las cuales sus condiciones estén en la TT o la KB y se agregan a una lista todas las reglas usadas.