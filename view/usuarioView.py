import flet as ft

def pageUsuario(page: ft.Page):
    page.title = "Usuário"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#1e1e1e"
    
    mensagem = ft.Text(
        "Olá Usuário!",
        size=24,
        weight=ft.FontWeight.BOLD,
        color="#00FFFF",
        text_align=ft.TextAlign.CENTER
    )
    
    botao = ft.ElevatedButton(
        text="Voltar para o Login",
        bgcolor="#FF4500",  # Botão com cor laranja neon
        color="#1e1e1e",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
            padding=ft.Padding(15, 10, 15, 10)
        ),
        on_click=lambda e: print("Botão clicado!")
    )
    
    page.add(
        ft.Column([
            ft.Text("Está é uma página de exemplo!"),
            mensagem,
            botao
        ], 
        alignment=ft.MainAxisAlignment.CENTER, 
        spacing=20, 
        expand=True)
    )
    
    return botao
