from pydantic.color import Color


def Colores(color):
    ColorDevuelto = ""
    if(color == "grisOscuro"):
        ColorDevuelto = "#e0e0e0",
    elif (color == "grisClaro"):
        ColorDevuelto = "#d4d4d4"

    return ColorDevuelto
