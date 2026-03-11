class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """

    def invertir_lista(self, lista):
        resultado = []
        i = len(lista) - 1
        while i >= 0:
            resultado.append(lista[i])
            i -= 1
        return resultado

    def buscar_elemento(self, lista, elemento):
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1

    def eliminar_duplicados(self, lista):
        # Todo este bloque debe tener un nivel de tabulación extra
        resultado = []
        vistos = set()

        for x in lista:
            # Esta clave (tipo, valor) diferencia 1 de True
            clave = (type(x), x)
            if clave not in vistos:
                vistos.add(clave)
                resultado.append(x)
        return resultado

    def merge_ordenado(self, lista1, lista2):
        resultado = []
        i = 0
        j = 0

        while i < len(lista1) and j < len(lista2):
            if lista1[i] <= lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1

        while i < len(lista1):
            resultado.append(lista1[i])
            i += 1

        while j < len(lista2):
            resultado.append(lista2[j])
            j += 1

        return resultado

    def rotar_lista(self, lista, k):
        n = len(lista)
        if n == 0:
            return lista

        k = k % n
        return lista[-k:] + lista[:-k]

    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1
        suma_total = n * (n + 1) // 2
        suma_lista = 0

        for num in lista:
            suma_lista += num

        return suma_total - suma_lista

    def es_subconjunto(self, conjunto1, conjunto2):
        for elemento in conjunto1:
            if elemento not in conjunto2:
                return False
        return True

    def implementar_pila(self):
        pila = []

        def push(x):
            pila.append(x)

        def pop():
            if pila:
                return pila.pop()
            return None

        def peek():
            if pila:
                return pila[-1]
            return None

        def is_empty():
            return len(pila) == 0

        return {
            "push": push,
            "pop": pop,
            "peek": peek,
            "is_empty": is_empty
        }

    def implementar_cola(self):
        cola = []

        def enqueue(x):
            cola.append(x)

        def dequeue():
            if cola:
                return cola.pop(0)
            return None

        def peek():
            if cola:
                return cola[0]
            return None

        def is_empty():
            return len(cola) == 0

        return {
            "enqueue": enqueue,
            "dequeue": dequeue,
            "peek": peek,
            "is_empty": is_empty
        }

    def matriz_transpuesta(self, matriz):
        # Manejo de caso borde: matriz vacía
        if not matriz:
            return []

        filas = len(matriz)
        columnas = len(matriz[0])
        resultado = []

        for j in range(columnas):
            fila = []
            for i in range(filas):
                fila.append(matriz[i][j])
            resultado.append(fila)

        return resultado