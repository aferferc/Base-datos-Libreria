import sqlite3 #Importa la libreria sqlite3 para hacer la base de datos
conexion = sqlite3.connect("libreria.db") #conecta o en caso de que no exista crea la base de datos bajo el nombre libreria
conexion.execute('PRAGMA foreign_keys= ON')


def crear(): #crea la funcion crear
    entrada_crear = int(input('''Has seleccionado crear un registro, elige el numero de la tabla a la que deseas añadirlo
    1.Libros
    2.Autores
    3.Ventas
    ''')) #recoge en una variable la obcion del usuario sobre que desea hacer tras darle las obciones
    if entrada_crear == 1: #a partir de aqui comprueba el valor de la variable llamando a la funcion que toca, si el valor no encaja, le dice al usuario que la entrada es errone a y vuelve al menu
        try: #trata de ejecutar el programa abajo
            valores_entrada = [(input("inserta la id del libro")), (input("inserta el titulo ")), (input("inserta el genero")), (input("inserta el año de publicacion")), (input("inserta la id del autor"))] #recoge los valores pedidos en una variable
            cursor = conexion.cursor() #conecta con la base de datos tras eso ingresa los valores recogidos previamente en la base con sql
            cursor.execute('''
            INSERT INTO Libros (ID_Libro, Titulo, Genero, Ano_Publicacion, ID_Autor) VALUES (?, ?, ?, ?, ?)
            ''', valores_entrada)
        except Exception as e: #en caso de que ocurra un error, se lo comunica al usuario, reestablece la base a su estado previo y detiene el programa
            print(f"Ocurrio un error: {e}, el programa se cerrara")
            conexion.rollback
            return
        finally: #si no sucede ningun error, guarda los cambios y termina la conexion con la base de datos
            conexion.commit
            conexion.close
    elif entrada_crear == 2:
        try: #trata de ejecutar el programa abajo
            valores_entrada = [(input("inserta la id del autor")), (input("inserta su nombre ")), (input("inserta su pais de origen"))] #recoge los valores pedidos en una variable
            cursor = conexion.cursor() #conecta con la base de datos tras eso ingresa los valores recogidos previamente en la base con sql
            cursor.execute('''
            INSERT INTO Autores (ID_Autor, Nombre, Pais_Origen) VALUES (?, ?, ?)
            ''', valores_entrada)
        except Exception as e: #en caso de que ocurra un error, se lo comunica al usuario, reestablece la base a su estado previo y detiene el programa
            print(f"Ocurrio un error: {e}, el programa se cerrara")
            conexion.rollback
            return
        finally: #si no sucede ningun error, guarda los cambios y termina la conexion con la base de datos
            conexion.commit
            conexion.close
    elif entrada_crear == 3:
        try: #trata de ejecutar el programa abajo
            valores_entrada = [(input("inserta la id de la venta")), (input("inserta la id del libro vendido ")), (input("inserta la fecha de venta")), (input("inserta la cantidad de volumenes vendidios")), (input("inserta el precio pagado"))] #recoge los valores pedidos en una variable
            cursor = conexion.cursor() #conecta con la base de datos tras eso ingresa los valores recogidos previamente en la base con sql
            cursor.execute('''
            INSERT INTO Ventas (ID_Venta, ID_Libro, Fecha_Venta, Cantidad_Vendidos, Precio_Total) VALUES (?, ?, ?, ?, ?)
            ''', valores_entrada)
        except Exception as e: #en caso de que ocurra un error, se lo comunica al usuario, reestablece la base a su estado previo y detiene el programa
            print(f"Ocurrio un error: {e}, el programa se cerrara")
            conexion.rollback
            return
        finally: #si no sucede ningun error, guarda los cambios y termina la conexion con la base de datos
            conexion.commit
            conexion.close
    else:
        print("Entrada de datos incorrecta, volviendo al menu")
        menu()

#ZONA PELIGROSA, RIESGO DE PANTALLAZO AZUL SI SE EJECUTAN ESTAS FUNCIONES

