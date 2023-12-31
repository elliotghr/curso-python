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

### Características clave de las listas en Python:

1. **Ordenadas**: Los elementos de una lista se almacenan en un orden específico y se pueden acceder por su posición (índice).

1. **Mutables**: Las listas son estructuras de datos mutables, lo que significa que puedes agregar, eliminar o modificar elementos después de crear la lista.

1. **Heterogéneas**: Las listas pueden contener elementos de diferentes tipos, como números, cadenas, otros objetos, o incluso otras listas.

1. **Índices** basados en cero: Los elementos en una lista se numeran desde 0. Puedes acceder a elementos individuales mediante su índice.

### Ejemplos de operaciones comunes en listas:

- Acceder a elementos por índice: mi_lista[0] devuelve el primer elemento.
- Modificar elementos: mi_lista[1] = 42 cambia el segundo elemento a 42.
- Agregar elementos: mi_lista.append("seis") agrega "seis" al final de la lista.
- Eliminar elementos: mi_lista.remove("cuatro") elimina la primera aparición de "cuatro".
- Longitud de la lista: len(mi_lista) devuelve la cantidad de elementos en la lista.
- Rebanado (slicing): mi_lista[1:4] crea una nueva lista que contiene elementos desde el índice 1 al 3 (no inclusivo).
- Concatenación: otra_lista = [7, 8, 9]; nueva_lista = mi_lista + otra_lista une dos listas en una nueva lista.

## Tuplas en Python

En Python, una tupla es una estructura de datos similar a una lista, pero con una diferencia clave: las tuplas son inmutables. Esto significa que una vez que se crea una tupla, no puedes modificar su contenido. Las tuplas se definen mediante paréntesis () y los elementos se separan por comas. Aquí tienes un ejemplo de una tupla:

```py
mi_tupla = (1, 2, 3, "cuatro", "cinco")
```

### Características clave de las tuplas en Python:

1. **Inmutables**: Una vez que se crea una tupla, no puedes cambiar, agregar o eliminar elementos de ella. Esto las hace adecuadas para datos que no deben modificarse.

1. **Ordenadas**: Al igual que las listas, las tuplas mantienen el orden de los elementos, lo que significa que los elementos se almacenan en un orden específico y se pueden acceder por su posición (índice).

1. **Heterogéneas**: Las tuplas pueden contener elementos de diferentes tipos, como números, cadenas, objetos, u otras tuplas.

1. **Índices basados en cero**: Los elementos en una tupla se numeran desde 0. Puedes acceder a elementos individuales mediante su índice.

### Ejemplos de operaciones comunes en tuplas:

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

### Características clave de los diccionarios en Python:

1. **Asociación** de clave-valor: Los elementos en un diccionario se almacenan como pares clave-valor, donde cada clave es única y está asociada con un valor.

1. **Mutables**: Los diccionarios son estructuras de datos mutables, lo que significa que puedes agregar, modificar o eliminar elementos después de crear el diccionario.

1. **Acceso rápido** a los valores: Puedes acceder a los valores en un diccionario utilizando sus claves en lugar de índices. Por ejemplo, `mi_diccionario["nombre"]` devolverá el valor "Juan".

1. **Claves heterogéneas**: Las claves de un diccionario pueden ser de diferentes tipos, como cadenas, números o tuplas. Sin embargo, las claves deben ser inmutables, lo que significa que no pueden ser listas o diccionarios.

1. **Valores heterogéneos**: Los valores de un diccionario pueden ser de cualquier tipo, incluyendo listas, tuplas, otros diccionarios o incluso funciones.

### Ejemplos de operaciones comunes en diccionarios:

- Acceder a un valor por clave: `mi_diccionario["nombre"]` devuelve "Juan".
- Modificar un valor: `mi_diccionario["edad"]` = 31 actualiza la edad a 31.
- Agregar nuevos pares clave-valor: `mi_diccionario["profesión"]` = "Ingeniero" agrega un nuevo par clave-valor.
- Eliminar un par clave-valor: del `mi_diccionario["ciudad"]` elimina la entrada "ciudad".
- Comprobar si una clave existe: "nombre" in `mi_diccionario` devuelve True si "nombre" es una clave en el diccionario.
- Obtener una lista de claves o valores: claves = `mi_diccionario.keys()` y valores = `mi_diccionario.values()`.

Los diccionarios son una estructura de datos fundamental y versátil en Python, y se utilizan ampliamente para almacenar y recuperar datos con rapidez y facilidad. Son especialmente útiles cuando necesitas asociar datos con etiquetas o nombres descriptivos.

## Conjuntos (Sets)

En Python, un conjunto (set) es una estructura de datos que representa una colección desordenada de elementos únicos. Los conjuntos se utilizan para realizar operaciones de conjunto, como unión, intersección y diferencia, y son ideales para eliminar elementos duplicados de una secuencia. Los conjuntos se definen utilizando llaves {} o la función set(). Aquí tienes un ejemplo de un conjunto:

