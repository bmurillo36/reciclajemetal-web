# -*- coding: utf-8 -*-
"""
Datos del centro y del curso de RECICLAJE del METAL, 4 horas.

QUE ES ESTA WEB: reciclajemetal.es, para quien tiene que renovar su formacion
del sector del METAL. La hermana es renovartpc.es, la de construccion. Son DOS
webs distintas a proposito y NO comparten textos (regla
no-duplicar-contenido-entre-webs de la memoria de Claude): si se copian, compiten
entre ellas en Google.

NI UN DATO INVENTADO. Lo que dicta Pedro va aqui; lo que regula el convenio va
con su fuente. Si algo no se sabe, no se publica: se pregunta.
"""

SITIO = "https://reciclajemetal.es"

# --- El centro (identico en todas sus webs; revisado por Pedro el 11/09/2026)
CENTRO = {
    "empresa": "Centro Médico Siglo XXI Prevención de Riesgos Laborales, S.L.",
    "marca": "Prevención Siglo 21",
    "homologacion_flc": "0505101086",   # Fundación Laboral de la Construcción
    "acreditacion_cm": "CM 87/2006",    # Comunidad de Madrid
    "direccion": "Calle La Fragua 1, Portal 2, 1ª planta (oficinas 2101, 2102 y 2104)",
    "cp": "28933",
    "ciudad": "Móstoles",
    "provincia": "Madrid",
    "referencia": "Junto a la Plaza de Toros",
    "telefonos": ["91 617 04 23", "630 29 25 16", "691 10 10 10"],
    "correo": "info@prevencion.cc",
}

TEL_E164 = {"91 617 04 23": "+34916170423",
            "630 29 25 16": "+34630292516",
            "691 10 10 10": "+34691101010"}

WASAP = "34630292516"
WASAP_TEXTO = ("Hola,%20quiero%20informaci%C3%B3n%20sobre%20el%20reciclaje%20"
               "del%20metal%20de%204%20horas")

MAPA = ("https://www.google.com/maps/search/?api=1&amp;"
        "query=Calle+La+Fragua+1+Portal+2+28933+M%C3%B3stoles+Madrid")

# --- El formulario ---------------------------------------------------------
# PENDIENTE: dar de alta la clave "reciclajemetal" en /etc/formularios/config.json
# del VPS (paso de root, ver despliegue/). Los campos que el servicio lee son
# SIETE y con inicial mayuscula: Nombre, Email, Telefono, Curso, Mensaje,
# Acepto, Origen.
FORMULARIO = "https://formularios.tpcmetal.es/enviar/reciclajemetal"

# --- La medicion -----------------------------------------------------------
# VACIO A PROPOSITO: reciclajemetal.es no esta en la tabla de contenedores de
# la gestora. El contenedor lo da Ana, no se inventa.
GTM = "GTM-56SQ9M6R"

# --- El curso --------------------------------------------------------------
# Precio y modalidad: los dicto Pedro el 16/09/2026 (70 EUR, presencial en
# Mostoles). El curso del metal YA ESTA HOMOLOGADO (Pedro, 16/09/2026).
#
# PENDIENTE PEDRO: periodicidad del reciclaje.
# `renovacion_anios` = 4 lo dijo Pedro, pero el portal oficial de la TPC NO
# publica ninguna periodicidad para el reciclaje del metal. Por eso el dato
# esta aqui pero NO SE USA EN NINGUNA PAGINA, a proposito. En cuanto haya una
# fuente, se escribe en paginas.py (portada y /tarjeta-profesional-metal/, que
# es donde hoy se dice «cuando tu empresa o la obra te lo pida»).
CURSO = {
    "nombre": "Reciclaje de la formación en prevención del sector del metal",
    "corto": "Reciclaje del metal de 4 horas",
    "horas": 4,
    "modalidad": "Presencial en Móstoles",
    "precio": 70,
    "renovacion_anios": 4,
}

HORARIO = [
    ("Lunes a jueves", "de 8 horas a 18 horas"),
    ("Viernes", "de 8 horas a 15 horas"),
    ("Sábados y domingos", "cerrado"),
]
HORARIO_NOTA = ("Los días que hay formación por la tarde —de 14 a 21 o de 15 "
                "a 22 horas— las aulas se quedan abiertas hasta esa hora.")
