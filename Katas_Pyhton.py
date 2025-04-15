""" 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias 
de cada letra en la cadena. Los espacios no deben ser considerados: """

def contar_frecuencias(cadena):
    # Creación de un diccionario vacío para almacenar las frecuencias
    frecuencias = {}

    # Recorrido de cada carácter de la cadena
    for char in cadena:
        # Ignorar los espacios
        if char != ' ':
            # Si el carácter ya está en el diccionario, incrementar su frecuencia
            if char in frecuencias:
                frecuencias[char] += 1
            else:
                # Si no está en el diccionario, agregarlo con frecuencia 1
                frecuencias[char] = 1

    return frecuencias

# Ejemplo:
cadena = "hola mundo"
resultado = contar_frecuencias(cadena)
print(resultado)

""" 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map(): """

def obtener_doble(lista):
    # Uso de la función map() para aplicar el doble a cada valor de la lista
    return list(map(lambda x: x * 2, lista))

# Ejemplo:
numeros = [1, 2, 3, 4, 5]
dobles = obtener_doble(numeros)
print(dobles)

""" 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo. """

def encontrar_palabras(lista_palabras, palabra_objetivo):
    # Filtro de las palabras que contienen la palabra objetivo
    return [palabra for palabra in lista_palabras if palabra_objetivo in palabra]

# Ejemplo:
palabras = ["manzana", "banana", "naranja", "mandarina", "pera"]
objetivo = "man"
resultado = encontrar_palabras(palabras, objetivo)
print(resultado)

""" 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map(): """

def calcular_diferencia(lista1, lista2):
    # Uso de map() para restar los valores de las dos listas
    return list(map(lambda x, y: x - y, lista1, lista2))

# Ejemplo:
lista1 = [10, 20, 30, 40, 50]
lista2 = [1, 2, 3, 4, 5]

resultado = calcular_diferencia(lista1, lista2)
print(resultado)

""" 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
una tupla que contenga la media y el estado. """

def evaluar_media(numeros, nota_aprobado=5):
    if not numeros:
        return (0, "sin datos")
    
    media = sum(numeros) / len(numeros)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (media, estado)

# Ejemplo:
notas = [4, 6, 5, 7]
resultado = evaluar_media(notas)
print(resultado)

""" 6. Escribe una función que calcule el factorial de un número de manera recursiva. """

def factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Ejemplo:
print(factorial(5))  # Salida: 120

""" 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map() """

def tuplas_a_strings(lista_tuplas):
    return list(map(lambda t: ' '.join(map(str, t)), lista_tuplas))

# Ejemplo:
tuplas = [(1, 'manzana'), (2, 'banana'), (3, 'cereza')]
resultado = tuplas_a_strings(tuplas)
print(resultado)

""" 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
indicando si la división fue exitosa o no. """

def dividir_numeros():
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        resultado = num1 / num2
    except ValueError:
        print("❌ Error: Debes ingresar valores numéricos.")
    except ZeroDivisionError:
        print("❌ Error: No se puede dividir entre cero.")
    else:
        print(f"✅ División exitosa. El resultado es: {resultado}")
    finally:
        print("Fin del programa.")

# Ejecutar función
dividir_numeros()

""" 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
"Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter() """

