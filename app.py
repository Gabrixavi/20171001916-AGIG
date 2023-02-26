import pymongo

from classes import DATA, DbMongo, Dataprocess
from dotenv import load_dotenv

def main():

    #client, db = DbMongo.getDB()

    pipeline = Dataprocess(DATA)
    
    pipeline.create_careers()
    pipeline.create_courses()
    pipeline.create_students()
    pipeline.create_enrollments()


    #Imprime Lista de Carreras
    print(pipeline.getCarreras1())
    print('\n\n\n')

    #Imprime Cursos con Numero de Aprobados y Reprobados
    print(pipeline.getCursos1())
    print('\n\n\n')

    #Imprime Lista de Enrolamiento
    print(pipeline.getEnrolamientos1())
    print('\n\n\n')



    #client.close()
    return True

if __name__ == "__main__":
    main()