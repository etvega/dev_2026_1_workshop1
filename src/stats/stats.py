class Stats:

    def promedio(self, numeros):
        if len(numeros) == 0:
            return 0
        return sum(numeros) / len(numeros)


    def mediana(self, numeros):
        if len(numeros) == 0:
            return 0

        nums = sorted(numeros)
        n = len(nums)

        if n % 2 == 1:
            return float(nums[n // 2])
        else:
            return (nums[n//2 - 1] + nums[n//2]) / 2


    def moda(self, numeros):
        if len(numeros) == 0:
            return None

        frecuencias = {}

        for num in numeros:
            if num in frecuencias:
                frecuencias[num] += 1
            else:
                frecuencias[num] = 1

        max_frecuencia = 0
        moda = numeros[0]

        for num in frecuencias:
            if frecuencias[num] > max_frecuencia:
                max_frecuencia = frecuencias[num]
                moda = num

        return moda


    def desviacion_estandar(self, numeros):
        if len(numeros) == 0:
            return 0

        media = self.promedio(numeros)

        suma = 0
        for n in numeros:
            suma += (n - media) ** 2

        varianza = suma / len(numeros)

        return varianza ** 0.5


    def varianza(self, numeros):
        if len(numeros) == 0:
            return 0

        media = self.promedio(numeros)

        suma = 0
        for n in numeros:
            suma += (n - media) ** 2

        return suma / len(numeros)


    def rango(self, numeros):
        if len(numeros) == 0:
            return 0

        return max(numeros) - min(numeros)