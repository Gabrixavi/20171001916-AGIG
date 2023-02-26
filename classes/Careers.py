#Creamos la clase carrera

class Careers:
    
    def __init__(self):
        self.carreras = {}
        
    def ingresarCarrera(self,carrera):
        self.carreras.update({carrera:1})

    def actualizarCarrera(self,carrera,val):
        self.carreras.update({carrera:val})

    def getCarreras(self):
        return self.carreras
        
    def verificarCarrera(self, carrera):
        if (carrera in self.carreras):
            curvalue = self.carreras[carrera] + 1
            self.actualizarCarrera(carrera, curvalue)
            return True
        else:
            return False
        


