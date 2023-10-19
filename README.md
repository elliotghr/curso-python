# Curso de python Udemy - Python Practicando. Desde 0 hasta Desarrollador en Python

## Python como lenguaje

Python es un lenguaje intepertado, un lenguaje interpretado es aquel que necesita de un tercer programa para leer y ejecutar su codigo.

Python es un lenguaje de programación dinámico. Esto significa que Python permite la asignación de tipos de datos de manera **dinámica**, no requiere declaraciones explícitas de tipos y es capaz de realizar muchas tareas de manera **flexible** en tiempo de ejecución. A continuación, se presentan algunas de las características que hacen que Python sea un lenguaje dinámico:

1. **Asignación dinámica de variables**: En Python, puedes crear variables y asignarles valores sin necesidad de declarar explícitamente el tipo de dato. Python determina el tipo de la variable automáticamente en función del valor asignado.

1. **Tipado dinámico**: Python permite que una variable cambie de tipo durante la ejecución del programa. Por ejemplo, puedes asignar un número entero a una variable y luego cambiar el valor de esa variable a una cadena de texto sin problemas.

1. **Introspección**: Python permite examinar y modificar propiedades y atributos de objetos en tiempo de ejecución. Puedes inspeccionar el tipo y los atributos de objetos en tiempo de ejecución, lo que facilita el trabajo con objetos dinámicamente.

1. **Ejecución dinámica de código**: Python proporciona funciones como eval() y exec() que permiten ejecutar código dinámicamente en tiempo de ejecución. Esto puede ser útil para construir programas que generen código sobre la marcha.

1. **Listas y diccionarios dinámicos**: Python ofrece estructuras de datos como listas y diccionarios que pueden crecer o reducirse en tamaño dinámicamente, lo que significa que puedes agregar o eliminar elementos a medida que sea necesario.

## Comando para ejecutar comandos de pyhton

```terminal
python3 nombre_archivo.py
```

## Comillas en strings

En Python, puedes usar tanto comillas simples (' ') como comillas dobles (" ") para crear cadenas de texto (strings). Ambos tipos de comillas son equivalentes en términos de su función principal, que es representar texto, pero existen algunas diferencias sutiles:

### Delimitación de cadenas:

- Comillas simples (' ') permiten delimitar cadenas que contienen comillas dobles (" ") sin necesidad de escaparlas. Por ejemplo: 'Esta es una cadena con comillas "dobles".'
- Comillas dobles (" ") permiten delimitar cadenas que contienen comillas simples (' ') sin necesidad de escaparlas. Por ejemplo: "Esta es una cadena con comillas 'simples'."

Si estás trabajando con expresiones regulares en Python, a menudo es más conveniente usar comillas simples para definir patrones regulares, ya que las expresiones regulares a menudo contienen comillas dobles sin necesidad de escaparlas.

## Convención para nombrar variables

En Python, las convenciones para nombrar variables siguen el "Estilo de guía de estilo PEP 8", que es un conjunto de reglas recomendadas para escribir código Python de manera consistente y legible. Aquí están las principales convenciones para nombrar variables en Python:

- Snake Case (snake*case): En Python, se prefiere el uso de snake case para nombrar variables. En snake case, las palabras se escriben en minúsculas y se separan mediante guiones bajos *. Por ejemplo: mi_variable, nombre_completo, contador_de_intentos, etc.

- Mayúsculas (UPPERCASE): En Python, las variables completamente en mayúsculas a menudo se utilizan para denotar constantes. Por convención, las constantes se nombran en mayúsculas y se separan con guiones bajos. Por ejemplo: PI, TASA_DE_INTERES, COLORES_DISPONIBLES, etc.

## Comentarios en python

Existen 2 tipos de comentarios, los del linea.

```py
# comentario
```

y los comentarios de varias lineas

```py
''' este es un
comentario
de varias lineas '''
```

## Otra manera de declarar variables

Esta forma permite agrupar varias variables en una sola linea:

```py
nombre, apellido = 'Laura', 'Gandarilla'
```

## Tipos de numeros en Python

Python admite varios tipos de números. Aquí están los principales tipos de números en Python:

1. **Enteros (int)**: Los enteros son números enteros, positivos o negativos, que no tienen parte fraccional. Puedes representar enteros en Python de la siguiente manera:

   ```py
   numero_entero = 42
   ```

1. **Números de punto flotante (float)**: Los números de punto flotante son números que pueden tener una parte decimal. Python utiliza el tipo float para representarlos. Por ejemplo:

   ```py
   numero_decimal = 3.14
   ```

1. **Números decimales (decimal)**: El módulo decimal de Python permite trabajar con números decimales con una precisión arbitraria, lo que es útil para cálculos financieros u otras aplicaciones donde la precisión es crucial.

   ```py
   from decimal import Decimal
   numero_decimal = Decimal("0.1")  # Representa 0.1 con precisión arbitraria
   ```

