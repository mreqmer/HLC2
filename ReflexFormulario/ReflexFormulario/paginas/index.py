import reflex as rx

from ReflexFormulario.componentes.formularios import form_example


@rx.page(route="/", title="Mi Web")
def index() -> rx.Component:
   return rx.vstack(
       form_example()
   )