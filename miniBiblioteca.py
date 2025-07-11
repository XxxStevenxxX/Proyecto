libros = [
    {
    'isbn': '978-0140449136',
    'titulo': 'La Odisea',
    'autor': 'Homero',
    'estado': 'Disponible',
    'socio_prestado': None
    },
    {
    'isbn': '978-0307277785',
    'titulo': 'Cien años de soledad',
    'autor': 'Gabriel García Márquez',
    'estado': 'Disponible',
    'socio_prestado': None
    },
    {
    'isbn': '978-0192833983',
    'titulo': 'Don Quijote de la Mancha',
    'autor': 'Miguel de Cervantes',
    'estado': 'Disponible',
    'socio_prestado': None
    }
]
socios = []
contador = 1


#Muestra las opciones del menú
def mostrar_menu():
    print(" MINIBIBLIOTECA")
    print("1. Registrar libro")
    print("2. Registrar socio")
    print("3. Prestar un libro")
    print("4. Devolver libro")
    print("5. Ver libros prestados")
    print("6. Ver todos los libros")
    print("7. Ver todos los socios")
    print("0. Salir")
    
    

#Define el proceso de registro de libros en el sistema de biblioteca
def registrar_libro():
    global libros
    print("")
    print("Registrar libros 📖")
    print("Digite 0 si desea volver al menú principal")
    print("")
    
    titulo = input("Título del libro: ").strip()
    if not titulo:
        print("❌El título no puede estar vacío❌")
        registrar_libro()
    if titulo == "0": return
    
    autor = input("Autor del libro: ").strip().upper()
    if not autor:
        print("❌El autor no puede estar vacío❌")
        registrar_libro()
    if autor == "0": return
    
    isbn = input("ISBN del libro: ").strip().lower()
    if not isbn:
        print("❌El ISBN no puede estar vacío❌")
        registrar_libro()
    if isbn == "0": return
    
    for l in libros:
        if l['isbn'] == isbn:
            print(f"❌Ya existe un libro con el ISBN {isbn}❌")
     
    #Crear nuevo libro
    nuevo_libro = {
        'isbn': isbn,
        'titulo': titulo,
        'autor': autor,
        'estado': 'Disponible',
        'socio_prestado': None   
    }
    
    libros.append(nuevo_libro)
    print("")
    print("✅ Libro registrado exitosamente 📖")
    print(f"📚 {titulo} - {autor}")
    print(f"🔢ISBN: {isbn}")
print("")
def registrar_socio():
    global socios
    print ("Registrar usuarios 👥")
    
    nombre = input("Nombre del usuario: ").strip().lower()

def prestar_libro():
    pass

def devolver_libro():
    pass

def libros_prestados():
    pass

def todos_libros():
    print("")
    print("Lista de libros")
    print("")
    
    if not libros:
        print("No hay libros registrados en la biblioteca")
        return
    
    for i, libro in enumerate(libros, 1):
        print(f"{i}. Nombre del libro: {libro["titulo"]}")
        print(f"   Autor: {libro["autor"]}")
        print(f"   ISBN: {libro["isbn"]}")
        print(f"   Estado: {libro["estado"]}")
        print("")
    

def ver_socios():
    pass
    
def main():
    #Función principal del programa
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()
        
        match opcion:
            case '1':
                registrar_libro()
            case '2':
                registrar_socio()
            case '3':
                prestar_libro()
            case '4':
                devolver_libro()
            case '5':
                libros_prestados()
            case '6':
                todos_libros()
            case '7':
                ver_socios()
            case '0':
                print("Gracias por usar la biblioteca.")
                print("¡Vuelve pronto!🙂")
                break
            case _:
                print("Opción no válida. Por favor selecciona una opción válida")
main()