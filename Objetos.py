from Producto import Producto
from Categorias import *

class Helados(Producto):
    def info(self):
        print(f'Nombre: {self.nombre}')    
        print(f'Precio: {self.precio} ')
        print(f'Categoria: {self.categoria}')   
        print(f'Estado: {self.estado}')
        print(f'Stock:{self.stock}')   

Oreo = Helados('Oreo',32,categoria[7],42)
Dracula = Helados ('Dracula', 34,categoria[2],30)
Chococono = Helados ('Chococono', 30, categoria[1],25)
Colombina = Helados('Colombina',32, categoria[5],20)
Casero = Helados ('Casero', 28, categoria[7],15)


'''
Oreo.info()
Oreo.change_status()
Oreo.info()
Oreo.cambio_precio()
Oreo.info()

'''

'''
pida nombre, numero de stock
nombre no vacio
intento infinito
no acepte num negativos
'''