def filtrar_mascotas(mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    # Usamos filter con una función lambda para excluir las prohibidas
    return list(filter(lambda m: m not in prohibidas, mascotas))

# Ejemplo:
lista_mascotas = ["Perro", "Gato", "Tigre", "Mapache", "Canario", "Cocodrilo"]
mascotas_permitidas = filtrar_mascotas(lista_mascotas)

print(mascotas_permitidas)

""" 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
excepción personalizada y maneja el error adecuadamente. """

class ListaVaciaError(Exception):
    """Excepción personalizada para listas vacías."""
    def __init__(self, mensaje="La lista está vacía. No se puede calcular el promedio."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def calcular_promedio(lista):
    if not lista:  # Si la lista está vacía
        raise ListaVaciaError  # Excepción personalizada
    return sum(lista) / len(lista)

# Ejemplo:
try:
    numeros = [10, 20, 30, 40, 50]
    promedio = calcular_promedio(numeros)
    print(f"El promedio es: {promedio}")
except ListaVaciaError as e:
    print(e)

""" 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones
adecuadamente. """

def obtener_edad():
    try:
        edad = input("Por favor, introduce tu edad: ")
        edad = int(edad)  # Intentamos convertir la entrada a un número entero

        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120 años.")  # Comprobamos el rango de edad

        print(f"Tu edad es: {edad} años.")

    except ValueError as e:
        print(f"Error: {e}. Por favor, ingresa un valor válido.")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")

# Llamamos a la función
obtener_edad()

""" 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map() """

def longitud_palabras(frase):
    # Separamos la frase en palabras usando el método split()
    palabras = frase.split()
    
    # Usamos map() para aplicar len() a cada palabra
    longitudes = list(map(len, palabras))
    
    return longitudes

# Ejemplo:
frase = "Hola esto es una prueba"
longitudes = longitud_palabras(frase)
print(longitudes)  

""" 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map() """

def convertir_a_tuplas(caracteres):
    # Convertimos el conjunto a una lista y eliminamos duplicados
    caracteres_unicos = set(caracteres)
    
    # Usamos map() para crear una tupla de mayúsculas y minúsculas para cada letra
    tuplas = list(map(lambda c: (c.upper(), c.lower()), caracteres_unicos))
    
    return tuplas

# Ejemplo:
conjunto_caracteres = "aAbBcCdDe"
resultado = convertir_a_tuplas(conjunto_caracteres)
print(resultado)

""" 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
función filter()"""

def palabras_que_comienzan_con(lista_palabras, letra):
    # Usamos filter() para filtrar las palabras que comienzan con la letra especificada
    palabras_filtradas = list(filter(lambda palabra: palabra.lower().startswith(letra.lower()), lista_palabras))
    
    return palabras_filtradas

# Ejemplo:
lista_de_palabras = ["manzana", "banana", "cereza", "mango", "ciruela"]
letra_especifica = "m"
resultado = palabras_que_comienzan_con(lista_de_palabras, letra_especifica)
print(resultado)

""" 15. Crea una función lambda que sume 3 a cada número de una lista dada """

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Usamos map() con una función lambda para sumar 3 a cada número
numeros_incrementados = list(map(lambda x: x + 3, numeros))

# Imprimimos el resultado
print(numeros_incrementados)

""" 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
todas las palabras que sean más largas que n. Usa la función filter() """

def palabras_mas_largas_que_n(cadena, n):
    # Separamos la cadena en palabras usando split()
    palabras = cadena.split()
    
    # Usamos filter() para filtrar las palabras que tienen más de n caracteres
    palabras_filtradas = list(filter(lambda palabra: len(palabra) > n, palabras))
    
    return palabras_filtradas

# Ejemplo:
texto = "La programación en Python es divertida y poderosa"
numero = 5
resultado = palabras_mas_largas_que_n(texto, numero)
print(resultado)

""" 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
corresponde al número quinientos setenta y dos (572). Usa la función reduce() """

from functools import reduce

def lista_a_numero(digitos):
    # Usamos reduce() para combinar los dígitos en un solo número
    numero = reduce(lambda x, y: x * 10 + y, digitos)
    return numero

# Ejemplo:
digitos = [5, 7, 2]
numero = lista_a_numero(digitos)
print(numero)

""" 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a
90. Usa la función filter() """

def estudiantes_con_buena_calificacion(estudiantes):
    # Usamos filter() para filtrar los estudiantes con calificación mayor o igual a 90
    estudiantes_filtrados = list(filter(lambda estudiante: estudiante['calificacion'] >= 90, estudiantes))
    
    return estudiantes_filtrados

# Lista de estudiantes con nombre, edad y calificación
estudiantes = [
    {'nombre': 'Ana', 'edad': 20, 'calificacion': 95},
    {'nombre': 'Luis', 'edad': 22, 'calificacion': 88},
    {'nombre': 'Carlos', 'edad': 21, 'calificacion': 90},
    {'nombre': 'Marta', 'edad': 19, 'calificacion': 85},
    {'nombre': 'Julia', 'edad': 23, 'calificacion': 92}
]

# Llamamos a la función y obtenemos los estudiantes con buena calificación
estudiantes_buena_calificacion = estudiantes_con_buena_calificacion(estudiantes)

# Mostramos los resultados
print(estudiantes_buena_calificacion)

""" 19. Crea una función lambda que filtre los números impares de una lista dada. """

def filtrar_impares(lista):
    # Usamos filter() con una función lambda para filtrar los números impares
    impares = list(filter(lambda x: x % 2 != 0, lista))
    return impares

# Ejemplo:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
resultado = filtrar_impares(numeros)
print(resultado)

""" 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
filter() """

def filtrar_enteros(lista):
    # Usamos filter() con una función lambda para filtrar solo los enteros
    enteros = list(filter(lambda x: isinstance(x, int), lista))
    return enteros

# Ejemplo:
lista_mixta = [1, 'a', 2, 'b', 3, 'c', 4]
resultado = filtrar_enteros(lista_mixta)
print(resultado)

""" 21. Crea una función que calcule el cubo de un número dado mediante una función lambda """

def calcular_cubo(numero):
    # Usamos una función lambda para calcular el cubo del número
    cubo = (lambda x: x ** 3)(numero)
    return cubo

# Ejemplo:
numero = 3
resultado = calcular_cubo(numero)
print(resultado)

""" 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce() """

from functools import reduce

def producto_total(lista):
    # Usamos reduce() para calcular el producto total de la lista
    producto = reduce(lambda x, y: x * y, lista)
    return producto

# Ejemplo:
numeros = [1, 2, 3, 4, 5]
resultado = producto_total(numeros)
print(resultado)

""" 23. Concatena una lista de palabras.Usa la función reduce() """

from functools import reduce

def concatenar_palabras(lista):
    # Usamos reduce() para concatenar todas las palabras de la lista
    concatenado = reduce(lambda x, y: x + y, lista)
    return concatenado

# Ejemplo:
palabras = ["Hola", " ", "mundo", " ", "desde", " ", "Python"]
resultado = concatenar_palabras(palabras)
print(resultado)

""" 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() """

from functools import reduce

def diferencia_total(lista):
    # Usamos reduce() para calcular la diferencia total de los valores de la lista
    diferencia = reduce(lambda x, y: x - y, lista)
    return diferencia

# Ejemplo:
numeros = [10, 3, 2, 1]
resultado = diferencia_total(numeros)
print(resultado)

""" 25. Crea una función que cuente el número de caracteres en una cadena de texto dada """

def contar_caracteres(cadena):
    # Usamos la función len() para contar los caracteres en la cadena
    return len(cadena)

# Ejemplo:
texto = "Hola, ¿cómo estás?"
resultado = contar_caracteres(texto)
print(resultado)

""" 26. Crea una función lambda que calcule el resto de la división entre dos números dados """

# Función lambda para calcular el resto de la división entre dos números
resto_division = lambda x, y: x % y

# Ejemplo:
numero1 = 10
numero2 = 3
resultado = resto_division(numero1, numero2)
print(resultado)

""" 27. Crea una función que calcule el promedio de una lista de números """

def calcular_promedio(lista):
    # Calculamos la suma de los números en la lista y luego la dividimos por la cantidad de elementos
    if len(lista) == 0:
        return 0  # Retorna 0 si la lista está vacía para evitar división por cero
    return sum(lista) / len(lista)

# Ejemplo:
numeros = [10, 20, 30, 40, 50]
resultado = calcular_promedio(numeros)
print(resultado)

""" 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada """

def primer_elemento_duplicado(lista):
    # Usamos un conjunto para rastrear los elementos que ya hemos visto
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento  # Retorna el primer elemento duplicado
        vistos.add(elemento)
    return None  # Si no se encuentra duplicados, retornamos None

# Ejemplo:
numeros = [1, 2, 3, 4, 5, 3, 6, 7]
resultado = primer_elemento_duplicado(numeros)
print(resultado)

""" 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
carácter '#', excepto los últimos cuatro """

def enmascarar_cadena(variable):
    # Convertimos la variable a cadena de texto
    cadena = str(variable)
    
    # Verificamos si la longitud de la cadena es mayor que 4
    if len(cadena) > 4:
        # Enmascaramos todos los caracteres, excepto los últimos cuatro
        return '#' * (len(cadena) - 4) + cadena[-4:]
    else:
        # Si la cadena tiene 4 caracteres o menos, no enmascaramos
        return cadena

# Ejemplo:
numero = 123456789
resultado = enmascarar_cadena(numero)

""" 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
pero en diferente orden """

def son_anagramas(palabra1, palabra2):
    # Comparamos las palabras ordenadas. Si son iguales, son anagramas.
    return sorted(palabra1) == sorted(palabra2)

# Ejemplo:
palabra1 = "amor"
palabra2 = "roma"
resultado = son_anagramas(palabra1, palabra2)
print(resultado)

""" 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
lanza una excepción """

class NombreNoEncontrado(Exception):
    """Excepción personalizada para cuando el nombre no es encontrado en la lista."""
    pass

def buscar_nombre():
    # Solicitar la lista de nombres
    nombres = input("Ingresa una lista de nombres, separados por comas: ").split(",")
    
    # Eliminar espacios en blanco alrededor de los nombres
    nombres = [nombre.strip() for nombre in nombres]
    
    # Solicitar el nombre a buscar
    nombre_a_buscar = input("Ingresa el nombre que deseas buscar: ").strip()
    
    # Buscar el nombre en la lista
    if nombre_a_buscar in nombres:
        print(f"El nombre '{nombre_a_buscar}' fue encontrado en la lista.")
    else:
        raise NombreNoEncontrado(f"El nombre '{nombre_a_buscar}' no fue encontrado en la lista.")

# Ejemplo:
try:
    buscar_nombre()
except NombreNoEncontrado as e:
    print(e)

""" 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
no trabaja aquí """

def buscar_puesto(nombre_completo, lista_empleados):
    # Buscar el nombre en la lista de empleados
    for empleado in lista_empleados:
        if empleado['nombre'] == nombre_completo:
            return f"El empleado {nombre_completo} trabaja como {empleado['puesto']}."
    
    return f"La persona {nombre_completo} no trabaja aquí."

# Ejemplo de lista de empleados
empleados = [
    {'nombre': 'Juan Pérez', 'puesto': 'Gerente de Ventas'},
    {'nombre': 'María López', 'puesto': 'Desarrolladora'},
    {'nombre': 'Ana Gómez', 'puesto': 'Contadora'},
]

# Ejemplo de uso
nombre_a_buscar = 'María López'
resultado = buscar_puesto(nombre_a_buscar, empleados)
print(resultado)  # Salida: El empleado María López trabaja como Desarrolladora.

# Si el empleado no se encuentra en la lista
nombre_a_buscar = 'Carlos Sánchez'
resultado = buscar_puesto(nombre_a_buscar, empleados)
print(resultado)

""" 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas """

# Función lambda que suma los elementos correspondientes de dos listas
sumar_elementos = lambda lista1, lista2: [x + y for x, y in zip(lista1, lista2)]

# Ejemplo:
lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]
resultado = sumar_elementos(lista1, lista2)
print(resultado)

""" 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
manipular la estructura del árbol """

# Código a seguir:
# 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
# 2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
# 3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
# 4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
# 5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
# 6.  Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.

class Arbol:
    def __init__(self):
        # Inicializamos el tronco con una longitud de 1 y las ramas como una lista vacía.
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        # Aumentamos la longitud del tronco en 1.
        self.tronco += 1

    def nueva_rama(self):
        # Añadimos una nueva rama de longitud 1 a la lista de ramas.
        self.ramas.append(1)

    def crecer_ramas(self):
        # Aumentamos en 1 la longitud de todas las ramas existentes.
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        # Eliminamos una rama en la posición especificada si es válida.
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print("Posición inválida. No se puede quitar la rama.")

    def info_arbol(self):
        # Retorna la información sobre la longitud del tronco, el número de ramas y las longitudes de las ramas.
        return f"Tronco: {self.tronco}, Número de ramas: {len(self.ramas)}, Longitudes de las ramas: {self.ramas}"

# Caso de uso

# 1. Crear un árbol.
arbol = Arbol()

# 2. Hacer crecer el tronco del árbol una unidad.
arbol.crecer_tronco()

# 3. Añadir una nueva rama al árbol.
arbol.nueva_rama()

# 4. Hacer crecer todas las ramas del árbol una unidad.
arbol.crecer_ramas()

# 5. Añadir dos nuevas ramas al árbol.
arbol.nueva_rama()
arbol.nueva_rama()

# 6. Retirar la rama situada en la posición 2.
arbol.quitar_rama(2)

# 7. Obtener información sobre el árbol.
informacion = arbol.info_arbol()
print(informacion)

""" 36.  Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
agregar dinero al saldo. """

# Código a seguir:
# 1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
# 2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
# 3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
# 4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.

class UsuarioBanco:
    def __init__(self, nombre, saldo, tiene_cuenta_corriente):
        # Inicializamos el usuario con su nombre, saldo y si tiene cuenta corriente.
        self.nombre = nombre
        self.saldo = saldo
        self.tiene_cuenta_corriente = tiene_cuenta_corriente

    def retirar_dinero(self, cantidad):
        # Verificamos si el saldo es suficiente para retirar el dinero.
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            raise ValueError(f"No tienes suficiente saldo para retirar {cantidad} unidades.")
    
    def transferir_dinero(self, usuario_origen, cantidad):
        # Verificamos si el usuario origen tiene suficiente saldo.
        if cantidad <= usuario_origen.saldo:
            usuario_origen.saldo -= cantidad
            self.saldo += cantidad
        else:
            raise ValueError(f"El usuario {usuario_origen.nombre} no tiene suficiente saldo para transferir {cantidad} unidades.")
    
    def agregar_dinero(self, cantidad):
        # Añadimos la cantidad al saldo del usuario.
        self.saldo += cantidad

    def info_usuario(self):
        # Retorna la información del usuario (nombre, saldo y si tiene cuenta corriente).
        return f"Usuario: {self.nombre}, Saldo: {self.saldo}, Cuenta Corriente: {'Sí' if self.tiene_cuenta_corriente else 'No'}"


# Caso de uso

# 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

# 2. Agregar 20 unidades de saldo de "Bob".
bob.agregar_dinero(20)

# 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
bob.transferir_dinero(alicia, 80)

# 4. Retirar 50 unidades de saldo a "Alicia".
alicia.retirar_dinero(50)

# Mostrar la información actual de ambos usuarios
print(alicia.info_usuario())  # Salida esperada: Usuario: Alicia, Saldo: 130, Cuenta Corriente: Sí
print(bob.info_usuario())  # Salida esperada: Usuario: Bob, Saldo: 40, Cuenta Corriente: Sí

""" 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,
reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
de la función procesar_texto """

# Código a seguir:
# 1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
# 2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene que devolver el texto con el remplazo de palabras.
# 3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
# 4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.

from collections import Counter

def contar_palabras(texto):
    # Contamos las palabras en el texto y devolvemos un diccionario con el conteo de cada palabra
    palabras = texto.split()
    return dict(Counter(palabras))

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    # Reemplazamos todas las ocurrencias de 'palabra_original' por 'palabra_nueva' en el texto
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra):
    # Eliminamos todas las ocurrencias de la 'palabra' en el texto
    palabras = texto.split()
    palabras_filtradas = [p for p in palabras if p != palabra]
    return " ".join(palabras_filtradas)