```py
mi_conjunto = {1, 2, 3, 4, 5}
```

### Características clave de los conjuntos en Python:

- **Elementos únicos**: Los conjuntos no pueden contener elementos duplicados; cada elemento es único en el conjunto.

- **Desordenados**: Los elementos en un conjunto no tienen un orden específico, por lo que no puedes acceder a ellos por índice.

- **Mutables**: Los conjuntos son estructuras de datos mutables, lo que significa que puedes agregar o eliminar elementos después de crear el conjunto.

### Ejemplos de operaciones comunes en conjuntos:

- Agregar elementos: mi_conjunto.add(6) agrega el elemento 6 al conjunto.
- Eliminar elementos: mi_conjunto.remove(3) elimina el elemento 3 del conjunto.
- Unión de conjuntos: union_set = mi_conjunto.union(otro_conjunto) crea un nuevo conjunto que contiene la unión de dos conjuntos.
- Intersección de conjuntos: interseccion_set = mi_conjunto.intersection(otro_conjunto) crea un nuevo conjunto que contiene la intersección de dos conjuntos.
- Diferencia de conjuntos: diferencia_set = mi_conjunto.difference(otro_conjunto) crea un nuevo conjunto que contiene la diferencia entre dos conjuntos.
- Comprobación de membresía: elemento in mi_conjunto devuelve True si el elemento está en el conjunto.
- Longitud del conjunto: _len(mi_conjunto)_ devuelve la cantidad de elementos en el conjunto.

Los conjuntos son particularmente útiles cuando necesitas mantener una colección de elementos únicos y realizar operaciones matemáticas de conjuntos en ellos. También son eficientes para eliminar duplicados de listas u otras secuencias. Sin embargo, ten en cuenta que los elementos de un conjunto deben ser inmutables (como números, cadenas o tuplas) porque los conjuntos mismos son mutables.

## Parametros y argumentos

En Python, los términos "parámetros" y "argumentos" se utilizan en el contexto de funciones para referirse a valores que se pasan a una función. Estos términos tienen significados específicos:

**Parámetros:**

- Los parámetros son nombres de variables que se definen en la declaración de una función y se utilizan para recibir valores o argumentos cuando se llama a la función.

- Los parámetros se colocan entre los paréntesis de la definición de la función y se utilizan para especificar qué valores debe recibir la función cuando se llama.

- Los parámetros actúan como marcadores de posición para los valores que se pasan a la función.

**Ejemplo de definición de función con parámetros:**

```py
def saludar(nombre):
    print(f"Hola, {nombre}!")
```

En este caso, nombre es un parámetro de la función saludar.

**Argumentos:**

- Los argumentos son los valores reales que se pasan a una función cuando se la llama.

- Los argumentos se utilizan para proporcionar valores concretos que deben coincidir con los parámetros definidos en la función.

- Cuando se llama a una función, los argumentos se pasan entre los paréntesis de la llamada y se asignan a los parámetros de la función en el orden en que se pasan.

**Ejemplo de llamada a función con argumentos:**

```py
saludar("Juan")
```

En este caso, "Juan" es un argumento que se pasa a la función saludar, y se asigna al parámetro nombre.

Es importante entender la diferencia entre parámetros y argumentos, ya que los parámetros son simplemente nombres de variables en la definición de la función, mientras que los argumentos son los valores que se pasan a la función cuando se llama.

## Init

`__init__` es un método especial en Python que se utiliza para inicializar objetos de una clase. Es parte de lo que se conoce como el "constructor" de la clase. Cuando se crea una instancia de una clase (es decir, se crea un objeto basado en esa clase), el método `__init__`  se llama automáticamente para realizar cualquier inicialización requerida.

Aquí hay un ejemplo básico para ilustrar cómo se utiliza `__init__` :

```py
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Soy {self.nombre} y tengo {self.edad} años.")
# Crear una instancia u objeto de la clase Persona
persona1 = Persona("Juan", 30)

# Llamar al método presentarse de la instancia persona1
persona1.presentarse()
```
En este ejemplo, `__init__` toma tres parámetros: `self` (que hace referencia a la instancia misma), nombre y edad. Dentro de `__init__`, se definen atributos de la instancia (`self`.nombre y `self`.edad) que se inicializan con los valores pasados al crear una nueva instancia de la clase Persona.

Cuando se crea la instancia persona1 de la clase Persona, se pasan los valores "Juan" y 30 como argumentos. El método `__init__` se ejecuta automáticamente, estableciendo `self`.nombre en "Juan" y `self.edad` en 30 para el objeto persona1.

Este método es comúnmente utilizado para realizar tareas de inicialización, como la asignación de valores predeterminados a las propiedades de un objeto.

