# class Materia:
#     def __init__(self, nombre, horario, profesores, alumnos, ano):
#         self.__nombre__ = nombre
#         self.__horario__=horario
#         self.__profesores__= profesores 
#         self.__alumnos__=alumnos
#         self.__ano__=ano
#     def agregar_alumno(self, alumno):
#         self.__alumnos__.append(alumno)
#     def obtener_alumno(self):
#         return self.__alumnos__


# computacion= Materia()
# computacion.agregar_alumno()

class Profesor:
    def __init__(self, nombre, cargo, legajo):
        self.__nombre__ = nombre
        self.__cargo__ = cargo
        self.__legajo__ = legajo

    def obtener_nombre(self):
        return self.__nombre__
    
    def obtener_cargo(self):
        return self.__cargo__
    
    def obtener_legajo(self):
        return self.__legajo__

     
class Alumno:
    def __init__(self,nombre, legajo, edad, mail):
        self.__nombre__ = nombre
        self.__legajo__ = legajo
        self.__edad__ = edad
        self.__mail__ = mail

    def obtener_nombre(self):
        return self.__nombre__

    def cambiar_mail(self, mail):
        self.__mail__= mail


class Materia : 
    def __init__ (self, nombre, profesores, ):
        self.__nombre__ = nombre
        self.__profesores__ = profesores
        self.__alumnos__ = []
    
    def obtener_alumno(self):
        return self.__alumnos__
    
    def obtener_profesores(self):
        return self.__profesores__ 
    
    def cambiar_nombre(self, nombre):
        self.__nombre__ = nombre 
    
    def agregar_alumno(self,alumno):
        self.__alumnos__.append(alumno)

