#Creamos la CLase Cursos

class Courses:
    def __init__(self):
        self.Cursos = {}


    def ingresarCursoApr(self,Curso):
        self.Cursos.update({Curso:{'Aprobados':1,'Reprobados':0}})

    def ingresarCursoRpb(self,Curso):
        self.Cursos.update({Curso:{'Aprobados':0,'Reprobados':1}})

    def actualizarCursoApr(self,Curso):
        apr = self.getCursos()[Curso]['Aprobados'] + 1
        rpb = self.getCursos()[Curso]['Reprobados']
        self.Cursos.update({Curso:{'Aprobados':apr,'Reprobados':rpb}})

    def actualizarCursoRpb(self,Curso):
        apr = self.getCursos()[Curso]['Aprobados']
        rpb = self.getCursos()[Curso]['Reprobados'] + 1
        self.Cursos.update({Curso:{'Aprobados':apr,'Reprobados':rpb}})

    def getCursos(self):
        return self.Cursos
        
    def verificarCursoApr(self, Curso):
        if (Curso in self.Cursos):
            
            self.actualizarCursoApr(Curso)
            return True
        else:
            return False

    def verificarCursoRpb(self, Curso):
        if (Curso in self.Cursos):
            self.actualizarCursoRpb(Curso)
            return True
        else:
            return False