import reflex as rx

from ReflexSelenium.Componentes.Listas import lista_buscadores
from ReflexSelenium.Componentes.cabecera import heading


@rx.page(route="/buscadores", title="Buscadores")
def buscadores() -> rx.Component:
   return rx.vstack(
      heading("Buscadores", "cabecera_buscadores"),
      lista_buscadores()
   )