import random

class Games:

    def piedra_papel_tijera(self, j1, j2):
        opciones = ["piedra", "papel", "tijera"]
        j1, j2 = j1.lower(), j2.lower()
        if j1 not in opciones or j2 not in opciones:
            return "invalid"
        if j1 == j2:
            return "empate"
        if (j1 == "piedra" and j2 == "tijera") or (j1 == "papel" and j2 == "piedra") or (j1 == "tijera" and j2 == "papel"):
            return "jugador1"
        return "jugador2"

    def adivinar_numero_pista(self, numero_secreto, intento):
        if intento == numero_secreto:
            return "correcto"
        elif intento > numero_secreto:
            return "muy alto"
        else:
            return "muy bajo"

    def ta_te_ti_ganador(self, tablero):
        # 1. Verificar filas
        for fila in tablero:
            if fila[0] == fila[1] == fila[2] and fila[0] != " ":
                return fila[0]
        # 2. Verificar columnas
        for col in range(3):
            if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] != " ":
                return tablero[0][col]
        # 3. Verificar diagonales
        if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
            return tablero[0][0]
        if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
            return tablero[0][2]
        
        # 4. SOLO SI NO HUBO GANADOR, verificar si hay espacios libres
        for fila in tablero:
            if " " in fila:
                return "continua"
        
        # 5. Si no hay ganador y no hay espacios, es empate
        return "empate"

    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        combinacion = []
        for _ in range(longitud):
            color = random.choice(colores_disponibles)
            combinacion.append(color)
        return combinacion

    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        if not (0 <= desde_fila < 8 and 0 <= desde_col < 8 and 0 <= hasta_fila < 8 and 0 <= hasta_col < 8):
            return False
        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False
        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False
        if desde_fila == hasta_fila:
            paso = 1 if hasta_col > desde_col else -1
            for col in range(desde_col + paso, hasta_col, paso):
                if tablero[desde_fila][col] != " ":
                    return False
        if desde_col == hasta_col:
            paso = 1 if hasta_fila > desde_fila else -1
            for fila in range(desde_fila + paso, hasta_fila, paso):
                if tablero[fila][desde_col] != " ":
                    return False
        return True