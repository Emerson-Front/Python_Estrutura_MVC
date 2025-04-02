import flet as ft
from view.usuarioView import pageUsuario
import route

class UsuarioController:

    def __init__(self, page):
                
        botao = pageUsuario(page)

        def botao_clicado(e):
            route.Route(page, '/')

        botao.on_click = botao_clicado