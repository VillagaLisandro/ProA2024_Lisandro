class Personaje:
    #atributo de clase
    estado = True #vivo
    
    #constructor / atributo de instancia
    def __init__(self, nombre, altura, velocidad, fuerza):
        self.nombre  = nombre 
        self.altura = altura
        self.velocidad = velocidad
        self.fuerza = fuerza 
        
