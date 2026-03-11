class Matrix:

    def suma_matrices(self, A, B):
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            raise ValueError("Dimensiones incompatibles")

        resultado = []
        for i in range(len(A)):
            fila = []
            for j in range(len(A[0])):
                fila.append(A[i][j] + B[i][j])
            resultado.append(fila)
        return resultado


    def resta_matrices(self, A, B):
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            raise ValueError("Dimensiones incompatibles")

        resultado = []
        for i in range(len(A)):
            fila = []
            for j in range(len(A[0])):
                fila.append(A[i][j] - B[i][j])
            resultado.append(fila)
        return resultado


    def multiplicar_matrices(self, A, B):
        if len(A[0]) != len(B):
            raise ValueError("Dimensiones incompatibles")

        resultado = []
        for i in range(len(A)):
            fila = []
            for j in range(len(B[0])):
                suma = 0
                for k in range(len(B)):
                    suma += A[i][k] * B[k][j]
                fila.append(suma)
            resultado.append(fila)
        return resultado


    def multiplicar_escalar(self, matriz, escalar):
        resultado = []
        for fila in matriz:
            nueva = []
            for elemento in fila:
                nueva.append(elemento * escalar)
            resultado.append(nueva)
        return resultado


    def transpuesta(self, matriz):
        # Corregido: Identación aplicada correctamente
        if not matriz:
            return []
        
        resultado = []
        for j in range(len(matriz[0])):
            fila = []
            for i in range(len(matriz)):
                fila.append(matriz[i][j])
            resultado.append(fila)
        return resultado


    def es_cuadrada(self, matriz):
        # Corregido: Identación y manejo de caso vacío
        if not matriz:
            return False
        return len(matriz) == len(matriz[0])


    def es_simetrica(self, matriz):
        if not self.es_cuadrada(matriz):
            return False

        n = len(matriz)
        for i in range(n):
            for j in range(n):
                if matriz[i][j] != matriz[j][i]:
                    return False
        return True


    def traza(self, matriz):
        if not self.es_cuadrada(matriz):
            raise ValueError("La matriz no es cuadrada")

        suma = 0
        for i in range(len(matriz)):
            suma += matriz[i][i]
        return suma


    def determinante_2x2(self, matriz):
        if len(matriz) != 2 or len(matriz[0]) != 2:
            raise ValueError("La matriz no es 2x2")

        a = matriz[0][0]
        b = matriz[0][1]
        c = matriz[1][0]
        d = matriz[1][1]

        return a*d - b*c


    def determinante_3x3(self, matriz):
        if len(matriz) != 3 or len(matriz[0]) != 3:
            raise ValueError("La matriz no es 3x3")

        a,b,c = matriz[0]
        d,e,f = matriz[1]
        g,h,i = matriz[2]

        return (a*e*i + b*f*g + c*d*h) - (c*e*g + b*d*i + a*f*h)


    def identidad(self, n):
        matriz = []
        for i in range(n):
            fila = []
            for j in range(n):
                if i == j:
                    fila.append(1)
                else:
                    fila.append(0)
            matriz.append(fila)
        return matriz


    def diagonal(self, matriz):
        if not self.es_cuadrada(matriz):
            raise ValueError("La matriz no es cuadrada")

        diag = []
        for i in range(len(matriz)):
            diag.append(matriz[i][i])
        return diag


    def es_diagonal(self, matriz):
        if not self.es_cuadrada(matriz):
            return False

        n = len(matriz)
        for i in range(n):
            for j in range(n):
                if i != j and matriz[i][j] != 0:
                    return False
        return True


    def rotar_90(self, matriz):
        n = len(matriz)
        m = len(matriz[0])

        resultado = []
        for j in range(m):
            fila = []
            for i in range(n-1, -1, -1):
                fila.append(matriz[i][j])
            resultado.append(fila)
        return resultado


    def buscar_en_matriz(self, matriz, valor):
        posiciones = []

        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if matriz[i][j] == valor:
                    posiciones.append((i, j))

        return posiciones