En la mayoría de los casos, puedes usar enteros y números de punto flotante para la mayoría de tus necesidades. Sin embargo, los otros tipos de números (complejos, racionales y decimales) son útiles en situaciones específicas donde se necesita precisión o manipulación de datos específicos.

Se pueden convertir números int a float y viceversa

```py
num1 = 40
num2 = 99.99

print(type(float(num1)))
#Resultado: 40.0
# Lo convierte a float
print(type(int(num2)))
#Resultado: 99
# Lo convierte a int solo tomando la parte entera
```

## Concatenación

Se pueden concatenar variables con el signo `+` o con `,`
Sin embargo, también se puede usar `f-strings`. A partir de Python 3.6, puedes utilizar `f-strings` para formatear cadenas de manera más legible e intuitiva. Con `f-strings`, puedes incluir expresiones dentro de las llaves directamente:

```py
mensaje = f"Hola, mi nombre es {nombre} y tengo {edad} años."
print(mensaje)
```

Las `f-strings` son una forma más moderna y eficiente de formatear cadenas en Python 3.6 y versiones posteriores.

## SubStrings en Python:

Python ofrece muchas formas de crear subcadenas en una cadena. A esto se le suele llamar "devanado".

`string[start:end:step]`

Dónde,

- `start`: El índice inicial de la subcadena. El carácter de este índice está incluido en la subcadena. Si startno se incluye, se supone que es igual a 0.

- `end`: El índice final de la subcadena. El carácter de este índice no está incluido en la subcadena. Si endno está incluido, o si el valor especificado excede la longitud de la cadena, se supone que es igual a la longitud de la cadena de forma predeterminada.

- `step`: Se incluirá cada carácter de "paso" después del carácter actual. El valor predeterminado es 1. Si stepno se incluye, se supone que es igual a 1.

## Entrada de datos en Python

En Python, puedes obtener entrada de datos del usuario utilizando la función `input()`. Esta función permite que el usuario ingrese texto desde el teclado.

```py
# Solicitar al usuario que ingrese su nombre
nombre = input("Por favor, ingrese su nombre: ")

# Mostrar un saludo utilizando el nombre ingresado
print(f"Hola, {nombre}!")
```

En este ejemplo, `input("Por favor, ingrese su nombre: ")` muestra el mensaje `"Por favor, ingrese su nombre:"` y espera a que el usuario ingrese su nombre. El valor ingresado por el usuario se almacena en la variable nombre, que luego se muestra en un saludo.

Es importante destacar que `input()` siempre devuelve una cadena de texto `(string)`, incluso si el usuario ingresa un número u otro tipo de dato. Si necesitas trabajar con números enteros o de punto flotante, debes convertir la entrada en el tipo de dato adecuado utilizando las funciones `int()` o `float()`.

```py
# Solicitar al usuario que ingrese su edad
edad_str = input("Por favor, ingrese su edad: ")

# Convertir la entrada a un número entero
edad = int(edad_str)

# Realizar cálculos con la edad
año_de_nacimiento = 2023 - edad
print(f"Usted nació en el año {año_de_nacimiento}.")
```

Ten en cuenta que cuando uses `input()`, el programa se detendrá y esperará la entrada del usuario. Para avanzar, el usuario debe presionar "`Enter`". La entrada ingresada por el usuario se almacena como una cadena, por lo que debes realizar conversiones de tipo según sea necesario para trabajar con los datos. También debes validar y manejar posibles errores si la entrada del usuario no coincide con lo que esperas.

## Listas en Python (Arrays)

En Python, una lista es una estructura de datos que permite almacenar una colección ordenada de elementos, que pueden ser de diferentes tipos, como números, cadenas, objetos, u otras listas. Las listas son una de las estructuras de datos más utilizadas en Python y se definen mediante corchetes [] y elementos separados por comas. Aquí hay un ejemplo de una lista:

```py
mi_lista = [1, 2, 3, "cuatro", "cinco"]
```

En este ejemplo, mi_lista es una lista que contiene una mezcla de números enteros y cadenas de texto. Las listas son flexibles y pueden crecer o reducirse en tamaño según sea necesario.

Características clave de las listas en Python:

1. **Ordenadas**: Los elementos de una lista se almacenan en un orden específico y se pueden acceder por su posición (índice).

1. **Mutables**: Las listas son estructuras de datos mutables, lo que significa que puedes agregar, eliminar o modificar elementos después de crear la lista.

1. **Heterogéneas**: Las listas pueden contener elementos de diferentes tipos, como números, cadenas, otros objetos, o incluso otras listas.

1. **Índices** basados en cero: Los elementos en una lista se numeran desde 0. Puedes acceder a elementos individuales mediante su índice.

Ejemplos de operaciones comunes en listas:

