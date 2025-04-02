from view.loginView import pageLogin
from model.loginModel import LoginModel
from controller.usuarioController import UsuarioController
import route

class LoginController:

    def __init__(self, page):
        self.page = page
        usuario, senha, mensagem, botao = pageLogin(page)
        
        
        def botao_clicado(e):
            if LoginModel.validar_login(self, usuario.value, senha.value):
                mensagem.value = "Login realizado com sucesso"

                route.Route(self.page, '/usuario')
            else:
                mensagem.value = "Nome de usuário ou senha inválidos"
            page.update()
        
                       
        botao.on_click = botao_clicado
