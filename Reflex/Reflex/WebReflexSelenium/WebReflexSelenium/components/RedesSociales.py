import reflex as rx

def redesSociales_componente():
    return rx.vstack(
        rx.heading("Redes sociales"),  # Encabezado sin tamaño específico
        rx.list(
            rx.list_item(rx.link("Instagram", href="https://www.instagram.com", is_external=True)),
            rx.list_item(rx.link("TikTok", href="https://www.tiktok.com", is_external=True)),
            rx.list_item(rx.link("Facebook", href="https://www.facebook.com", is_external=True)),
        ),
        rx.button("Volver", on_click=lambda: rx.redirect("/")),  # Botón para volver al índice
        spacing="4",  # Espaciado entre elementos
    )