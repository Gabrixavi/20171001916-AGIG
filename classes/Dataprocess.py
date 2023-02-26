from classes import DATA
from classes.Careers import Careers
from classes.Courses import Courses
from classes.Students import Students
from classes.Enrollments import Enrollments
class Dataprocess:

    def __init__(self, data):
        self.__data = data
        self.iCarrera = Careers()
        self.iCurso = Courses()
        self.iEnrolamiento = Enrollments()
        self.iEstudiante = Students()

    def create_careers(self):
        ## Do something to create careers on your mongodb collection using __data
        
        for item in self.__data:
            if(self.iCarrera.verificarCarrera(item['carrera'])):
                pass
            else:
                self.iCarrera.ingresarCarrera(item['carrera'])
        return True
    def create_courses(self):
        ## Do something to create courses on your mongodb collection using __data
        
        for item in DATA:
            for apr in item['cursos_aprobados']:
                if(self.iCurso.verificarCursoApr(apr)):
                    pass
                else:
                    self.iCurso.ingresarCursoApr(apr)
        

            for rpb in item['cursos_reprobados']:
                if(self.iCurso.verificarCursoRpb(rpb)):
                    pass
                else:
                    self.iCurso.ingresarCursoRpb(rpb)
        return True

    def create_students(self):
        ## Do something to create students on your mongodb collection using __data

        return True

    def create_enrollments(self):
        ## Do something to create enrollments on your mongodb collection using __data
        for item in DATA:
            for apr in item['cursos_aprobados']:
                self.iEnrolamiento.setEstudiante(item['nombre_completo'])
                self.iEnrolamiento.setCurso(apr)
                self.iEnrolamiento.setEstado('Aprobado')
                self.iEnrolamiento.ingresarEnrolamiento()

            for rpb in item['cursos_reprobados']:
                self.iEnrolamiento.setEstudiante(item['nombre_completo'])
                self.iEnrolamiento.setCurso(rpb)
                self.iEnrolamiento.setEstado('Reprobado')
                self.iEnrolamiento.ingresarEnrolamiento()
        return True

    def getCarreras1(self):
        return self.iCarrera.getCarreras()
    def getCursos1(self):
        return self.iCurso.getCursos()
    def getEnrolamientos1(self):
        return self.iEnrolamiento.getEnrolamientos()