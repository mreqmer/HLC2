"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from ReflexSelenium.paginas.index import index
from ReflexSelenium.paginas.buscadores import buscadores
from ReflexSelenium.paginas.redes_sociales import redes_sociales

from ReflexSelenium.Componentes.cabecera import heading
from rxconfig import config


class State(rx.State):
    """The app state."""
    ...

app = rx.App()
app._compile()

