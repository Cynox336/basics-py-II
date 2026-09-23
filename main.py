from libreria import agregar_libro, listar_libros, libros_por_autor, existe_libro

# Añade una colección de libros
mis_libros = []
mis_libros.append(agregar_libro("Arthas: Rise of the Lich King", "Christie Golden"))
mis_libros.append(agregar_libro("Sylvanas", "Christie Golden"))
mis_libros.append(agregar_libro("Stormrage", "Richard A. Knaak"))
mis_libros.append(agregar_libro("Day of the Dragon", "Richard A. Knaak"))

# Muestra la colección de libros creada
print("--- Colección de libros ---")
print(listar_libros(mis_libros))

# Busca un libro por el autor
print("\n--- Libros de Christie Golden ---")
print(libros_por_autor(mis_libros, "Christie Golden"))

# Verifica si un libro está disponible
print("\n--- Verificación de disponibilidad ---")
print("¿Está disponible 'Stormrage'?:", existe_libro(mis_libros, "Stormrage"))
print("¿Está disponible 'Illidan'?:", existe_libro(mis_libros, "Illidan"))