from classes import DATA, Careers, Courses, Students, Enrollments

#'numero_cuenta': 4809152
#'nombre_completo': 'Marta 0 Martínez 0'
#'cursos_aprobados': ['Química', 'Enfermería']
#'cursos_reprobados': ['Economía', 'Geografía', 'Química']
#'edad': 36
#'carrera': 'Administración de Empresas'

#print(DATA[0]['numero_cuenta'])
#print(DATA[0]['nombre_completo'])

#for apr in DATA[0]['cursos_aprobados']:
#    print(apr)

#for rpb in DATA[0]['cursos_reprobados']:
#    print(rpb)

#print(DATA[0]['edad'])
#print(DATA[0]['carrera'])

#Definiendo Objetos
iCarrera = Careers()
iCurso = Courses()
iEstudiante = Students()
iEnrolamiento = Enrollments()

for item in DATA:
#    if(iCarrera.verificarCarrera(item['carrera'])):
#        pass
#    else:
#        iCarrera.ingresarCarrera(item['carrera'])
#
#    for apr in item['cursos_aprobados']:
#        if(iCurso.verificarCursoApr(apr)):
#            pass
#        else:
#            iCurso.ingresarCursoApr(apr)
        

#    for rpb in item['cursos_reprobados']:
#        if(iCurso.verificarCursoRpb(rpb)):
#            pass
#        else:
#            iCurso.ingresarCursoRpb(rpb)

    for apr in item['cursos_aprobados']:
        iEnrolamiento.setEstudiante(item['nombre_completo'])
        iEnrolamiento.setCurso(apr)
        iEnrolamiento.setEstado('Aprobado')
        iEnrolamiento.ingresarEnrolamiento()

    for rpb in item['cursos_reprobados']:
        iEnrolamiento.setEstudiante(item['nombre_completo'])
        iEnrolamiento.setCurso(rpb)
        iEnrolamiento.setEstado('Reprobado')
        iEnrolamiento.ingresarEnrolamiento()
print(iEnrolamiento.getEnrolamientos())

        
        

    
        
#print(iCarrera.getCarreras())
#print(iCurso.getCursos())

#for key, value in iCarrera.getCarreras().items():
#    print(key, value)

#for key, value in iCurso.getCursos().items():
#    print(key, value)