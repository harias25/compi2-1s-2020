import gramatica as g

f = open ('entrada.txt','r')
texto = f.read()
f.close()

instrucciones = g.parse(texto)

for ins in instrucciones:
    ins.ejecutar()