def leer():  # Crea la función leer
    entrada_leer = int(input('''Has seleccionado hacer una consulta, elige el número de la tabla a la que deseas hacer una consulta:
    1. Libros
    2. Autores
    3. Ventas
    '''))  # Recoge la opción del usuario

    if entrada_leer == 1:  # Si selecciona Libros
        entrada_leer = int(input('''Has seleccionado hacer una consulta, elige el tipo de consulta:
        1. Consulta por ID
        2. Consulta por Columna
        '''))  # Recoge la selección del usuario
        if entrada_leer == 1:  # Consulta por ID
            try:
                criterio = input("Inserta el ID del libro: ")
                conexion = sqlite3.connect("libreria.db")
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM Libros WHERE ID_Libro = ?", (criterio,))
                resultados = cursor.fetchall()
                print("Resultados de la consulta:", resultados)
            except Exception as e:
                print(f"Error al realizar la consulta: {e}, el programa se cerrará")
            finally:
                conexion.close()
        elif entrada_leer == 2:  # Consulta por Columna
            print("Esta funcionalidad no está completamente definida. Asegúrate de agregar lógica adecuada.")
        else:
            print("Entrada de datos incorrecta, volviendo al menú.")
    elif entrada_leer == 2:  # Si selecciona Autores
        entrada_leer = int(input('''Has seleccionado hacer una consulta, elige el tipo de consulta:
        1. Consulta por ID
        2. Consulta por Columna
        '''))  # Recoge la selección del usuario
        if entrada_leer == 1:  # Consulta por ID
            try:
                criterio = input("Inserta el ID del autor: ")
                conexion = sqlite3.connect("libreria.db")
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM Autores WHERE ID_Autor = ?", (criterio,))
                resultados = cursor.fetchall()
                print("Resultados de la consulta:", resultados)
            except Exception as e:
                print(f"Error al realizar la consulta: {e}, el programa se cerrará")
            finally:
                conexion.close()
        elif entrada_leer == 2:  # Consulta por Columna
            print("Esta funcionalidad no está completamente definida. Asegúrate de agregar lógica adecuada.")
        else:
            print("Entrada de datos incorrecta, volviendo al menú.")
    elif entrada_leer == 3:  # Si selecciona Ventas
        entrada_leer = int(input('''Has seleccionado hacer una consulta, elige el tipo de consulta:
        1. Consulta por ID
        2. Consulta por Columna
        '''))  # Recoge la selección del usuario
        if entrada_leer == 1:  # Consulta por ID
            try:
                criterio = input("Inserta el ID de la venta: ")
                conexion = sqlite3.connect("libreria.db")
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM Ventas WHERE ID_Venta = ?", (criterio,))
                resultados = cursor.fetchall()
                print("Resultados de la consulta:", resultados)
            except Exception as e:
                print(f"Error al realizar la consulta: {e}, el programa se cerrará")
            finally:
                conexion.close()
        elif entrada_leer == 2:  # Consulta por Columna
            print("Esta funcionalidad no está completamente definida. Asegúrate de agregar lógica adecuada.")
        else:
            print("Entrada de datos incorrecta, volviendo al menú.")
    else:
        print("Entrada de datos incorrecta, volviendo al menú.")

def actualizar():  # Función para actualizar registros
    entrada_actualizar = int(input('''Has seleccionado actualizar un registro. Elige el número de la tabla a la que deseas realizar la actualización:
    1. Libros
    2. Autores
    3. Ventas
    '''))  # Recoge la opción del usuario

    if entrada_actualizar == 1:  # Si selecciona Libros
        try:
            id = input("Inserta el ID del libro a actualizar: ")
            columna = input("Inserta el nombre de la columna que deseas actualizar (por ejemplo, Titulo, Genero, etc.): ")
            nuevo_valor = input(f"Inserta el nuevo valor para la columna '{columna}': ")
            conexion = sqlite3.connect("libreria.db")
            cursor = conexion.cursor()
            query = f"UPDATE Libros SET {columna} = ? WHERE ID_Libro = ?"
            cursor.execute(query, (nuevo_valor, id))
            conexion.commit()
            print(f"Registro actualizado correctamente en la tabla 'Libros'.")
        except Exception as e:
            print(f"Error al actualizar el registro en la tabla 'Libros': {e}")
            conexion.rollback()
        finally:
            conexion.close()

    elif entrada_actualizar == 2:  # Si selecciona Autores
        try:
            id = input("Inserta el ID del autor a actualizar: ")
            columna = input("Inserta el nombre de la columna que deseas actualizar (por ejemplo, Nombre, Pais_Origen): ")
            nuevo_valor = input(f"Inserta el nuevo valor para la columna '{columna}': ")
            conexion = sqlite3.connect("libreria.db")
            cursor = conexion.cursor()
            query = f"UPDATE Autores SET {columna} = ? WHERE ID_Autor = ?"
            cursor.execute(query, (nuevo_valor, id))
            conexion.commit()
            print(f"Registro actualizado correctamente en la tabla 'Autores'.")
        except Exception as e:
            print(f"Error al actualizar el registro en la tabla 'Autores': {e}")
            conexion.rollback()
        finally:
            conexion.close()

    elif entrada_actualizar == 3:  # Si selecciona Ventas
        try:
            id = input("Inserta el ID de la venta a actualizar: ")
            columna = input("Inserta el nombre de la columna que deseas actualizar (por ejemplo, Fecha_Venta, Cantidad_Vendidos, Precio_Total): ")
            nuevo_valor = input(f"Inserta el nuevo valor para la columna '{columna}': ")
            conexion = sqlite3.connect("libreria.db")
            cursor = conexion.cursor()
            query = f"UPDATE Ventas SET {columna} = ? WHERE ID_Venta = ?"
            cursor.execute(query, (nuevo_valor, id))
            conexion.commit()
            print(f"Registro actualizado correctamente en la tabla 'Ventas'.")
        except Exception as e:
            print(f"Error al actualizar el registro en la tabla 'Ventas': {e}")
            conexion.rollback()
        finally:
            conexion.close()

    else:  # Entrada incorrecta
        print("Entrada de datos incorrecta, volviendo al menú.")

