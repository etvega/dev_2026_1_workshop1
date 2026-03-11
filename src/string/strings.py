class Strings:

    def es_palindromo(self, texto):
        texto = texto.lower().replace(" ", "")
        invertido = self.invertir_cadena(texto)
        return texto == invertido

    def invertir_cadena(self, texto):
        resultado = ""
        for letra in texto:
            resultado = letra + resultado
        return resultado

    def contar_vocales(self, texto):
        vocales = "aeiouAEIOU"
        contador = 0
        for letra in texto:
            if letra in vocales:
                contador += 1
        return contador

    def contar_consonantes(self, texto):
        vocales = "aeiouAEIOU"
        count = 0
        for c in texto:
            # Corregido: solo contar si es una letra y no es vocal
            if c.isalpha() and c not in vocales:
                count += 1
        return count

    def es_anagrama(self, texto1, texto2):
        t1 = sorted(texto1.replace(" ", "").lower())
        t2 = sorted(texto2.replace(" ", "").lower())
        return t1 == t2

    def contar_palabras(self, texto):
        palabras = texto.split()
        return len(palabras)

    def palabras_mayus(self, texto):
        resultado = ""
        nueva = True
        for c in texto:
            if c == " ":
                resultado += c
                nueva = True
            else:
                if nueva:
                    resultado += c.upper()
                    nueva = False
                else:
                    resultado += c
        return resultado

    def eliminar_espacios_duplicados(self, texto):
        resultado = ""
        anterior = ""
        for c in texto:
            if not (c == " " and anterior == " "):
                resultado += c
            anterior = c
        return resultado

    def es_numero_entero(self, texto):
        if texto == "":
            return False
        inicio = 0
        if texto[0] == "-" or texto[0] == "+":
            if len(texto) == 1:
                return False
            inicio = 1
        for i in range(inicio, len(texto)):
            if texto[i] < '0' or texto[i] > '9':
                return False
        return True

    def cifrar_cesar(self, texto, desplazamiento):
        resultado = ""
        for letra in texto:
            if letra.isalpha():
                base = ord('A') if letra.isupper() else ord('a')
                nueva = chr((ord(letra) - base + desplazamiento) % 26 + base)
                resultado += nueva
            else:
                resultado += letra
        return resultado

    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)

    def encontrar_subcadena(self, texto, sub):
        if sub == "":
            return []
        posiciones = []
        for i in range(len(texto) - len(sub) + 1):
            match = True
            for j in range(len(sub)):
                if texto[i + j] != sub[j]:
                    match = False
                    break
            if match:
                posiciones.append(i)
        return posiciones