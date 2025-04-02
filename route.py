from controller.loginController import LoginController
from controller.usuarioController import UsuarioController
import flet as ft

class Route:
    
    
    def __init__(self, page, rota):
        
        page.clean()

        match rota:
            case '/':
                LoginController(page)
            case '/usuario':
                UsuarioController(page)
            case _:
                print('Página não encontrada')
                page.add(ft.Text('Página não encontrada'))
