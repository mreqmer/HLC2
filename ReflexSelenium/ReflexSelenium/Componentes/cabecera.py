import reflex as rx


def heading(titulo_cabecera : str, id_cabecera : str):
    return (
        rx.heading(titulo_cabecera, id=id_cabecera)
    )