def test_escritura_csv(self):
    # Se borran los clientes 48H y 15J
    db.Clientes.borrar('48H')
    db.Clientes.borrar('15J')
    # Se modifica el cliente 28Z
    db.Clientes.modificar('28Z', 'Mariana', 'Pérez')
    # Se abre el fichero de datos y se leen sus datos
    dni, nombre, apellido = None, None, None
    with open(config.DATABASE_PATH, newline="\n") as fichero:
        logging.debug("Se abre el fichero de datos")
        reader = csv.reader(fichero, delimiter=";")
        logging.debug("Se lee el fichero de datos")
        dni, nombre, apellido = next(reader) # Primera línea del iterador
        logging.debug("Se lee la primera línea del fichero de datos")
    # Se comprueba que el cliente 28Z tiene los datos actualizados
    self.assertEqual(dni, '28Z')
    self.assertEqual(nombre, 'Mariana')
    self.assertEqual(apellido, 'Pérez')
    
