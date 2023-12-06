class Clientes:
    lista = []
    def buscar(dni):
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente
    def crear(dni, nombre, apellido):
        nuevo_cliente = Cliente(dni, nombre, apellido)
        Clientes.lista.append(nuevo_cliente)
        print("Se agrego el cliente: " + nuevo_cliente)
        return nuevo_cliente
    def modificar(dni, nombre, apellido):
        cliente = Clientes.buscar(dni)
        cliente.nombre = nombre
        cliente.apellido = apellido
        print("Se modifico el cliente: " + cliente)
        return cliente
    def borrar(dni):
        cliente = Clientes.buscar(dni)
        Clientes.lista.remove(cliente)
        print("Se borro el cliente: " + cliente)
        return cliente