def procesar_texto(texto, opcion, *args):
    # Procesamos el texto según la opción indicada
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("Se deben proporcionar la palabra original y la nueva palabra para reemplazar.")
        palabra_original, palabra_nueva = args
        return reemplazar_palabras(texto, palabra_original, palabra_nueva)
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("Se debe proporcionar la palabra a eliminar.")
        palabra = args[0]
        return eliminar_palabra(texto, palabra)
    else:
        raise ValueError("Opción no válida. Debes elegir entre 'contar', 'reemplazar' o 'eliminar'.")

# Caso de uso
texto = "la casa es grande y la casa es bonita"

# Contar palabras
resultado_contar = procesar_texto(texto, "contar")
print("Conteo de palabras:", resultado_contar)

# Reemplazar palabra
resultado_reemplazar = procesar_texto(texto, "reemplazar", "casa", "hogar")
print("Texto después de reemplazar:", resultado_reemplazar)

# Eliminar palabra
resultado_eliminar = procesar_texto(texto, "eliminar", "la")
print("Texto después de eliminar:", resultado_eliminar)


""" 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario """

def determinar_momento_del_dia(hora):
    # Verificamos en qué parte del día se encuentra según la hora proporcionada
    if 0 <= hora < 6:
        return "Es de noche."
    elif 6 <= hora < 12:
        return "Es de día."
    elif 12 <= hora < 20:
        return "Es de tarde."
    elif 20 <= hora < 24:
        return "Es de noche."
    else:
        return "Hora inválida."

