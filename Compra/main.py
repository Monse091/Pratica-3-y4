import flet as ft
from page_view import PageView

def main(page: ft.Page):

    def route_change(e):
        page.views.clear()
        if page.route == "/":
            page.views.append(
                ft.View(
                    "/",
                    [
                        ft.AppBar(
                            leading_width=40,
                            title=ft.Text("Bienvenido Al Super"),
                            center_title=False,
                            bgcolor=ft.colors.PURPLE_400,
                        ),
                        ft.Row([
                            page_view.home_page(),
                        ], expand=True)
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page_view = PageView(page)
    page.on_view_pop = view_pop

    page.go(page.route)

ft.app(main)