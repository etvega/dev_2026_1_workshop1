class Conversion:

    def celsius_a_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

    def fahrenheit_a_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

    def metros_a_pies(self, metros):
        return metros * 3.28084

    def pies_a_metros(self, pies):
        return pies * 0.3048

    def decimal_a_binario(self, decimal):
        return bin(decimal)[2:]

    def binario_a_decimal(self, binario):
        return int(binario, 2)

    def decimal_a_romano(self, numero):
        valores = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        resultado = ""
        for valor, romano in valores:
            while numero >= valor:
                resultado += romano
                numero -= valor

        return resultado

    def romano_a_decimal(self, romano):
        valores = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }

        total = 0
        anterior = 0

        for letra in reversed(romano):
            valor = valores[letra]
            if valor < anterior:
                total -= valor
            else:
                total += valor
            anterior = valor

        return total

    def texto_a_morse(self, texto):
        morse = {
            "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
            "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
            "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
            "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
            "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
            "Z": "--..",
            "0": "-----", "1": ".----", "2": "..---", "3": "...--",
            "4": "....-", "5": ".....", "6": "-....", "7": "--...",
            "8": "---..", "9": "----."
        }

        resultado = []
        for letra in texto.upper():
            if letra in morse:
                resultado.append(morse[letra])

        return " ".join(resultado)

    def morse_a_texto(self, morse_string):
        # El diccionario debe estar identado dentro de la función
        dic = {
            ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
            "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
            "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
            ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
            "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
            "--..": "Z",
            "-----": "0", ".----": "1", "..---": "2", "...--": "3",
            "....-": "4", ".....": "5", "-....": "6", "--...": "7",
            "---..": "8", "----.": "9"
        }

        resultado = ""
        # Usamos morse_string.split() para separar los puntos y rayas
        for simbolo in morse_string.split():
            if simbolo in dic:
                resultado += dic[simbolo]

        return resultado