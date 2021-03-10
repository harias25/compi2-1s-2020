from enum import Enum
from Arbol.Expresion import Expresion
from Arbol.Tipo import Tipo

class TIPO_OPERACION(Enum) :
    SUMA = 1
    RESTA= 2
    MULTIPLICACION= 3
    DIVISION= 4
    MODULO= 5
    POTENCIA= 6
    MENOS_UNARIO= 7
    PRIMITIVO= 8

class Operacion(Expresion):
    def __init__(self):
        self.tipo           = None     #Tipo de Operacion
        self.ternario       = None     #Expresion Ternaria
        self.operadorIzq    = None     #Expresion
        self.operadorDer    = None     #Expresion
        self.valor          = None     #Object
        self.linea          = 0
        self.columna        = 0

    def Primitivo(self,valor):
            self.tipo = TIPO_OPERACION.PRIMITIVO
            self.valor = valor

    def OperacionUnaria(self,exp,linea,columna):
        self.tipo = TIPO_OPERACION.MENOS_UNARIO
        self.operadorIzq = exp
        self.linea = linea
        self.columna = columna

    def Operacion(self,izq,der,operacion,linea,columna):
        self.tipo = operacion
        self.operadorIzq = izq
        self.operadorDer = der
        self.linea = linea
        self.columna = columna 

    def getValorImplicito(self):
        #PRIMITIVOS
        if(self.tipo == TIPO_OPERACION.PRIMITIVO):
            return self.valor.getValorImplicito()

        #UNARIA
        elif(self.tipo == TIPO_OPERACION.MENOS_UNARIO):
            valor1 = self.operadorIzq.getValorImplicito()

            #OPERACION DE ENTEROS
            if isinstance(valor1, int):
                return int(valor1) * -1 
            elif isinstance(valor1, float):     # FLOAT
                return round(float(float(valor1) * -1),2)
            else:
                #ERROR DE TIPOS DE DATOS PERMITIDOS PARA LA OPERACION
                print("SEMANTICO","Error semantico, Error en tipo de dato permitido para un UNARIO",self.linea,self.columna)
                return None
                
        #SUMA
        elif(self.tipo == TIPO_OPERACION.SUMA):
            valor1 = self.operadorIzq.getValorImplicito()
            valor2 = self.operadorDer.getValorImplicito()

            #OPERACION DE ENTEROS
            if isinstance(valor1, int) and isinstance(valor2, int):
                return int(valor1) + int(valor2)
            elif isinstance(valor1, int) and isinstance(valor2, float):     # ENTERO - FLOAT
                return round(float(float(valor1) + float(valor2)),2)
            elif isinstance(valor1, float) and isinstance(valor2, int):     # FLOAT - ENTERO
                return round(float(float(valor1) + float(valor2)),2)
            elif isinstance(valor1, float) and isinstance(valor2, float):   # FLOAT - FLOAT
                return round(float(float(valor1) + float(valor2)),2)
            else:
                #ERROR DE TIPOS DE DATOS PERMITIDOS PARA LA OPERACION
                print("SEMANTICO","Error semantico, Error en tipos de datos permitidos para una SUMA",self.linea,self.columna)
                return None
        
        #RESTA
        elif(self.tipo == TIPO_OPERACION.RESTA):
            valor1 = self.operadorIzq.getValorImplicito()
            valor2 = self.operadorDer.getValorImplicito()
            #OPERACION DE ENTEROS
            if isinstance(valor1, int) and isinstance(valor2, int):
                return int(valor1) - int(valor2)
            elif isinstance(valor1, int) and isinstance(valor2, float):     # ENTERO - FLOAT
                return round(float(float(valor1) - float(valor2)),2)
            elif isinstance(valor1, float) and isinstance(valor2, int):     # FLOAT - ENTERO
                return round(float(float(valor1) - float(valor2)),2)
            elif isinstance(valor1, float) and isinstance(valor2, float):   # FLOAT - FLOAT
                return round(float(float(valor1) - float(valor2)),2)
            else:
                #ERROR DE TIPOS DE DATOS PERMITIDOS PARA LA OPERACION
                print("SEMANTICO","Error semantico, Error en tipos de datos permitidos para una RESTA",self.linea,self.columna)
                return None

        #MULTIPLICACIÓN
        elif(self.tipo == TIPO_OPERACION.MULTIPLICACION):
            valor1 = self.operadorIzq.getValorImplicito()
            valor2 = self.operadorDer.getValorImplicito()
            #OPERACION DE ENTEROS
            if isinstance(valor1, int) and isinstance(valor2, int):
                return int(valor1) * int(valor2)
            elif isinstance(valor1, int) and isinstance(valor2, float):     # ENTERO - FLOAT
                return round(float(float(valor1) * float(valor2)),2)
            elif isinstance(valor1, float) and isinstance(valor2, int):     # FLOAT - ENTERO
                return round(float(float(valor1) * float(valor2)),2)
            elif isinstance(valor1, float) and isinstance(valor2, float):   # FLOAT - FLOAT
                return round(float(float(valor1) * float(valor2)),2)
            else:
                #ERROR DE TIPOS DE DATOS PERMITIDOS PARA LA OPERACION
                print("SEMANTICO","Error semantico, Error en tipos de datos permitidos para una MULTIPLICACION",self.linea,self.columna)
                return None
        
        #DIVISION
        elif(self.tipo == TIPO_OPERACION.DIVISION):
            valor1 = self.operadorIzq.getValorImplicito()
            valor2 = self.operadorDer.getValorImplicito()

            if(isinstance(valor2, int) or  isinstance(valor2, float)):
                temp = int(valor2)
                if(temp == 0):
                    print("SEMANTICO","Error semantico, No es posible una división sobre CERO!",self.linea,self.columna)
                    return None

            #OPERACION DE ENTEROS
            if isinstance(valor1, int) and isinstance(valor2, int):
                return int(valor1) / int(valor2)
            elif isinstance(valor1, int) and isinstance(valor2, float):     # ENTERO - FLOAT
                return round(float(float(valor1) / float(valor2)),2)
            elif isinstance(valor1, float) and isinstance(valor2, int):     # FLOAT - ENTERO
                return round(float(float(valor1) / float(valor2)),2)
            elif isinstance(valor1, float) and isinstance(valor2, float):   # FLOAT - FLOAT
                return round(float(float(valor1) / float(valor2)),2)
            else:
                #ERROR DE TIPOS DE DATOS PERMITIDOS PARA LA OPERACION
                print("SEMANTICO","Error semantico, Error en tipos de datos permitidos para una DIVISION",self.linea,self.columna)
                return None

        #MODULO
        elif(self.tipo == TIPO_OPERACION.MODULO):
            valor1 = self.operadorIzq.getValorImplicito()
            valor2 = self.operadorDer.getValorImplicito()

            if(isinstance(valor2, int) or  isinstance(valor2, float)):
                temp = int(valor2)
                if(temp == 0):
                    print("SEMANTICO","Error semantico, No es posible una modulo sobre CERO!",self.linea,self.columna)
                    return None

            #OPERACION DE ENTEROS
            if isinstance(valor1, int) and isinstance(valor2, int):
                return int(valor1) % int(valor2)
            elif isinstance(valor1, int) and isinstance(valor2, float):     # ENTERO - FLOAT
                return round(float(float(valor1) % float(valor2)),2)
            elif isinstance(valor1, float) and isinstance(valor2, int):     # FLOAT - ENTERO
                return round(float(float(valor1) % float(valor2)),2)
            elif isinstance(valor1, float) and isinstance(valor2, float):   # FLOAT - FLOAT
                return round(float(float(valor1) % float(valor2)),2)
            else:
                #ERROR DE TIPOS DE DATOS PERMITIDOS PARA LA OPERACION
                print("SEMANTICO","Error semantico, Error en tipos de datos permitidos para una MODULO",self.linea,self.columna)
                return None

        #UNARIA
        elif(self.tipo == TIPO_OPERACION.MENOS_UNARIO):
            valor1 = self.operadorIzq.getValorImplicito()
            if(isinstance(valor1,str)): valor1 = self.obtenerValorNumerico(valor1)

            #OPERACION DE ENTEROS
            if isinstance(valor1, int):
                return int(valor1) * -1 
            elif isinstance(valor1, float):     # FLOAT
                return round(float(float(valor1) * -1),2)
            else:
                #ERROR DE TIPOS DE DATOS PERMITIDOS PARA LA OPERACION
                print("SEMANTICO","Error semantico, Error en tipo de dato permitido para un UNARIO",self.linea,self.columna)
                return None

    def getTipo(self):
        value = self.getValorImplicito()
        if(value == True or value == False):
            return Tipo.BOOLEAN
        elif isinstance(value, str):
            return Tipo.STRING
        elif isinstance(value, int):
            return Tipo.INT
        elif isinstance(value, float):
            return Tipo.DOOBLE
        else:
            return Tipo.NULL

    