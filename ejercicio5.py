# Clase Curso que representa un curso en la universidad
class Curso:
    def __init__(self, codigo, nombre, creditos, estudiantes):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.estudiantes = estudiantes

    def mostrar_datos(self):
        """ Muestra la información del curso """
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Créditos: {self.creditos}")
        print(f"Estudiantes inscritos: {self.estudiantes}")

    def calcular_creditos_totales(self):
        """ Calcula el total de créditos ofrecidos por el curso """
        return self.creditos

# Clase Universidad que gestiona una colección de cursos
class Universidad:
    def __init__(self):
        self.cursos = []

    def agregar_curso(self):
        """ Solicita al usuario la información del curso y lo agrega a la universidad """
        codigo = input("Ingrese el código del curso: ")
        nombre = input("Ingrese el nombre del curso: ")
        creditos = int(input("Ingrese el número de créditos del curso: "))
        estudiantes = int(input("Ingrese el número de estudiantes inscritos: "))
        curso = Curso(codigo, nombre, creditos, estudiantes)
        self.cursos.append(curso)
        print("Curso agregado exitosamente.")

    def mostrar_cursos(self):
        """ Muestra la información de todos los cursos en la universidad """
        if not self.cursos:
            print("No hay cursos registrados.")
            return
        print("\nInformación de los cursos:")
        for curso in self.cursos:
            print("\n---")
            curso.mostrar_datos()
            print("---")

    def calcular_creditos_totales(self):
        """ Calcula el número total de créditos ofrecidos por todos los cursos """
        creditos_totales = sum(curso.calcular_creditos_totales() for curso in self.cursos)
        return creditos_totales

# Función principal para interactuar con el usuario
def main():
    universidad = Universidad()

    while True:
        print("\nOpciones:")
        print("1. Agregar curso")
        print("2. Mostrar cursos")
        print("3. Calcular créditos totales")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            universidad.agregar_curso()
        elif opcion == '2':
            universidad.mostrar_cursos()
        elif opcion == '3':
            creditos_totales = universidad.calcular_creditos_totales()
            print(f"El número total de créditos ofrecidos es: {creditos_totales}")
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()
