EMPTY = "-"
TORRE = "TORRE"
tablero = []

for i in range(8):
    fila = [EMPTY for i in range(8)]
    tablero.append (fila)

tablero[0][0] = TORRE
tablero[0][7] = TORRE
tablero[7][0] = TORRE
tablero[7][7] = TORRE

print(tablero)
habitaciones =[[[False for r in range(20)] for f in range(15)] for t in range(3)]
temps = [[0.0 for h in range (24)] for d in range (31)]
