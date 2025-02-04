import reflex as rx

from ReflexSelenium.Componentes.Listas import lista_favoritos
from ReflexSelenium.Componentes.cabecera import heading


@rx.page(route="/", title="Enlaces Favoritos")
def index() -> rx.Component:
   return rx.vstack(
       heading("Enlaces Favoritos", "cabecera_enlaces_favoritos"),
       lista_favoritos()
   )