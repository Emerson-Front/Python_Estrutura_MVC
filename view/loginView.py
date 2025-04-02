import flet as ft

def pageLogin(page: ft.Page):
    page.title = "Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#f5f5f5"
    
    mensagem = ft.Text(
        color="red", 
        size=14
    )
    
    titulo = ft.Text(
        "Bem-vindo!", 
        size=24, 
        weight=ft.FontWeight.BOLD, 
        color="blue"
    )
    
    usuario = ft.TextField(
        label="Nome de Usuário", 
        width=300, 
        text_style=ft.TextStyle(color="black"), 
        hint_text="Digite seu usuário", 
        hint_style=ft.TextStyle(color="gray")
    )
    
    senha = ft.TextField(
        label="Senha", 
        password=True, 
        can_reveal_password=True, 
        width=300, 
        text_style=ft.TextStyle(color="black"), 
        hint_text="Digite sua senha", 
        hint_style=ft.TextStyle(color="gray")
    )
    
    botao = ft.ElevatedButton(
        text="Entrar", 
        bgcolor="#007BFF", 
        color="white",
        width=300,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
            padding=ft.Padding(15, 10, 15, 10)
        )
    )
    
    page.add(
        ft.Column([
            titulo,
            usuario,
            senha,
            mensagem,
            botao,
            ft.Text(
                "*Usuário: emerson, Senha: 123*", 
                color="red", 
                size=12
            )
        ], 
        alignment=ft.MainAxisAlignment.CENTER, 
        spacing=10, 
        expand=True)
    )
    
    return usuario, senha, mensagem, botao