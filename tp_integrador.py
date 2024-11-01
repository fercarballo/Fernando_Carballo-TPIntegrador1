# Trabajo Integrador: Organizador Académico

class Alumno:
    def __init__(self, nombre, apellido, dni, beca=False):
        self.nombre = nombre
        self.apellido = apellido
        self.__dni = dni  
        self.beca = beca  # Indica si el alumno es becado o no
        self.materias = []  # Lista de materias del alumno

    def agregar_materia(self, materia):
        self.materias.append(materia)

    def mostrar_informacion(self):
        # Muestra la información básica del alumno
        beca_status = "Becado" if self.beca else "No Becado"
        print(f"Nombre: {self.nombre} {self.apellido}, DNI: {self.__dni}, Estado: {beca_status}")
        for materia in self.materias:
            print(f"Materia: {materia.nombre}")

class Materia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []  # Lista de notas de la materia

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def calcular_promedio(self):
        # Calcula y devuelve el promedio de las notas
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)


class AlumnoRegular(Alumno):
    def __init__(self, nombre, apellido, dni):
        super().__init__(nombre, apellido, dni, beca=False)

class AlumnoBecado(Alumno):
    def __init__(self, nombre, apellido, dni):
        super().__init__(nombre, apellido, dni, beca=True)

    def calcular_promedio(self):
        promedio = super().calcular_promedio()
        return promedio * 1.1  # Los alumnos becados tienen un 10% extra en el promedio

class Profesor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.materias = []  # Lista de materias asignadas

    def asignar_materia(self, materia):
        self.materias.append(materia)

    def mostrar_materias(self):
        # Muestra las materias asignadas al profesor
        print(f"Profesor: {self.nombre} {self.apellido}")
        for materia in self.materias:
            print(f"Materia: {materia.nombre}")


def menu():
    # Lista inicial de alumnos
    alumnos = [
        AlumnoRegular('Juan', 'Pérez', '12345678'),
        AlumnoBecado('Ana', 'González', '87654321'),
    ]
    
    # materias predefinidas a los alumnos
    matematica = Materia('Matemática')
    matematica.agregar_nota(7.5)
    matematica.agregar_nota(8.0)
    alumnos[0].agregar_materia(matematica)

    historia = Materia('Historia')
    historia.agregar_nota(9.0)
    alumnos[1].agregar_materia(historia)

    # Lista inicial de profesores
    profesores = [
        Profesor('Carlos', 'Fernández'),
        Profesor('María', 'López')
    ]
    
    # materias a los profesores
    profesores[0].asignar_materia(matematica)
    profesores[1].asignar_materia(historia)

    # Lista inicial de alumnos
    alumnos = [
        AlumnoRegular('Juan', 'Pérez', '12345678'),
        AlumnoBecado('Ana', 'González', '87654321'),
    ]
    
    # materias predefinidas a los alumnos
    matematica = Materia('Matemática')
    matematica.agregar_nota(7.5)
    matematica.agregar_nota(8.0)
    alumnos[0].agregar_materia(matematica)

    historia = Materia('Historia')
    historia.agregar_nota(9.0)
    alumnos[1].agregar_materia(historia)

    # Lista inicial de profesores
    profesores = [
        Profesor('Carlos', 'Fernández'),
        Profesor('María', 'López')
    ]
    
    # materias a los profesores
    profesores[0].asignar_materia(matematica)
    profesores[1].asignar_materia(historia)

    # La lista de alumnos y profesores ya tiene algunos valores iniciales cargados por las dudas
    while True:
        print("\n--- Organizador Académico ---")
        print("1. Agregar Alumno")
        print("2. Agregar Materia a Alumno")
        print("3. Agregar Nota a Materia")
        print("4. Mostrar Información de Alumnos")
        print("5. Agregar Profesor")
        print("6. Asignar Materia a Profesor")
        print("7. Mostrar Información de Profesores")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del alumno: ")
            apellido = input("Apellido del alumno: ")
            dni = input("DNI del alumno: ")
            tipo = input("Tipo de alumno (regular/becado): ").lower()
            if tipo == "becado":
                alumno = AlumnoBecado(nombre, apellido, dni)
            else:
                alumno = AlumnoRegular(nombre, apellido, dni)
            alumnos.append(alumno)
            print("Alumno agregado correctamente.")

        elif opcion == "2":
            if not alumnos:
                print("No hay alumnos registrados.")
                continue
            nombre_alumno = input("Nombre del alumno al que desea agregar una materia: ")
            alumno = next((a for a in alumnos if a.nombre == nombre_alumno), None)
            if alumno:
                nombre_materia = input("Nombre de la materia: ")
                materia = Materia(nombre_materia)
                alumno.agregar_materia(materia)
                print("Materia agregada correctamente.")
            else:
                print("Alumno no encontrado.")

        elif opcion == "3":
            if not alumnos:
                print("No hay alumnos registrados.")
                continue
            nombre_alumno = input("Nombre del alumno: ")
            nombre_materia = input("Nombre de la materia: ")
            alumno = next((a for a in alumnos if a.nombre == nombre_alumno), None)
            if alumno:
                materia = next((m for m in alumno.materias if m.nombre == nombre_materia), None)
                if materia:
                    nota = float(input("Ingrese la nota: "))
                    materia.agregar_nota(nota)
                    print("Nota agregada correctamente.")
                else:
                    print("Materia no encontrada.")
            else:
                print("Alumno no encontrado.")

        elif opcion == "4":
            if not alumnos:
                print("No hay alumnos registrados.")
                continue
            for alumno in alumnos:
                alumno.mostrar_informacion()
                for materia in alumno.materias:
                    print(f"Promedio en {materia.nombre}: {materia.calcular_promedio()}")

        elif opcion == "5":
            nombre = input("Nombre del profesor: ")
            apellido = input("Apellido del profesor: ")
            profesor = Profesor(nombre, apellido)
            profesores.append(profesor)
            print("Profesor agregado correctamente.")

        elif opcion == "6":
            if not profesores:
                print("No hay profesores registrados.")
                continue
            nombre_profesor = input("Nombre del profesor al que desea asignar una materia: ")
            profesor = next((p for p in profesores if p.nombre == nombre_profesor), None)
            if profesor:
                nombre_materia = input("Nombre de la materia: ")
                materia = Materia(nombre_materia)
                profesor.asignar_materia(materia)
                print("Materia asignada correctamente.")
            else:
                print("Profesor no encontrado.")

        elif opcion == "7":
            if not profesores:
                print("No hay profesores registrados.")
                continue
            for profesor in profesores:
                profesor.mostrar_materias()

        elif opcion == "8":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el menú interactivo
menu()
