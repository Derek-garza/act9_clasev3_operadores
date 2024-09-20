print("Act9")
print("Derek Garza 1196 nueva mat:")

    #zona de class
class operador1196:
        
    # zona de funciones
    def suma1196(self,D,G):
        s1196=D+G
        print(f"la suma de {D} + {G} = {s1196}")
    def resta1196(self,D,G):
            r1196= D-G
            print(f"la resta de {D} - {G} = {r1196}")
    def multi1196(self,D,G):
            m1196= D*G
            print(f"la multiplicacion de {D} * {G} = {m1196}")
    def div1196(self,D,G):
            d1196= D/G
            print(f"la division de {D} / {G} = {d1196}")
    def modulo1196(self,D,G):
            mo1196= D%G
            print(f"la modulo de {D} % {G} = {mo1196}")
    def exponente1196(self,D,G):
            e1196= D**G
            print(f"la exponente de {D} ** {G} = {e1196}")
    def coeficiente1196(self,D,G):
            c1196= D//G
            print(f"la coeficiente de {D} // {G} = {c1196}")
    # ZONA DE CREADCION DE OBJETO
operagarza=operador1196()

    
    #zona de uso de objeto
print("Funcion suma")
operagarza.suma1196(5,5)
print("Funcion resta")
operagarza.resta1196(5,2)
print("Funcion multiplicacion")
operagarza.multi1196(5,5)
print("Funcion divison")
operagarza.div1196(10,2)
print("Funcion modulo")
operagarza.modulo1196(5,10)
print("Funcion exponente")
operagarza.exponente1196(2,2)
print("Funcion coeficiente")
operagarza.coeficiente1196(10,10)