from Arbol.Expresion import Expresion
from Arbol.Tipo import Tipo

class Primitivo(Expresion):
    def __init__(self,valor,linea,columna):
        self.valor = valor     #Object
        self.linea = linea
        self.columna = columna
    
    def getValorImplicito(self):
        return self.valor

    def getTipo(self):
        if(self.valor == True or self.valor == False):
            return Tipo.BOOLEAN
        elif isinstance(self.valor, int):
            return Tipo.INT
        elif isinstance(self.valor, float):
            return Tipo.DOOBLE  
        elif isinstance(self.valor, str):
            return Tipo.STRING  
        else:
            return Tipo.NULL  