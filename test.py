import unittest
from clases import Alumno, Materia, Profesor

class TestMateria (unittest.TestCase):
    
    def test_constructor(self):
        nombre='Algebra'
        profesores=['Eugenia','Ruth']
        algebra=Materia(nombre,profesores)
        self.assertEqual(algebra.__nombre__,'Algebra')
        self.assertEqual(algebra.__profesores__,['Eugenia','Ruth'])
    
    def test_obtener_profesores(self):
        nombre='Algebra'
        profesores=['Eugenia','Ruth']
        algebra=Materia(nombre,profesores)
        self.assertEqual(algebra.obtener_profesores(),['Eugenia','Ruth'])
    
    def test_cambiar_nombre(self):
        nombre='Algebra'
        profesores=['Eugenia','Ruth']
        algebra=Materia(nombre,profesores)
        algebra.cambiar_nombre('Algebralineal')
        self.assertEqual(algebra.__nombre__,'Algebralineal')

class TestProfesor (unittest.TestCase):
     
     def test_profesor(self):
        profesores = Profesor("eugenia", "titular", "7000")
        self.assertEqual(profesores.__nombre__, "eugenia")
        self.assertEqual(profesores.__cargo__, "titular")
        self.assertEqual(profesores.__legajo__, "7000")

     def test_obtener_nomnbre(self):
        profesores = Profesor("eugenia", "titular", "7000")
        self.assertEqual(profesores.obtener_nombre(), "eugenia")

     def test_obtener_cargo(self):
        profesores = Profesor("eugenia", "titular", "7000")
        self.assertEqual(profesores.obtener_cargo(), "titular")

     def test_obtener_legajo(self):
        profesores = Profesor("eugenia", "titular", "7000")
        self.assertEqual(profesores.obtener_legajo(), "7000")

class TestAlumno (unittest.TestCase):
  
    def test_alumno(self):
        alumno = Alumno("Delfina", "62133", "20", ".d.susel")
        self.assertEqual(alumno.__nombre__, "Delfina")
        self.assertEqual(alumno.__legajo__, "62133")
        self.assertEqual(alumno.__edad__, "20")
        self.assertEqual(alumno.__mail__, ".d.susel") 

    def test_obtener_nombre(self):
        alumno = Alumno("Delfina", "62133", "20", ".d.susel")
        self.assertEqual(alumno.obtener_nombre(), "Delfina")

    def test_cambiar_mail(self):
        mail = ".d.susel"
        alumno = Alumno("Delfina", "62133", "20", mail)
        alumno.cambiar_mail("sb.escudero")
        self.assertEqual(alumno.__mail__, "sb.escudero")






unittest.main()