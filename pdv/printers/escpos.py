
import serial

class Impressora:

    def __init__(self, porta="COM3", baud=9600):
        self.porta = porta
        self.baud = baud

    def imprimir(self, texto):
        try:
            s = serial.Serial(self.porta, self.baud, timeout=1)
            s.write(texto.encode('latin-1'))
            s.write(b"\n\n\x1D\x56\x00")  # Corte parcial
            s.close()
        except Exception as e:
            print("Erro ao imprimir:", e)
