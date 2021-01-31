  
from Arbol.Instruccion import Instruccion
   
class Print(Instruccion) :
    def __init__(self,cad,linea,columna):
        self.valor = cad
        self.linea = linea
        self.columna = columna

    def ejecutar(self):
        resultado = self.valor.getValorImplicito()
        print('Salida > ', resultado)