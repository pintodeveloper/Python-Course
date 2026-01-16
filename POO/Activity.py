class Vehiculo():
    def __init__(self,color,ruedas,ancho,alto,marchas):
        self.color = color
        self.ruedas = ruedas
        self.marchas = marchas
        self.ancho = ancho
        self.alto = alto
        self.acelerando = False
        self.frenando = False
        self.girarando = False
    
    def Arrancar(self):
        self.acelerando = True
    
    def frenar(self):
        self.frenando = True
    
    def girar(self):
        self.girarando = True

class Coche(Vehiculo):
    def __init__(self,color,ruedas,ancho,alto,marchas,cilindrada,asientos,aireAcondicionado):
        
        super().__init__(color,ruedas,ancho,alto,marchas)
        self.asientos = asientos
        self.aireAcondicionado = aireAcondicionado
        self.cilindrada = cilindrada

    def Arrancar(self):
        self.arrancar = True
    

    
    def irAtras(self):
        self.marchaAtras = True
     

class Furgoneta(Coche):
    def __init__(self, color, ruedas, ancho, alto, marchas, cilindrada, asientos, aireAcondicionado,carga):
        super().__init__(color, ruedas, ancho, alto, marchas, cilindrada, asientos, aireAcondicionado)
        self.carga = carga
       
    def cargar(self):
        self.cargando = True

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, ancho, alto,marchas):
        super().__init__(color, ruedas, ancho, alto,marchas)
    
    
    
    def saltar(self):
        self.saltando = True
        
    def derrapar(self):
        self.derrapando = True
        
        
class Moto(Coche,Bicicleta):
    def __init__(self, color, ruedas, ancho, alto, marchas, cilindrada, asientos):
        super().__init__(color, ruedas, ancho, alto, marchas, cilindrada, asientos, aireAcondicionado=False)
        
        
        
moto = Moto("Verda","si",34,34,True,1000,2)

print(moto.derrapar())