## Del

`__del__`, es otro método especial en Python que se utiliza como el "destructor" de una clase. Mientras que `__init__` se encarga de la inicialización, `__del__` se utiliza para realizar las tareas de limpieza o liberación de recursos cuando un objeto ya no es necesario y está a punto de ser destruido o eliminado.

Sin embargo, el uso de `__del__` no es tan común como `__init__`, ya que en Python el recolector de basura (_`garbage collector`_) se encarga de la eliminación automática de objetos cuando ya no se hace referencia a ellos. Aún así, `__del__` se puede utilizar para liberar recursos que no son manejados automáticamente por el recolector de basura, como por ejemplo, cerrar archivos, conexiones a bases de datos, o liberar otros recursos externos.

Aquí hay un ejemplo sencillo que ilustra el uso de `__del__`:

```python
class MiClase:
    def __init__(self):
        print("Se ha creado un objeto")

    def __del__(self):
        print("Se está eliminando un objeto")

# Crear una instancia de la clase MiClase
objeto = MiClase()

# Eliminar la referencia al objeto (esto no garantiza que el método __del__ se ejecute inmediatamente)
del objeto
```

En este ejemplo, al crear una instancia de `MiClase`, se imprime "Se ha creado un objeto". Luego, al eliminar la referencia al objeto mediante del objeto, se llama al método `__del__`, imprimiendo "Se está eliminando un objeto".

Es importante tener en cuenta que la ejecución de `__del__` no está garantizada en un momento específico, ya que depende del funcionamiento del recolector de basura de Python. Por lo tanto, no se debe confiar en `__del__` para la liberación de recursos críticos, y es preferible utilizar otros métodos más seguros para la gestión de recursos, como el uso de context managers (`with statement`) para garantizar la liberación de recursos al finalizar su uso.

## `With`

El `with` statement en Python se utiliza para trabajar con recursos que necesitan ser inicializados o limpiados de manera adecuada, como archivos abiertos, conexiones a bases de datos, sockets de red, entre otros. Este enunciado asegura que los recursos se liberen correctamente una vez que se complete su uso, incluso si ocurren excepciones durante el proceso.

El `with` statement se asegura de que los recursos sean liberados utilizando dos métodos especiales: `__enter__` y `__exit__`. Estos métodos son parte de un protocolo conocido como el "_context manager protocol_".

Aquí hay un ejemplo de cómo se utiliza `with` para trabajar con un archivo:

```python
# Abrir un archivo utilizando `with` statement
with open('archivo.txt', 'r') as archivo:
    contenido = archivo.read()
    # Hacer algo con el contenido del archivo

# Una vez que se sale del bloque `with`, el archivo se cierra automáticamente
# No es necesario llamar a archivo.close() explícitamente
```

En este ejemplo, open('archivo.txt', 'r') abre el archivo en modo lectura. El `with` statement se encarga de llamar a los métodos `__enter__` y `__exit__` implícitos en el contexto del archivo. Dentro del bloque `with`, puedes realizar operaciones con el archivo. Una vez que se sale del bloque `with`, el archivo se cierra automáticamente, independientemente de si ha habido excepciones o no.

Para usar el `with` statement, el objeto con el que estás trabajando debe tener implementados los métodos `__enter__` y `__exit__`. Estos métodos definen lo que se debe hacer al entrar y salir del bloque `with`. Por ejemplo, para crear tu propio context manager, podrías definir una clase con estos métodos para administrar la inicialización y limpieza de recursos de manera controlada.

El `with` statement es una forma más segura y legible de trabajar con recursos que necesitan ser liberados correctamente después de su uso, ya que garantiza que se realicen las operaciones de limpieza, incluso en presencia de excepciones.

## str
`__str__` es un método especial en Python que se utiliza para definir la representación de cadena de un objeto. Cuando se invoca la función `str()` en un objeto, o cuando se utiliza la función `print()` para mostrar el objeto, Python busca la implementación del método `__str__` en la clase de ese objeto. Si se encuentra, `__str__` devuelve la representación de cadena del objeto.

Aquí tienes un ejemplo simple de cómo usar `__str__`:

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

# Crear una instancia de la clase Persona
persona = Persona("Ana", 25)

# Imprimir la representación de cadena del objeto usando print()
print(persona)  # Esto llama a persona.`__str__`()
```

En este caso, la clase Persona tiene un método `__str__` definido. Cuando se llama print(persona), en realidad se está invocando persona.`__str__()` automáticamente para obtener la representación de cadena del objeto persona.

La implementación de `__str__` te permite definir cómo quieres que tu objeto se represente como una cadena. Esto es útil para personalizar la salida al imprimir objetos, lo que puede ser útil para la depuración y la presentación de objetos en un formato legible para los humanos.

