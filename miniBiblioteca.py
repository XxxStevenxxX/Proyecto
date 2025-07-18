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
socios = [
    {
        'nombre': 'Ana Torres',
        'codigo': '001',
        'correo': 'ana.torres@example.com',
        'estado': 'registrado'
    },
    {
        'nombre': 'Luis Gómez',
        'codigo': '002',
        'correo': 'luis.gomez@example.com',
        'estado': 'registrado'
    },
    {
        'nombre': 'Camila Ríos',
        'codigo': '003',
        'correo': 'camila.rios@example.com',
        'estado': 'registrado'
    }


]
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
    print("")
    print ("Registrar usuarios 👥")
    print("Digite 0 para volver al menú principal")
    
    nombre = input("Nombre del usuario: ").strip().lower()
    if not nombre:
        print("❌ El nombre del usuario no puede estar vacío ❌")
        registrar_socio()
    if nombre == '0': return
    
    codigo = input ("Digite el código del usuario: ").strip()
    if not codigo:
        print("❌ El código del usuario no puede estar vacío ❌")
        registrar_socio()
    if codigo == '0': return
    
    correo = input ("Digite el correo electrónico:").strip().lower()
    if not correo:
        print("❌ El correo del usuario no puede estar vacío ❌")
        registrar_socio()
    if correo == '0': return
    
    for s in socios:
        if s ['codigo'] == codigo:
            print(f"❌ Ya existe un usuario registrado con el código {codigo}, por favor, digita uno nuevo ❌")
            
    nuevo_socio = {
        'nombre': nombre,
        'codigo': codigo,
        'correo': correo,
        'estado': 'registrado',
        'librosPrestados': None
    }
    socios.append(nuevo_socio)
    print("")
    print(f"Usuario {nombre} registrado exitosamente con el código {codigo} 👥")
    print(f"Correo del usuario:{correo}")
    print("")

def prestar_libro():
    global libros , socios
    
    #Solicitar ISBN del libro
    print("📚 Préstamo de libros 📚")
    print("Digita 0 para volver al menú principal")
    print("")
    isbn = input("Digita el ISBN del libro: ")
    if not isbn:
        print("❌ El ISBN del libro no puede estar vacío ❌")
        prestar_libro()
    if isbn == '0': return
    
    #Buscar libro
    libro_encontrado = None
    for libro in libros:
        if libro['isbn'] == isbn:
            libro_encontrado = libro
            break
    
    if not libro_encontrado:
        print(f"No se encontró un libro con el ISBN {isbn}").strip().lower()
    
    #Buscar usuario
    codigo_usuario = input("Digita el código del usuario: ")
    if not codigo_usuario:
        print("❌ El ID del usuario no puede estar vacío ❌")
        prestar_libro()
    if codigo_usuario == '0': return
    
    usuario_encontrado = None
    for socio in socios:
        if socio['codigo'] == codigo_usuario:
            usuario_encontrado = socio
            break
    
    #Verificación de disponibilidad del libro
    libro_disponible = None    
    for libro in libros:
        if libro['estado'] == 'Disponible':
            libro_disponible = True
            break
    if not libro_disponible:
            print(f"El libro {libro['titulo']} no se encuentra disponible")
            return
        
    libro_encontrado['estado'] = 'Prestado'
    libro_encontrado['socio_prestado'] = codigo_usuario
    
    print(f"El libro {libro['titulo']} fue prestado exitosamente al usuario {socio['nombre']}")
            
            

def devolver_libro():
    global libros
    isbn = input("Digita el ISBN del libro: ")
    if not isbn:
        print("❌ El ISBN del libro no puede estar vacío ❌")
        devolver_libro()
    if isbn == '0': return
    
    #Buscar libro
    libro_encontrado = None
    for libro in libros:
        if libro['isbn'] == isbn:
            libro_encontrado = libro
            break
    
    if not libro_encontrado:
        print(f"No se encontró un libro con el ISBN {isbn}").strip().lower()
        return
    libro_encontrado['estado'] = 'Disponible'
    libro_encontrado['socio_prestado'] = None
    print("Libro devuelto exitosamente")
    

def libros_prestados():
    
    for i, libro in enumerate(libros, 1):
        if libro ['estado'] == 'Prestado':
            print(f"{i}. Nombre del libro: {libro["titulo"]}")
            print(f"   Autor: {libro["autor"]}")
            print(f"   ISBN: {libro["isbn"]}")
            print(f"   Usuario: {libro['socio_prestado']}")
            print("")
    
        

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
   print("")
   print("Lista de usuarios registrados 👥")
   print("")
   
   if not socios:
       print("❌ No hay usuarios registrados en el sistema ❌")
       return
   for i, socio in enumerate(socios, 1):
       print(f"{i}. Nombre del usuario: {socio["nombre"]}")
       print(f"   Código de registro: {socio["codigo"]}")
       print(f"   Correo del usuario: {socio["correo"]}")
       print(f"   Estado: {socio["estado"]}")
       print("")
         
    
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