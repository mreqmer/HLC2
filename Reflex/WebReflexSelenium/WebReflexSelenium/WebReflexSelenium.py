"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from reflex_chakra import vstack

from WebReflexSelenium.components.Index_Contenido import *
from WebReflexSelenium.components.Buscadores import *
from WebReflexSelenium.components.RedesSociales import *
from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
   return rx.vstack(
       index_contenido(),
   )
def buscadores() -> rx.Component:
   return rx.vstack(
       buscadores_content(),
   )
def redes_sociales() -> rx.Component:
    return rx.vstack(
        redesSociales_componente()
    )


app = rx.App()
app.add_page(index)
app.add_page(buscadores, route="/buscadores")
app.add_page(redes_sociales, route="/redes_sociales")

