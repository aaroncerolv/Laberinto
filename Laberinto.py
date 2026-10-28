class Laberinto:
    def __init__(self, renglon, columna):
        self.renglon = renglon
        self.columna = columna
        self.tablero = []

    def leer_archivo(self):
        with open("entrada7.lab", "r") as laberinto:
            self.renglon = int(laberinto.readline().strip())
            self.columna = int(laberinto.readline().strip())

            for fila in range(self.renglon):
                linea = laberinto.readline().strip()
                valores = linea.split(",")
                numeros = [] 
                for c, valor in enumerate(valores):
                    valor = valor.strip()
                    if valor in ('S', 'E'):   
                        numeros.append(valor)
                    else:
                        numeros.append(int(valor))
                self.tablero.append(numeros)

    def buscar_inicio(self):
        for fila in range(self.renglon):
            for columna in range(self.columna):
                inicio = self.tablero[fila][columna]
                if inicio == 'S':
                    return (fila, columna)

    def recorrer_laberinto(self):
        inicio = self.buscar_inicio()
        pila = []
        pila.append(inicio)

        while len(pila) > 0:
            cord_actual = pila[-1]
            fila, columna = cord_actual
            
            if self.tablero[fila][columna] == 'E':
                return True
                
            if self.tablero[fila][columna] != 'S':
                self.tablero[fila][columna] = 'x'

            movimientos = [(fila-1, columna), (fila+1, columna), (fila, columna-1), (fila, columna+1)]
            mov_validos = []
            for mov in movimientos:
                fila_mov, col_mov = mov
                if 0 <= fila_mov < self.renglon and 0 <= col_mov < self.columna:
                    if self.tablero[fila_mov][col_mov] in (0, 'E'):
                        mov_validos.append(mov)

            if len(mov_validos) > 0:
                pila.append(mov_validos[0])
            else:
                pila.pop()

        return False

if __name__ == "__main__":
    # Creamos el objeto de la clase
    mi_laberinto = Laberinto(0, 0)
    
    # Leemos el archivo
    mi_laberinto.leer_archivo()
    
    # Ejecutamos el laberinto y guardamos el resultado
    encontro_salida = mi_laberinto.recorrer_laberinto()
    
    # Mostramos el resultado en pantalla
    print("¿Se encontró la salida?", encontro_salida)