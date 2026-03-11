class Magic:

    def fibonacci(self, n):
        if n < 0: return None
        if n == 0: return 0
        if n == 1: return 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    def secuencia_fibonacci(self, n):
        if n <= 0: return []
        secuencia = [0, 1]
        while len(secuencia) < n:
            secuencia.append(secuencia[-1] + secuencia[-2])
        return secuencia[:n]

    def es_primo(self, n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True

    def generar_primos(self, n):
        return [i for i in range(2, n + 1) if self.es_primo(i)]

    def es_numero_perfecto(self, n):
        if n < 2: return False
        suma = sum(i for i in range(1, n) if n % i == 0)
        return suma == n

    def triangulo_pascal(self, n):
        if n <= 0: return []
        triangulo = [[1]]
        for i in range(1, n):
            fila = [1]
            for j in range(1, i):
                fila.append(triangulo[i-1][j-1] + triangulo[i-1][j])
            fila.append(1)
            triangulo.append(fila)
        return triangulo

    def factorial(self, n):
        if n < 0: return None
        res = 1
        for i in range(1, n + 1): res *= i
        return res

    def mcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def mcm(self, a, b):
        if a == 0 or b == 0: return 0
        return abs(a * b) // self.mcd(a, b)

    def suma_digitos(self, n):
        return sum(int(d) for d in str(abs(n)))

    def es_numero_armstrong(self, n):
        s = str(abs(n))
        potencia = len(s)
        return sum(int(d)**potencia for d in s) == abs(n)

    def es_cuadrado_magico(self, matriz):
        n = len(matriz)
        suma_objetivo = sum(matriz[0])
        # Verificar filas y columnas
        for i in range(n):
            if sum(matriz[i]) != suma_objetivo: return False
            if sum(matriz[j][i] for j in range(n)) != suma_objetivo: return False
        # Verificar diagonales
        if sum(matriz[i][i] for i in range(n)) != suma_objetivo: return False
        if sum(matriz[i][n-1-i] for i in range(n)) != suma_objetivo: return False
        return True