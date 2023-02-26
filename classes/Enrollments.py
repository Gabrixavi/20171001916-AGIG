#Creamos la clase enrolamientos

class Enrollments:
    def __init__(self):
        self.estudiante = ''
        self.curso = ''
        self.estado = ''
        self.enrolamientos = []
        
    def ingresarEnrolamiento(self):
        self.enrolamientos.append({'estudiante':self.estudiante, 'curso': self.curso, 'estado': self.estado})

    def getEnrolamientos(self):
        return self.enrolamientos

    def setEstudiante (self, estudiante):
        self.estudiante = estudiante

    def setCurso (self, curso):
        self.curso = curso

    def setEstado (self, estado):
        self.estado = estado
        