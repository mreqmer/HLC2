import reflex as rx
from reflex import color

from WebReflexSelenium.colores.Colores import Colores

def index_contenido():
    return rx.vstack(
        rx.heading("Enlaces favoritos"),
        rx.list(
            rx.list.item(rx.link("Buscadores", href="/buscadores")),
            rx.list.item(rx.link("Redes Sociales", href="/redes_sociales")),
        ),
        spacing="4",
    )

