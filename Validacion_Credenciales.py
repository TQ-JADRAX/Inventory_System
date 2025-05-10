from Producto import *
from Objetos import *
from Carrito import *
from Inventario import *
from Interfaz_Usuario import *
from Interfaz_Empleado import *

def Validacion_Credencial():
    while True:
        try:
            print('USUARIO / EMPLEADO / SALIR')
            credencial = int(input('1/2/3: '))
            if credencial == 1:
                Menu_Usuario()
            elif credencial == 2:
                Menu_Empleado()
            elif credencial == 3:
                break
        except NameError as e:
            print(e)
        except Exception as e:
            print(e)


          





Validacion_Credencial()
