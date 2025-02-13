import reflex as rx

class FormState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def form_example():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(
                    id="form_nombre",
                    placeholder="Nombre:",
                    name="nombre",
                ),
                rx.input(
                    id="form_apellidos",
                    placeholder="Apellidos: ",
                    name="apellidos",
                ),
                rx.hstack(
                    rx.text("Sexo: "),
                    rx.radio(
                        ["Hombre", "Mujer"],
                        name="sexo",
                        direction = "column",
                        id="form_sexo"
                    ),
                ),
                rx.input(
                    id="form_correo",
                    placeholder = "Correo: ",
                    name = "correo"
                ),
                rx.vstack(
                    rx.checkbox(
                        text="Deseo recibir información sobre novedades y ofertas",
                        name="checkOfertas",
                        default_checked = True,
                        ),
                    rx.checkbox(
                        "Declaro haber leido y aceptar las condiciones generales del programa y la normativa sobre protección de datos.",
                        name="checkTerminos",
                    ),
                ),
                rx.button(
                    "Enviar",
                    type="submit",
                    id="form_button"
                ),
            ),
            on_submit=FormState.handle_submit,
            reset_on_submit=True,
            id="formulario_id"
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(FormState.form_data.to_string()),
    )