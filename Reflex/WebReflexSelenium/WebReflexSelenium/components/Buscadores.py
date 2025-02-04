import reflex as rx


def buscadores_content():
    return rx.vstack(
        rx.heading("Buscadores"),
        rx.list(
            rx.list_item(rx.link("Google", href="https://www.google.com", is_external=True)),
            rx.list_item(rx.link("Bing", href="https://www.bing.com", is_external=True)),
            rx.list_item(rx.link("Baidu", href="https://www.baidu.com", is_external=True)),
        ),
        rx.button("Volver", on_click=lambda: rx.redirect("/")),  # Botón para volver al índice
        spacing="4",
    )