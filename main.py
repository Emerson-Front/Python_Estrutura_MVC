import flet as ft
import route

def main(page: ft.Page):
    
    route.Route(page, page.route)
          
ft.app(target=main)
