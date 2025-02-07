import sqlite3 #Importa la libreria sqlite3 para hacer la base de datos
libros  = [ #crea una cadena llamada libros en la que se guardan todos los datos que la base tendra en la tabla libros
    (1, 'El Quijote', 'Novela', 1605, 1),
    (2, 'Cien Años de Soledad', 'Realismo magico', 1967, 2),
    (3, 'Don Juan', 'Teatro', 1630, 1),
    (4, 'El Amor en los Tiempos del Cólera', 'Romance', 1985, 2),
    (5, 'Crónica de una Muerte Anunciada', 'Misterio', 1981, 2),
    (6, 'La Hojarasca', 'Drama', 1955, 2),
    (7, 'Relato de un Náufrago', 'Aventuras', 1955, 2),
    (8, 'La Casa de los Espíritus', 'Realismo magico', 1982, 3),
    (9, 'De Amor y de Sombra', 'Romance', 1984, 3),
    (10, 'Eva Luna', 'Novela', 1987, 3),
    (11, 'Cuentos de Eva Luna', 'Cuentos', 1989, 3),
    (12, 'Paula', 'Biografia', 1994, 3),
    (13, 'La Sombra del Viento', 'Misterio', 2001, 10),
    (14, 'El Juego del Ángel', 'Misterio', 2008, 10),
    (15, 'El Prisionero del Cielo', 'Novela', 2011, 10),
    (16, 'Marina', 'Novela', 1999, 10),
    (17, 'La Ciudad de Vapor', 'Cuentos', 2020, 10),
    (18, 'La Noche del Oráculo', 'Misterio', 2003, 4),
    (19, 'El Libro de los Abrazos', 'Cuentos', 1989, 5),
    (20, 'Las Venas Abiertas de América Latina', 'Historia', 1971, 5)
    ]
autores = [ #crea una cadena llamada autorers en la que se guardan todos los datos que la base tendra en la tabla autores
    (1, 'Miguel de Cervantes', 'España'),
    (2, 'Gabriel García Márquez', 'Colombia'),
    (3, 'Isabel Allende', 'Chile'),
    (4, 'Jorge Luis Borges', 'Argentina'),
    (5, 'Eduardo Galeano', 'Uruguay'),
    (6, 'Mario Vargas Llosa', 'Peru'),
    (7, 'Mario Benedetti', 'Uruguay'),
    (8, 'Laura Esquivel', 'Mexico'),
    (9, 'Julio Cortazar', 'Argentina'),
    (10, 'Carlos Ruiz Zafon', 'España')
]

ventas = [ #crea una cadena llamada ventas en la que se guardan todos los datos que la base tendra en la tabla ventas
    (1, 1, '2023-01-05', 2, 40.00),
    (2, 2, '2023-02-10', 1, 20.00),
    (3, 3, '2023-03-15', 5, 100.00),
    (4, 4, '2023-04-20', 3, 60.00),
    (5, 5, '2023-05-10', 4, 80.00),
    (6, 6, '2023-06-25', 1, 20.00),
    (7, 7, '2023-07-15', 2, 40.00),
    (8, 8, '2023-08-05', 3, 60.00),
    (9, 9, '2023-09-10', 2, 40.00),
    (10, 10, '2023-10-20', 1, 20.00),
    (11, 11, '2023-11-01', 2, 40.00),
    (12, 12, '2023-12-10', 3, 60.00),
    (13, 13, '2024-01-05', 4, 80.00),
    (14, 14, '2024-02-15', 1, 20.00),
    (15, 15, '2024-04-25', 3, 60.00),
    (16, 16, '2024-04-25', 3, 60.00),
    (17, 17, '2024-05-15', 5, 100.00),
    (18, 18, '2024-06-10', 2, 40.00),
    (19, 19, '2024-07-05', 1, 20.00),
    (20, 20, '2024-08-15', 3, 60.00)
]

conexion = sqlite3.connect("libreria.db") #conecta o en caso de que no exista crea la base de datos bajo el nombre libreria
cursor = conexion.cursor()
#crea la tabla autores con sus respectivos atributos usando sql
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS Autores (
    ID_Autor INT PRIMARY KEY,
    Nombre VARCHAR(255) NOT NULL,
    Pais_Origen VARCHAR(255)
);
''')
#crea la tabla Libros con sus respectivos atributos usando sql
cursor.execute('''
CREATE TABLE IF NOT EXISTS Libros (
    ID_Libro INT PRIMARY KEY,
    Titulo VARCHAR(255) NOT NULL,
    Genero VARCHAR(100),
    Ano_Publicacion INT,
    ID_Autor INT,
    FOREIGN KEY (ID_Autor) REFERENCES AUTORES(ID_Autor) 
    ON UPDATE CASCADE 
    ON DELETE CASCADE
);
''')
#crea la tabla Ventas con sus respectivos atributos usando sql
cursor.execute('''
CREATE TABLE IF NOT EXISTS Ventas (
    ID_Venta INT PRIMARY KEY,
    ID_Libro INT,
    Fecha_Venta DATE,
    Cantidad_Vendidos INT,
    Precio_Total DECIMAL(10, 2),
    FOREIGN KEY (ID_Libro) REFERENCES LIBROS(ID_Libro) 
    ON UPDATE CASCADE 
    ON DELETE CASCADE
);
''')
#inserta en la tabla Autores todos los datos que se habian guardado en la lista autores
cursor.executemany('''
INSERT INTO Autores (ID_Autor, Nombre, Pais_Origen) VALUES (?, ?, ?)
''', autores)
#inserta en la tabla libros todos los datos que se habian guardado en la lista libros
cursor.executemany('''          
INSERT INTO Libros (ID_Libro, Titulo, Genero, Ano_Publicacion, ID_Autor) VALUES (?, ?, ?, ?, ?)
''', libros)     
#inserta en la tabla Ventas todos los datos que se habian guardado en la lista ventas
cursor.executemany ('''              
INSERT INTO Ventas (ID_Venta, ID_Libro, Fecha_Venta, Cantidad_Vendidos, Precio_Total) VALUES (?, ?, ?, ?, ?)
''', ventas) 

conexion.commit() #guarda todos los cambios realizados en la base
conexion.close() #termina la conexion con la base