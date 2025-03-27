import flet as ft
# Flet é uma biblioteca de interface gráfica para Python


# Função principal para criar a interface de login
def main(page: ft.Page):
    page.title = "Losgin"

    # Cria um widget de texto para exibir mensagens
    mensagem = ft.Text()
    # Cria um campo de entrada de texto para o nome de usuário
    usuario = ft.TextField(label="Nome de Usuário")
    # Cria um campo de entrada de texto para a senha
    senha = ft.TextField(label="Senha", password=True,
                         can_reveal_password=True)
    # Cria um botão para o login
    botao = ft.ElevatedButton(text="Entrar")

    # Adiciona os elementos da interface à página
    page.add(usuario, senha, mensagem, botao)

    page.add(ft.Text("*Usuário: emerson, Senha: 123*"))

    # Retorna os elementos da interface para o controlador
    return usuario, senha, mensagem, botao
