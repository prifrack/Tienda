import pickle


class Producto:
    def __init__(self, id, nombre, precio, stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Precio: ${self.precio:.2f}, Stock: {self.stock}"


class GestorVentas:
    def __init__(self):
        self.productos = []
        self.total_ventas = 0

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print("Producto agregado exitosamente.")

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

    def realizar_venta(self, id_producto, cantidad):
        for producto in self.productos:
            if producto.id == id_producto:
                if cantidad <= producto.stock:
                    producto.stock -= cantidad
                    venta_total = cantidad * producto.precio
                    self.total_ventas += venta_total
                    print(
                        f"Venta realizada. Total de venta: ${venta_total:.2f}")
                else:
                    print("No hay suficiente stock para esta venta.")
                return
        print("Producto no encontrado.")

    def calcular_total_ventas(self):
        return self.total_ventas

    def guardar_productos(self, archivo):
        with open(archivo, 'wb') as file:
            pickle.dump(self.productos, file)
        print("Datos guardados exitosamente.")

    def cargar_productos(self, archivo):
        try:
            with open(archivo, 'rb') as file:
                self.productos = pickle.load(file)
            print("Datos cargados exitosamente.")
        except FileNotFoundError:
            print("El archivo no existe.")


if __name__ == "__main__":
    gestor_ventas = GestorVentas()

    while True:
        print("\nMenú:")
        print("1. Agregar producto")
        print("2. Mostrar lista de productos")
        print("3. Realizar venta")
        print("4. Calcular total de ventas")
        print("5. Guardar datos en archivo")
        print("6. Cargar datos desde archivo")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = int(input("ID del producto: "))
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            stock = int(input("Stock del producto: "))
            producto = Producto(id, nombre, precio, stock)
            gestor_ventas.agregar_producto(producto)

        elif opcion == "2":
            print("Lista de productos:")
            gestor_ventas.mostrar_productos()

        elif opcion == "3":
            id_producto = int(input("ID del producto a vender: "))
            cantidad = int(input("Cantidad a vender: "))
            gestor_ventas.realizar_venta(id_producto, cantidad)

        elif opcion == "4":
            total_ventas = gestor_ventas.calcular_total_ventas()
            print(f"Total de ventas realizadas: ${total_ventas:.2f}")

        elif opcion == "5":
            archivo = input("Nombre del archivo para guardar los datos: ")
            gestor_ventas.guardar_productos(archivo)

        elif opcion == "6":
            archivo = input("Nombre del archivo para cargar los datos: ")
            gestor_ventas.cargar_productos(archivo)

        elif opcion == "7":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