#FIN DE LA ZONA PELIGROSA

def eliminar(): #crea la funcion eliminar
    entrada_crear = int(input('''Has seleccionado eliminar un registro, elige el numero de la tabla del que deseas eliminarlo
    1.Libros
    2.Autores
    3.Ventas
    ''')) #recoge en una variable la obcion del usuario sobre que desea hacer tras darle las obciones
    if entrada_crear == 1: #a partir de aqui comprueba el valor de la variable llamando a la funcion que toca, si el valor no encaja, le dice al usuario que la entrada es errone a y vuelve al menu
        try: #trata de ejecutar el programa abajo
            valores_entrada = [(input("inserta la id del libro que desea eliminar"))] #recoge los valores pedidos en una variable
            cursor = conexion.cursor() #conecta con la base de datos tras eso elimina la consulta deseada en la base con sql
            cursor.execute(f'''
            DELETE FROM Libros
            WHERE "ID_Libro" = {valores_entrada}    ''')
        except Exception as e: #en caso de que ocurra un error, se lo comunica al usuario, reestablece la base a su estado previo y detiene el programa
            print(f"Ocurrio un error: {e}, el programa se cerrara")
            conexion.rollback
            return
        finally: #si no sucede ningun error, guarda los cambios y termina la conexion con la base de datos
            conexion.commit
            conexion.close
    elif entrada_crear == 2:
        try: #trata de ejecutar el programa abajo
            valores_entrada = [(input("inserta la id del autor que desea eliminar"))] #recoge los valores pedidos en una variable
            cursor = conexion.cursor() #conecta con la base de datos tras eso elimina la consulta deseada en la base con sql
            cursor.execute(f'''
            DELETE FROM Libros
            WHERE "ID_Libro" = {valores_entrada}    ''')
        except Exception as e: #en caso de que ocurra un error, se lo comunica al usuario, reestablece la base a su estado previo y detiene el programa
            print(f"Ocurrio un error: {e}, el programa se cerrara")
            conexion.rollback
            return
        finally: #si no sucede ningun error, guarda los cambios y termina la conexion con la base de datos
            conexion.commit
            conexion.close
    elif entrada_crear == 3:
        try: #trata de ejecutar el programa abajo
            valores_entrada = [(input("inserta la id de la venta que desea eliminar"))] #recoge los valores pedidos en una variable
            cursor = conexion.cursor() #conecta con la base de datos tras eso elimina la consulta deseada en la base con sql
            cursor.execute(f'''
            DELETE FROM Libros
            WHERE "ID_Libro" = {valores_entrada}    ''')
        except Exception as e: #en caso de que ocurra un error, se lo comunica al usuario, reestablece la base a su estado previo y detiene el programa
            print(f"Ocurrio un error: {e}, el programa se cerrara")
            conexion.rollback
            return
        finally: #si no sucede ningun error, guarda los cambios y termina la conexion con la base de datos
            conexion.commit
            conexion.close
    else:
        print("Entrada de datos incorrecta, volviendo al menu")
        menu()

def menu(): #crea la funcion menu
    entrada_menu = int(input('''Bienvenido a la base de datos de la libreria, por favor introduzca el nuemro de la obcion que desea realizar, las obciones son: 
    1.Crear un nuevo registro
    2.Crear una consulta
    3.Actualizar un registro
    4.Eliminar un registro
    ''')) #recoge en una variable la obcion del usuario sobre que desea hacer tras darle las obciones
    if entrada_menu == 1: #a partir de aqui comprueba el valor de la variable llamando a la funcion que toca, si el valor no encaja, le dice al usuario que la entrada es errone a y detiene el program con return
        crear()
    elif entrada_menu == 2:
        leer()
    elif entrada_menu == 3:
        actualizar()
    elif entrada_menu == 4:
        eliminar()
    else:
        print("Entrada de datos incorrecta, el programa se cerrara")
        return

menu()

