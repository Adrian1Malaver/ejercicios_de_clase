from biblioteca import Biblioteca
from estudiante import Estudiante
from docente import Docente
from administrador import Administrador

def main():
    biblioteca = Biblioteca()  # Crear una instancia de Biblioteca

    while True:
        print("\nSelecciona una sede:")
        print("1. Aduanilla")
        print("2. Macarena")
        print("3. La 40")
        print("4. El Vivero")
        print("5. Salir")

        opcion_sede = input("Tu elección: ")

        if opcion_sede == "1":
            sede = "Aduanilla"
        elif opcion_sede == "2":
            sede = "Macarena"
        elif opcion_sede == "3":
            sede = "La 40"
        elif opcion_sede == "4":
            sede = "El Vivero"
        elif opcion_sede == "5":
            break
        else:
            print("Opción inválida. Por favor, selecciona una sede válida.")
            continue

        estudiante = Estudiante(sede, biblioteca)  # Pasar la instancia de Biblioteca
        docente = Docente(sede, biblioteca)  # Pasar la instancia de Biblioteca
        administrador = Administrador(sede, biblioteca)  # Pasar la instancia de Biblioteca

        while True:
            print("\nSelecciona una opción:")
            print("1. Estudiante")
            print("2. Docente")
            print("3. Administrador")
            print("4. Cambiar de sede")
            print("5. Salir")

            opcion_usuario = input("Tu elección: ")

            if opcion_usuario == "1":
                codigo = input("Ingresa tu código de estudiante: ")
                estudiante.ingresar_codigo(codigo)

                print("\nSelecciona una acción:")
                print("1. Pedir un libro")
                print("2. Devolver un libro")
                print("3. Salir")
                accion_estudiante = input("Tu elección: ")
                
                if accion_estudiante == "1":
                    docente.ver_libros_disponibles()
                    nombre_libro = input("Ingresa el nombre del libro que deseas pedir: ")
                    estudiante.pedir_libro(nombre_libro)
                
                elif accion_estudiante == "2":
                    nombre_libro = input("Ingresa el nombre del libro que deseas devolver: ")
                    estudiante.devolver_libro(nombre_libro)
                
                elif accion_estudiante == "3":
                    continue

            elif opcion_usuario == "2":
                docente.ver_libros_disponibles()
            
            elif opcion_usuario == "3":
                administrador.elegir_sede(sede)
                print("\nSelecciona una acción:")
                print("1. Eliminar un libro")
                print("2. Agregar un libro")
                print("3. Salir")
                accion_administrador = input("Tu elección: ")
                
                if accion_administrador == "1":
                    docente.ver_libros_disponibles()
                    nombre_libro = input("Ingresa el nombre del libro que deseas eliminar: ")
                    administrador.eliminar_libro(nombre_libro)
                
                elif accion_administrador == "2":
                    nombre_libro = input("Ingresa el nombre del nuevo libro: ")
                    administrador.agregar_libro(nombre_libro)
                
                elif accion_administrador == "3":
                    continue

            elif opcion_usuario == "4":
                break

if __name__ == "__main__":
    main()