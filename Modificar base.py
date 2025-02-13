import sqlite3 #Importa la libreria sqlite3 para hacer la base de datos
conexion = sqlite3.connect("libreria.db") #conecta o en caso de que no exista crea la base de datos bajo el nombre libreria

def actualizar_registro(id, nuevo_valor):
    conexion = int(input('''Has seleccionado actualizar regiistro'''))
    try:
        cursor = conexion.cursor()
        # Aquí cambiaremos la consulta SQL para una actualización
        cursor.execute("UPDATE tabla SET columna = %s WHERE id = %s", (nuevo_valor, id))
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        print(f"Error al actualizar el registro: {e}")
    finally:
        conexion.close()

def crear_consultas(consulta_tipo, criterio):
    conexion = int(input('''Has seleccionado hacer consulta UwU'''))
    try:
        cursor = conexion.cursor()
        if consulta_tipo == "por_id":
            cursor.execute("SELECT * FROM tabla WHERE id = %s", (criterio,))
        elif consulta_tipo == "por_columna":
            cursor.execute("SELECT * FROM tabla WHERE columna = %s", (criterio,))
        else:
            print("Tipo de consulta no reconocido")
            return None
        resultados = cursor.fetchall()
        return resultados
    except Exception as e:
        conexion.rollback()
        print(f"Error al realizar la consulta: {e}")
    finally:
        conexion.close()


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
            conexion.closes
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
            conexion.closes
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
            conexion.closes
    else:
        print("Entrada de datos incorrecta, volviendo al menu")
        menu()

def leer(): #crea la funcion leer
    print(2)

def actualizar(): #crea la funcion actualizar
    print(3)

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
            conexion.closes
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
            conexion.closes
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
            conexion.closes
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