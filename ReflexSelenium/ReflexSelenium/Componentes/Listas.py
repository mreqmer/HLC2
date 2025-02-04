import reflex as rx

def lista_buscadores():
    return (
        rx.list(
            rx.list.item(rx.link("Google", href="https://www.google.com/?hl=es", id="link_google", is_external = True)),
            rx.list.item(rx.link("Bing", href="https://www.bing.com/?setlang=es", id="link_bing", is_external = True)),
            rx.list.item(rx.link("Baidu", href="https://www.baidu.com/", id="link_baidu", is_external = True)),
            id="lista_buscadores"
        ),
    )

def lista_favoritos():
    return (
        rx.list(
            rx.list.item(rx.link("Buscadores", href="/buscadores", id="buscadores")),
            rx.list.item(rx.link("Redes Sociales", href="/redes_sociales", id="redes_sociales")),
            id="lista_favoritos"
        ),
    )