# Importa a função principal da visualização de login
from view.loginView import main
# Importa o modelo de login para validação
from model.loginModel import LoginModel
import flet as ft  # Importa a biblioteca Flet para construção da interface


class LoginController:

    def __init__(self):
        # Inicializa a aplicação Flet com o método iniciarLogin
        ft.app(self.iniciarLogin)

    def iniciarLogin(self, page: ft.Page):
        # Chama a função main para criar os elementos da interface
        usuario, senha, mensagem, botao = main(page)

        # Função chamada ao clicar no botão de login
        def login(e):
            # Valida as credenciais do usuário
            if LoginModel().validar_login(usuario.value, senha.value):
                mensagem.value = "Login realizado com sucesso"
                
            else:
                mensagem.value = "Nome de usuário ou senha inválidos"
                            
            page.update()  # Atualiza a página para refletir as mudanças

        # Define a função de login como o manipulador de clique do botão
        botao.on_click = login