# Solicitar la hora al usuario
try:
    hora = int(input("Ingresa la hora (0-23): "))
    # Llamar a la función y mostrar el resultado
    resultado = determinar_momento_del_dia(hora)
    print(resultado)
except ValueError:
    print("Por favor, ingresa un número válido.")

""" 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
Las reglas de calificación son: """
# 0 - 69 insuficiente
# 70 - 79 bien
# 80 - 89 muy bien
# 90 - 100 excelente

def calificacion_texto(calificacion):
    # Determinamos la calificación en texto según la calificación numérica
    if 0 <= calificacion <= 69:
        return "Insuficiente"
    elif 70 <= calificacion <= 79:
        return "Bien"
    elif 80 <= calificacion <= 89:
        return "Muy bien"
    elif 90 <= calificacion <= 100:
        return "Excelente"
    else:
        return "Calificación fuera de rango"

# Solicitar la calificación al usuario
try:
    calificacion = float(input("Ingresa la calificación del alumno (0-100): "))
    
    # Llamar a la función para obtener la calificación en texto
    resultado = calificacion_texto(calificacion)
    print(f"La calificación en texto es: {resultado}")
except ValueError:
    print("Por favor, ingresa una calificación numérica válida.")

""" 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o
"triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura) """

import math

def calcular_area(figura, datos):
    # Determinamos el área según la figura proporcionada
    if figura == "rectangulo":
        if len(datos) == 2:  # Se espera una tupla con base y altura
            base, altura = datos
            return base * altura
        else:
            raise ValueError("Para un rectángulo se necesitan 2 datos: base y altura.")
    
    elif figura == "circulo":
        if len(datos) == 1:  # Se espera una tupla con el radio
            radio, = datos
            return math.pi * radio ** 2
        else:
            raise ValueError("Para un círculo se necesita 1 dato: el radio.")
    
    elif figura == "triangulo":
        if len(datos) == 2:  # Se espera una tupla con base y altura
            base, altura = datos
            return 0.5 * base * altura
        else:
            raise ValueError("Para un triángulo se necesitan 2 datos: base y altura.")
    
    else:
        raise ValueError("Figura no válida. Las opciones son: 'rectangulo', 'circulo' o 'triangulo'.")