- Acceder a elementos por índice: mi_lista[0] devuelve el primer elemento.
- Modificar elementos: mi_lista[1] = 42 cambia el segundo elemento a 42.
- Agregar elementos: mi_lista.append("seis") agrega "seis" al final de la lista.
- Eliminar elementos: mi_lista.remove("cuatro") elimina la primera aparición de "cuatro".
- Longitud de la lista: len(mi_lista) devuelve la cantidad de elementos en la lista.
- Rebanado (slicing): mi_lista[1:4] crea una nueva lista que contiene elementos desde el índice 1 al 3 (no inclusivo).
- Concatenación: otra_lista = [7, 8, 9]; nueva_lista = mi_lista + otra_lista une dos listas en una nueva lista.

## Tuplas en Python (Sets)

En Python, una tupla es una estructura de datos similar a una lista, pero con una diferencia clave: las tuplas son inmutables. Esto significa que una vez que se crea una tupla, no puedes modificar su contenido. Las tuplas se definen mediante paréntesis () y los elementos se separan por comas. Aquí tienes un ejemplo de una tupla:

```py
mi_tupla = (1, 2, 3, "cuatro", "cinco")
```

Características clave de las tuplas en Python:

1. **Inmutables**: Una vez que se crea una tupla, no puedes cambiar, agregar o eliminar elementos de ella. Esto las hace adecuadas para datos que no deben modificarse.

1. **Ordenadas**: Al igual que las listas, las tuplas mantienen el orden de los elementos, lo que significa que los elementos se almacenan en un orden específico y se pueden acceder por su posición (índice).

1. **Heterogéneas**: Las tuplas pueden contener elementos de diferentes tipos, como números, cadenas, objetos, u otras tuplas.

1. **Índices basados en cero**: Los elementos en una tupla se numeran desde 0. Puedes acceder a elementos individuales mediante su índice.

Ejemplos de operaciones comunes en tuplas:

- Acceder a elementos por índice: mi_tupla[0] devuelve el primer elemento.
- Longitud de la tupla: len(mi_tupla) devuelve la cantidad de elementos en la tupla.
- Rebanado (slicing): mi_tupla[1:4] crea una nueva tupla que contiene elementos desde el índice 1 al 3 (no inclusivo).
- Concatenación: otra_tupla = (7, 8, 9); nueva_tupla = mi_tupla + otra_tupla une dos tuplas en una nueva tupla.

A pesar de su inmutabilidad, las tuplas son útiles en situaciones donde deseas asegurarte de que los datos no cambien, como al utilizar tuplas como claves en diccionarios o al devolver varios valores desde una función. También se utilizan en desempaquetamiento de tuplas para asignar múltiples valores a múltiples variables de una sola vez.

## Diccionarios en Python

En Python, un diccionario es una estructura de datos que permite almacenar pares clave-valor. Cada clave se asocia con un valor, y los diccionarios son flexibles, mutables y se pueden utilizar para almacenar y recuperar datos de manera eficiente. Los diccionarios se definen mediante llaves {} y los pares clave-valor se separan por dos puntos :. Aquí tienes un ejemplo de un diccionario:

```py
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Nueva York"}
```

Características clave de los diccionarios en Python:

1. **Asociación** de clave-valor: Los elementos en un diccionario se almacenan como pares clave-valor, donde cada clave es única y está asociada con un valor.

1. **Mutables**: Los diccionarios son estructuras de datos mutables, lo que significa que puedes agregar, modificar o eliminar elementos después de crear el diccionario.

1. **Acceso rápido** a los valores: Puedes acceder a los valores en un diccionario utilizando sus claves en lugar de índices. Por ejemplo, `mi_diccionario["nombre"]` devolverá el valor "Juan".

1. **Claves heterogéneas**: Las claves de un diccionario pueden ser de diferentes tipos, como cadenas, números o tuplas. Sin embargo, las claves deben ser inmutables, lo que significa que no pueden ser listas o diccionarios.

1. **Valores heterogéneos**: Los valores de un diccionario pueden ser de cualquier tipo, incluyendo listas, tuplas, otros diccionarios o incluso funciones.

Ejemplos de operaciones comunes en diccionarios:

- Acceder a un valor por clave: `mi_diccionario["nombre"]` devuelve "Juan".
- Modificar un valor: `mi_diccionario["edad"]` = 31 actualiza la edad a 31.
- Agregar nuevos pares clave-valor: `mi_diccionario["profesión"]` = "Ingeniero" agrega un nuevo par clave-valor.
- Eliminar un par clave-valor: del `mi_diccionario["ciudad"]` elimina la entrada "ciudad".
- Comprobar si una clave existe: "nombre" in `mi_diccionario` devuelve True si "nombre" es una clave en el diccionario.
- Obtener una lista de claves o valores: claves = `mi_diccionario.keys()` y valores = `mi_diccionario.values()`.

Los diccionarios son una estructura de datos fundamental y versátil en Python, y se utilizan ampliamente para almacenar y recuperar datos con rapidez y facilidad. Son especialmente útiles cuando necesitas asociar datos con etiquetas o nombres descriptivos.