# Ejemplo de uso

# Rectángulo: base=5, altura=10
print("Área del rectángulo:", calcular_area("rectangulo", (5, 10)))

# Círculo: radio=7
print("Área del círculo:", calcular_area("circulo", (7,)))

# Triángulo: base=6, altura=8
print("Área del triángulo:", calcular_area("triangulo", (6, 8)))

""" 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo
siguiente: """

# 1. Solicita al usuario que ingrese el precio original de un artículo.
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
# 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€.
# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
# 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.

def calcular_precio_final():
    # Solicitar el precio original del artículo
    try:
        precio_original = float(input("Ingresa el precio original del artículo: "))
    except ValueError:
        print("Por favor, ingresa un valor numérico válido.")
        return

    # Preguntar si tiene un cupón de descuento
    tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").lower()

    if tiene_cupon == "sí":
        # Solicitar el valor del cupón de descuento
        try:
            descuento = float(input("Ingresa el valor del cupón de descuento (€): "))
        except ValueError:
            print("Por favor, ingresa un valor numérico válido para el descuento.")
            return
        
        # Verificar si el cupón es válido (mayor que 0)
        if descuento > 0:
            precio_final = precio_original - descuento
            print(f"Se ha aplicado un descuento de {descuento}€.")
        else:
            print("El valor del cupón no es válido (debe ser mayor que 0).")
            precio_final = precio_original
    else:
        print("No se ha aplicado ningún descuento.")
        precio_final = precio_original

    # Mostrar el precio final
    print(f"El precio final de la compra es: {precio_final}€.")

# Llamar a la función para ejecutar el programa
calcular_precio_final()