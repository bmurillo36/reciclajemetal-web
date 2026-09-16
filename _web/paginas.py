# -*- coding: utf-8 -*-
"""
El contenido de reciclajemetal.es, página a página.

Cada función devuelve (cuerpo, extra_head). El «extra» es lo que va en la
cabecera de esa página y solo de esa: los datos estructurados, sobre todo.

REGLA AL ESCRIBIR AQUÍ: NI UN DATO INVENTADO.

  - Lo del CENTRO (precio, edad, qué llevar, FUNDAE, duplicado, horario) lo
    dictó Pedro y vive en centro.py.
  - Lo del CONVENIO (los 15 reciclajes, los tres temarios, quién emite la
    tarjeta, la caducidad de cinco años) sale de trabajoenconstruccion.com,
    el portal oficial de la TPC, y aquí se dice con su fuente.
  - Lo que NO se sabe no se publica. En concreto:

        Pedro dice «cada 4 años». El portal oficial NO publica ninguna
        periodicidad para el reciclaje del metal. Hasta que haya una fuente,
        esta web NO afirma cada cuánto se repite: habla de «cuando tu empresa
        o la obra te lo pida» y de que la TARJETA caduca a los cinco años.
        Lo mismo vale para `CURSO["renovacion_anios"]` de centro.py: está
        puesto, pero NO se usa en ninguna página a propósito.

  - Tampoco se publica: número de homologación de ESTE curso, fechas de
    convocatoria, plazas, ofertas ni urgencias. Prohibido por Pedro.
"""

import json

from centro import (SITIO, CENTRO, TEL_E164, CURSO, HORARIO, HORARIO_NOTA,
                    FORMULARIO, WASAP, WASAP_TEXTO, MAPA)

MENU = [
    ("/", "Inicio"),
    ("/curso-reciclaje-metal-4-horas/", "El curso"),
    ("/oficios/", "Oficios"),
    ("/tarjeta-profesional-metal/", "La tarjeta"),
    ("/preguntas-frecuentes/", "Preguntas"),
    ("/contacto/", "Contacto"),
]

TEL1 = CENTRO["telefonos"][0]

CONVENIO = ("IV Convenio colectivo estatal de la industria, las nuevas "
            "tecnologías y los servicios del sector del metal")

# --- Los 15 reciclajes del catálogo del metal ------------------------------
# Copiados LITERALMENTE de la sección «Formación de Reciclaje» del catálogo del
# sector del metal de trabajoenconstruccion.com. Son 15 cursos de 4 horas,
# amparados por el Anexo IV del IV Convenio del metal. El orden es el del
# catálogo (alfabético). No se añade ni se quita ninguno.
OFICIOS = [
    "Administrativos",
    "Electricidad (montaje y mantenimiento de instalaciones eléctricas de "
    "alta y baja tensión)",
    "Ferrallado",
    "Fontanería e instalaciones de climatización",
    "Instalación de ascensores",
    "Instalaciones, reparaciones, montajes, estructuras metálicas, cerrajería "
    "y carpintería metálica",
    "Mandos intermedios",
    "Mantenimiento de maquinaria y vehículos",
    "Operadores de aparatos elevadores",
    "Operadores de equipos manuales",
    "Responsables y técnicos de ejecución de la actividad",
    "Trabajos de construcción y mantenimiento de vías férreas",
    "Trabajos de instalación de equipos contraincendios",
    "Trabajos de instalaciones de telecomunicaciones",
    "Trabajos en gasoductos y redes de distribución de gases combustibles",
]

# --- Los tres temarios que tenemos por escrito -----------------------------
# Son los tres únicos de los que tenemos el contenido oficial. De los otros
# doce NO se publica temario: se publica el esquema que comparten los tres, y
# se dice que es un esquema. Inventar el temario de un oficio ajeno es la
# forma más rápida de que alguien venga con el curso equivocado.
TEMARIOS = [
    ("Administrativos", "administrativos", [
        "Técnicas preventivas: protección colectiva y equipos de protección "
        "individual, pantallas de visualización, medidas de emergencia, "
        "primeros auxilios y botiquín.",
        "Medios auxiliares, equipos y herramientas: el mobiliario frente a "
        "los riesgos posturales y ergonómicos.",
        "Verificación e identificación del lugar de trabajo y de su entorno.",
        "Iluminación y ambiente de trabajo.",
        "Documentación y panel informativo de obra.",
    ]),
    ("Ferrallado", "ferrallado", [
        "A. Definición de los trabajos: ferralla armada en taller o en obra, "
        "acopio, armado y montaje en forjados, muros, trincheras, vigas, "
        "pilares, escaleras y rampas.",
        "B. Técnicas preventivas específicas: identificación y evaluación de "
        "los riesgos del puesto.",
        "Medios auxiliares y equipos de corte y doblado.",
        "Manipulación manual de cargas, posturas forzadas y movimientos "
        "repetitivos.",
        "Trabajos en altura.",
        "Protección colectiva y protección individual.",
        "Etiquetado y fichas de datos de seguridad.",
    ]),
    ("Electricidad: alta y baja tensión", "electricidad", [
        "Definición de los trabajos: líneas aéreas y subterráneas de alta y "
        "baja tensión, centros de transformación y subestaciones.",
        "Montaje y mantenimiento eléctrico industrial y de edificación, e "
        "instalaciones provisionales de obra.",
        "Técnicas preventivas: identificación y evaluación de los riesgos del "
        "puesto y medios auxiliares.",
        "Real Decreto 614/2001, sobre el riesgo eléctrico.",
        "Manipulación manual de cargas y trabajos en altura.",
        "Protección colectiva e individual, y líneas de vida verticales y "
        "horizontales.",
    ]),
]

# El patrón que comparten los tres temarios de arriba. Se publica COMO
# ESQUEMA, no como temario de nadie.
ESQUEMA = [
    ("Qué trabajos cubre el oficio",
     "Cada reciclaje empieza delimitando las tareas de las que habla: qué "
     "entra en ese oficio y qué no. Es lo que distingue un reciclaje de otro."),
    ("Identificación y evaluación de los riesgos del puesto",
     "Los riesgos concretos de esas tareas, no los de la construcción en "
     "general."),
    ("Medios auxiliares, equipos y herramientas",
     "Las máquinas y los medios propios del oficio, y cómo se usan sin "
     "llevarse un susto."),
    ("Protección colectiva y equipos de protección individual",
     "Qué protege a todos y qué te protege a ti, y en qué orden se aplica "
     "cada cosa."),
]

INCLUYE = [
    ("Las 4 horas completas", "presenciales, en nuestra aula de Móstoles."),
    ("El material", "lo pone el centro. No tienes que comprar nada."),
    ("El título del curso", "te lo entregamos al terminar."),
    ("Sin extras", "70 € y ahí está todo. Ni matrícula ni sorpresas."),
]

PARA_QUIEN = [
    ("Ya hiciste la formación del metal",
     "Hiciste el curso de tu oficio en su día y ahora te piden actualizarla."),
    ("Tu empresa te lo pide",
     "La empresa o la obra te dice que tienes el reciclaje pendiente y hay "
     "que resolverlo."),
    ("Entras en obras de construcción",
     "Trabajas para una empresa del ámbito del Acuerdo Estatal del Sector "
     "del Metal y pisas obra."),
    ("Empresas con varios trabajadores",
     "Si sois un grupo, abrimos convocatoria propia para vosotros."),
]

PREGUNTAS = [
    ("¿Qué es exactamente el reciclaje de la formación del metal?",
     "Es una acción formativa de 4 horas del catálogo de formación del sector "
     "del metal. Está en la sección «Formación de Reciclaje» de ese catálogo, "
     "amparada por el Anexo IV del " + CONVENIO + ". Sirve para actualizar la "
     "formación preventiva del oficio que ya hiciste en su día."),

    ("¿Cuánto cuesta y cuánto dura?",
     "70 € el curso completo y 4 horas de duración. Es presencial, en nuestro "
     "centro de Móstoles. En el precio entra el material y el título; no hay "
     "matrícula ni extras."),

    ("¿Cada cuánto hay que hacer el reciclaje?",
     "Depende de lo que te pidan tu empresa o la obra. El portal oficial de la "
     "Tarjeta Profesional de la Construcción no publica una periodicidad para "
     "el reciclaje del metal, así que no te vamos a dar una cifra que no "
     "podamos respaldar. Lo que sí tiene fecha es la tarjeta: caduca a los "
     "cinco años de su emisión. Si a ti te han dado un plazo por escrito, "
     "tráelo y lo cuadramos contigo."),

    ("¿El curso de 4 horas me da la tarjeta del metal?",
     "No por sí solo. Para obtener la Tarjeta Profesional de la Construcción "
     "del sector del metal se exige al menos una acción formativa de 8 horas o "
     "más. El reciclaje de 4 horas es formación de actualización, no la vía "
     "para conseguir la tarjeta. Además, la tarjeta no la emite el centro: la "
     "emite la Fundación del Metal para la Formación, Cualificación y el "
     "Empleo."),

    ("¿Quién tiene que hacer esta formación?",
     "Los trabajadores de las empresas del ámbito del Acuerdo Estatal del "
     "Sector del Metal que realizan sus trabajos en obras de construcción. Si "
     "tu empresa es del metal y entras en obra, te afecta."),

    ("¿Qué oficios tienen curso de reciclaje?",
     "Quince, todos de 4 horas: administrativos; electricidad de alta y baja "
     "tensión; ferrallado; fontanería y climatización; instalación de "
     "ascensores; instalaciones, reparaciones, montajes, estructuras "
     "metálicas, cerrajería y carpintería metálica; mandos intermedios; "
     "mantenimiento de maquinaria y vehículos; operadores de aparatos "
     "elevadores; operadores de equipos manuales; responsables y técnicos de "
     "ejecución de la actividad; vías férreas; equipos contraincendios; "
     "telecomunicaciones; y gasoductos y redes de distribución de gases "
     "combustibles."),

    ("¿Se puede hacer online?",
     "No. Este curso lo damos presencial, en nuestra aula de Móstoles. Son "
     "cuatro horas y se hacen aquí."),

    ("¿Qué tengo que llevar el día del curso?",
     "Solo el DNI o el NIE. Todo lo demás lo pone el centro."),

    ("¿Qué edad hace falta?",
     "18 años cumplidos."),

    ("Voy a llegar tarde, ¿pasa algo?",
     "Hay 30 minutos de margen. Pasados esos treinta minutos ya no se puede "
     "entrar, porque el curso tiene que cumplir sus cuatro horas. Ven puntual "
     "y no hay problema."),

    ("¿Cuándo es el próximo grupo?",
     "Los grupos se abren según la demanda. No publicamos un calendario fijo "
     "a propósito: preferimos apuntar lo que necesitas y avisarte en cuanto "
     "haya fecha. Si sois varios de una misma empresa, abrimos convocatoria "
     "para vosotros."),

    ("¿Se puede bonificar por FUNDAE?",
     "El curso es bonificable, pero la gestión no la hacemos nosotros: hay que "
     "tramitarla con una entidad organizadora externa. Y si eres autónomo, no "
     "tienes crédito de formación. Preferimos decirlo antes que después."),

    ("He perdido el título, ¿me dais otro?",
     "Sí. El duplicado del título cuesta 10 €."),

    ("¿Es lo mismo que la tarjeta de construcción?",
     "No. La Tarjeta Profesional de la Construcción del sector del metal la "
     "emite la Fundación del Metal para la Formación, Cualificación y el "
     "Empleo, según el IV Convenio Estatal del Sector del Metal. La del sector "
     "de la construcción va por otro convenio y por otra entidad. Si no sabes "
     "cuál te están pidiendo, llámanos antes de pagar nada: lo miramos "
     "contigo en un minuto."),

    ("¿Dónde se solicita o se renueva la tarjeta del metal?",
     "En la Fundación del Metal para la Formación, Cualificación y el Empleo, "
     "en la calle Rivas 25, Polígono Industrial Vicálvaro, 28052 Madrid, "
     "teléfono 911 77 01 31. El portal oficial de la tarjeta tiene además un "
     "teléfono gratuito, el 900 11 21 21. La renovación se tramita por el "
     "mismo procedimiento que la solicitud inicial."),
]


# --- Piezas que se repiten -------------------------------------------------

def _tic():
    return ('<svg width="18" height="18" viewBox="0 0 24 24" fill="none" '
            'stroke="#3F6759" stroke-width="2.6" stroke-linecap="round" '
            'stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>')


def _botonera(principal="Pedir fecha", href="/contacto/"):
    return (
        '<div class="botonera">'
        '<a class="btn btn--cta" href="%s">%s</a>'
        '<a class="btn btn--linea" href="tel:%s">Llamar al %s</a>'
        '</div>' % (href, principal, TEL_E164[TEL1], TEL1))


def _formulario(titulo="Pregunta lo que necesites", ruta="/"):
    """El formulario. Va al servicio propio de Pedro; ver centro.py.

    `ruta` es la página en la que se pinta, y solo sirve para el campo Origen:
    así se sabe DESDE QUÉ PÁGINA pidió información cada persona. Esta web no
    tiene medición (la gestora no le ha asignado contenedor), así que ese campo
    es hoy la única forma de saberlo.
    """
    return """
<section class="seccion seccion--menta" id="pedir">
  <div class="wrap">
    <div class="rejilla rejilla--2">
      <div class="aparece">
        <p class="rotulo">Hablamos</p>
        <h2>%(titulo)s</h2>
        <p class="entradilla">Déjanos el teléfono y te llamamos nosotros. Si
        tienes prisa, llamar es más rápido: normalmente lo resolvemos en la
        misma llamada.</p>
        <div class="botonera">
          <a class="btn btn--salvia" href="tel:%(tel_e)s">Llamar al %(tel)s</a>
          <a class="btn btn--linea" href="https://wa.me/%(wasap)s?text=%(wtexto)s"
             rel="noopener">WhatsApp</a>
        </div>
        <div class="aviso">
          <p><strong>Los grupos se abren según la demanda.</strong> Dinos qué
          oficio es el tuyo y cuándo te viene bien, y te avisamos en cuanto
          haya fecha. Si sois varios de una empresa, abrimos grupo para
          vosotros.</p>
        </div>
      </div>

      <div class="form-caja aparece" data-orden="1">
        <form class="form" method="post" action="%(accion)s">
          <input type="hidden" name="_next" value="%(sitio)s/gracias/">
          <input type="hidden" name="_t" value="">
          <input type="hidden" name="Origen" value="reciclajemetal.es%(ruta)s">
          <p style="position:absolute;left:-9999px" aria-hidden="true">
            <label>No rellenar <input type="text" name="_honey" tabindex="-1" autocomplete="off"></label>
          </p>

          <div class="campo">
            <label for="nombre">Nombre y apellidos <span class="obl">*</span></label>
            <input id="nombre" name="Nombre" type="text" required autocomplete="name"
                   maxlength="80" placeholder="Como aparece en tu DNI">
          </div>
          <div class="campo">
            <label for="telefono">Teléfono <span class="obl">*</span></label>
            <input id="telefono" name="Telefono" type="tel" required autocomplete="tel"
                   inputmode="tel" maxlength="20" placeholder="600 00 00 00">
            <span class="pista">Es por donde te avisamos de la fecha.</span>
          </div>
          <div class="campo">
            <label for="correo">Correo electrónico</label>
            <input id="correo" name="Email" type="email" autocomplete="email"
                   maxlength="90" placeholder="opcional">
          </div>
          <div class="campo">
            <label for="cuando">¿Cuál es tu oficio?</label>
            <select id="cuando" name="Curso">%(oficios)s</select>
            <span class="pista">Si no lo ves claro, deja «No lo sé» y lo miramos
            contigo.</span>
          </div>
          <div class="campo">
            <label for="mensaje">Cuéntanos</label>
            <textarea id="mensaje" name="Mensaje" maxlength="900"
              placeholder="Si te lo pide una obra o una empresa concreta, dínoslo: así te confirmamos que este es el curso que te piden."></textarea>
          </div>
          <label class="consentimiento">
            <input type="checkbox" name="Acepto" value="si" required>
            <span>He leído la <a href="/politica-de-privacidad/">política de
            privacidad</a> y acepto que uséis mis datos para responderme.</span>
          </label>
          <button type="submit" class="btn btn--cta">Enviar y que me llamen</button>
          <p class="form__aviso">Solo lo usamos para contestarte. Ni lo vendemos
          ni te apuntamos a ninguna lista.</p>
        </form>
      </div>
    </div>
  </div>
</section>""" % {
        "titulo": titulo, "accion": FORMULARIO, "sitio": SITIO,
        "ruta": ruta,
        "oficios": ('<option value="Reciclaje metal 4 h">No lo sé, ayudadme'
                    '</option>' + "".join(
                        '<option value="Reciclaje metal 4 h · %s">%s</option>'
                        % (o.split(" (")[0], o) for o in OFICIOS)),
        "tel": TEL1, "tel_e": TEL_E164[TEL1],
        "wasap": WASAP, "wtexto": WASAP_TEXTO}


def _ld(*bloques):
    return "".join('<script type="application/ld+json">%s</script>\n'
                   % json.dumps(b, ensure_ascii=False, separators=(",", ":"))
                   for b in bloques)


def _centro_ld():
    return {
        "@context": "https://schema.org",
        "@type": ["EducationalOrganization", "LocalBusiness"],
        "@id": SITIO + "/#centro",
        "name": "Prevención Siglo 21 — Centro de formación",
        "legalName": CENTRO["empresa"],
        "url": SITIO,
        "telephone": [TEL_E164[t] for t in CENTRO["telefonos"]],
        "email": CENTRO["correo"],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": CENTRO["direccion"],
            "postalCode": CENTRO["cp"],
            "addressLocality": CENTRO["ciudad"],
            "addressRegion": CENTRO["provincia"],
            "addressCountry": "ES",
        },
        "areaServed": {"@type": "AdministrativeArea", "name": "Comunidad de Madrid"},
        "identifier": [
            {"@type": "PropertyValue",
             "name": "Acreditación de la Comunidad de Madrid",
             "value": CENTRO["acreditacion_cm"]},
            {"@type": "PropertyValue",
             "name": "Homologación de la Fundación Laboral de la Construcción",
             "value": CENTRO["homologacion_flc"]},
        ],
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification",
             "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday"],
             "opens": "08:00", "closes": "18:00"},
            {"@type": "OpeningHoursSpecification",
             "dayOfWeek": "Friday", "opens": "08:00", "closes": "15:00"},
        ],
    }


def _curso_ld():
    """El Course. SIN `availability` ni fechas: no hay calendario publicado y
    Pedro prohíbe las urgencias y las plazas inventadas."""
    return {
        "@context": "https://schema.org",
        "@type": "Course",
        "@id": SITIO + "/#curso",
        "name": "Reciclaje de la formación en prevención del sector del metal (4 horas)",
        "description": ("Curso de reciclaje del sector del metal, 4 horas "
                        "presenciales en Móstoles (Madrid). Actualiza la "
                        "formación preventiva del oficio."),
        "url": SITIO + "/curso-reciclaje-metal-4-horas/",
        "inLanguage": "es",
        "teaches": [t for t, _d in ESQUEMA],
        "provider": {"@id": SITIO + "/#centro"},
        "offers": {
            "@type": "Offer",
            "price": str(CURSO["precio"]),
            "priceCurrency": "EUR",
            "category": "Formación",
            "url": SITIO + "/contacto/",
        },
        "hasCourseInstance": {
            "@type": "CourseInstance",
            "courseMode": "Onsite",
            "courseWorkload": "PT4H",
            "location": {
                "@type": "Place",
                "name": "Prevención Siglo 21 — Móstoles",
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": CENTRO["direccion"],
                    "postalCode": CENTRO["cp"],
                    "addressLocality": CENTRO["ciudad"],
                    "addressCountry": "ES",
                },
            },
        },
    }


def _migas(*pares):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n,
             "item": SITIO + u} for i, (n, u) in enumerate(pares)],
    }


def _migas_html(*pares):
    """Las migas que se VEN. Las de schema.org las lee Google; estas las lee
    quien entra por una página interior desde el buscador y no sabe dónde
    está."""
    trozos = []
    for i, (n, u) in enumerate(pares):
        if i == len(pares) - 1:
            trozos.append("<span>%s</span>" % n)
        else:
            trozos.append('<a href="%s">%s</a>' % (u, n))
    return ('<nav class="wrap" aria-label="Migas de pan" '
            'style="padding-top:14px;padding-bottom:0;font-size:.86rem;'
            'color:var(--tenue)">%s</nav>' % " › ".join(trozos))


# --- Las páginas -----------------------------------------------------------

def portada():
    cifras = [
        ("%d h" % CURSO["horas"], "de duración"),
        ("%d €" % CURSO["precio"], "el curso completo"),
        (len(OFICIOS), "reciclajes en el catálogo"),
        ("5 años", "lo que dura la tarjeta"),
    ]
    html_cifras = "".join(
        '<div class="linterna"><span class="cifra__n">%s</span>'
        '<span class="cifra__t">%s</span></div>'
        % (n, t) for n, t in cifras)

    incluye = "".join(
        '<li>%s<span><strong>%s</strong> %s</span></li>' % (_tic(), t, d)
        for t, d in INCLUYE)

    quien = "".join(
        '<article class="tarjeta linterna aparece" data-orden="%d">'
        '<span class="tarjeta__num">%d</span><h3>%s</h3><p>%s</p></article>'
        % (i, i + 1, t, d) for i, (t, d) in enumerate(PARA_QUIEN))

    pasos = [
        ("Nos dices tu oficio",
         "Por teléfono, por WhatsApp o dejando tus datos aquí. Con saber el "
         "oficio nos basta para decirte cuál es tu reciclaje."),
        ("Te apuntamos y te damos fecha",
         "Los grupos se abren según la demanda. Te avisamos en cuanto haya "
         "uno que te encaje."),
        ("Vienes cuatro horas al aula",
         "En Móstoles, junto a la Plaza de Toros, con aparcamiento gratuito "
         "al lado. Solo tienes que traer el DNI o el NIE."),
        ("Te llevas el título",
         "Te lo entregamos al terminar. Es lo que le enseñas a tu empresa."),
    ]
    html_pasos = "".join(
        '<article class="tarjeta%s aparece" data-orden="%d">'
        '<span class="tarjeta__num">%d</span><h3>%s</h3><p>%s</p></article>'
        % (" tarjeta--acento" if i == 3 else "", i, i + 1, t, d)
        for i, (t, d) in enumerate(pasos))

    lista_oficios = "".join("<li>%s</li>" % o for o in OFICIOS)

    seis = "".join(
        '<details class="pregunta"><summary>%s</summary>'
        '<div class="pregunta__cuerpo"><p>%s</p></div></details>' % (p, r)
        for p, r in PREGUNTAS[:6])

    cuerpo = """
<section class="hero">
  <div class="wrap hero__in">
    <div class="hero__grid">
      <div>
        <span class="sello"><span class="sello__punto"></span>Sector del metal · 4 horas</span>
        <h1>El <em>reciclaje</em> del metal de 4 horas, en Madrid</h1>
        <p class="entradilla">La formación de actualización del sector del
        metal para quien trabaja en obras de construcción. Cuatro horas
        presenciales en nuestro centro de Móstoles, %(precio)d € y el título al
        terminar. Formación homologada.</p>
        %(botonera)s
      </div>

      <aside class="ficha ficha--luz linterna aparece" data-orden="1">
        <p class="rotulo">Precio cerrado</p>
        <div class="ficha__precio">
          <span class="ficha__euros">%(precio)d €</span>
          <span class="ficha__iva">el curso completo</span>
        </div>
        <p class="pista" style="color:var(--tenue);font-size:.9rem">Sin matrícula
        y sin extras. Lo que ves es lo que pagas.</p>
        <ul class="ficha__lista">%(incluye)s</ul>
      </aside>
    </div>
  </div>
</section>

<section class="cifras">
  <div class="wrap">
    <div class="cifras__grid">%(cifras)s</div>
  </div>
</section>

<section class="seccion seccion--crema">
  <div class="wrap">
    <div class="cabecera-seccion aparece">
      <p class="rotulo">Qué es</p>
      <h2>Qué es el reciclaje del metal y de dónde sale</h2>
      <p class="entradilla">El catálogo de formación del sector del metal
      tiene una sección propia, «Formación de Reciclaje», con
      <strong>quince cursos de cuatro horas</strong>, uno por familia de
      oficios. Están amparados por el <strong>Anexo IV</strong> del %(convenio)s.</p>
    </div>
    <div class="rejilla rejilla--2">
      <div class="aparece">
        <p>No es un curso nuevo ni un curso distinto del que hiciste: es la
        <strong>actualización</strong> de la formación preventiva de tu oficio.
        Por eso dura cuatro horas y no veinte.</p>
        <p>La formación del metal es <strong>obligatoria para los trabajadores
        de las empresas del ámbito del Acuerdo Estatal del Sector del Metal que
        realizan sus trabajos en obras de construcción</strong>. Si tu empresa
        es del metal y entras en obra, esto va contigo.</p>
        <p><a href="/curso-reciclaje-metal-4-horas/">Ver el curso al detalle</a>
        · <a href="/oficios/">los quince oficios</a> ·
        <a href="/tarjeta-profesional-metal/">la tarjeta del metal</a>.</p>
      </div>
      <div class="aviso aparece" data-orden="1">
        <p><strong>¿Cada cuánto hay que repetirlo?</strong> No te vamos a dar
        una cifra que no podamos respaldar: el portal oficial de la tarjeta no
        publica una periodicidad para el reciclaje del metal. Se hace
        <em>cuando tu empresa o la obra te lo pide</em>. Lo que sí tiene fecha
        es la tarjeta, que <strong>caduca a los cinco años de su
        emisión</strong>.</p>
      </div>
    </div>
  </div>
</section>

<section class="seccion seccion--papel">
  <div class="wrap">
    <div class="cabecera-seccion aparece">
      <p class="rotulo">Para quién</p>
      <h2>Quién hace este curso</h2>
    </div>
    <div class="rejilla rejilla--4">%(quien)s</div>
  </div>
</section>

<section class="seccion seccion--menta">
  <div class="wrap">
    <div class="cabecera-seccion aparece">
      <p class="rotulo">Cómo va</p>
      <h2>De la primera llamada al título, en cuatro pasos</h2>
    </div>
    <div class="rejilla rejilla--4">%(pasos)s</div>
  </div>
</section>

<section class="seccion seccion--papel">
  <div class="wrap">
    <div class="cabecera-seccion aparece">
      <p class="rotulo">Los oficios</p>
      <h2>Los quince reciclajes del catálogo del metal</h2>
      <p class="entradilla">Todos de cuatro horas. Dinos el tuyo y te
      confirmamos cuál te toca.</p>
    </div>
    <article class="bloque aparece">
      <div class="bloque__cab"><span class="bloque__n">15</span>
      <h3>Formación de Reciclaje, Anexo IV</h3></div>
      <ul>%(lista_oficios)s</ul>
    </article>
    <div class="botonera">
      <a class="btn btn--linea" href="/oficios/">Ver los temarios</a>
    </div>
  </div>
</section>

<section class="seccion seccion--crema">
  <div class="wrap">
    <div class="cabecera-seccion aparece">
      <p class="rotulo">Dudas</p>
      <h2>Lo que más nos preguntan</h2>
    </div>
    %(seis)s
    <div class="botonera">
      <a class="btn btn--linea" href="/preguntas-frecuentes/">Todas las preguntas</a>
    </div>
  </div>
</section>
%(formulario)s""" % {
        "botonera": _botonera(), "precio": CURSO["precio"], "incluye": incluye,
        "cifras": html_cifras, "quien": quien, "pasos": html_pasos,
        "convenio": CONVENIO, "lista_oficios": lista_oficios,
        "seis": seis,
        "formulario": _formulario(ruta="/")}

    return cuerpo, _ld(_centro_ld(), _curso_ld())


def curso():
    incluye = "".join(
        '<li>%s<span><strong>%s</strong> %s</span></li>' % (_tic(), t, d)
        for t, d in INCLUYE)

    esquema = "".join(
        '<article class="tarjeta aparece" data-orden="%d">'
        '<span class="tarjeta__num">%d</span><h3>%s</h3><p>%s</p></article>'
        % (i, i + 1, t, d) for i, (t, d) in enumerate(ESQUEMA))

    cuerpo = """
<section class="seccion seccion--crema">
  %(migas)s
  <div class="wrap">
    <div class="cabecera-seccion">
      <span class="sello"><span class="sello__punto"></span>4 horas · %(precio)d €</span>
      <h1 style="margin-top:.5em">Curso de reciclaje del sector del metal, 4 horas</h1>
      <p class="entradilla">Cuatro horas presenciales en Móstoles para
      actualizar la formación preventiva de tu oficio del metal. Formación
      homologada, título al terminar y %(precio)d € sin extras.</p>
      %(botonera)s
    </div>
  </div>
</section>

<section class="seccion seccion--papel">
  <div class="wrap">
    <div class="rejilla rejilla--2">
      <div class="aparece">
        <h2>Para qué sirve</h2>
        <p>El catálogo de formación del sector del metal tiene una sección
        llamada <strong>«Formación de Reciclaje»</strong> con quince cursos de
        cuatro horas, uno por familia de oficios, amparados por el
        <strong>Anexo IV</strong> del %(convenio)s.</p>
        <p>Sirven para <strong>actualizar</strong> la formación preventiva que
        ya hiciste, no para sustituirla. Por eso son de cuatro horas: parten de
        que tu oficio ya lo conoces y repasan lo que más cambia —los riesgos
        del puesto, los medios de protección y los equipos.</p>
        <p>La formación del metal es obligatoria para los trabajadores de
        empresas del ámbito del <strong>Acuerdo Estatal del Sector del
        Metal</strong> que realizan sus trabajos en obras de construcción.</p>
        <p>Si lo que buscas es la tarjeta y no el reciclaje, lo explicamos en
        <a href="/tarjeta-profesional-metal/">la página de la tarjeta del
        metal</a>.</p>
      </div>
      <div class="ficha aparece" data-orden="1">
        <p class="rotulo">Qué incluye</p>
        <ul class="ficha__lista">%(incluye)s</ul>
      </div>
    </div>
  </div>
</section>

<section class="seccion seccion--menta">
  <div class="wrap">
    <div class="cabecera-seccion aparece">
      <p class="rotulo">Contenido</p>
      <h2>Qué se ve en las cuatro horas</h2>
      <p class="entradilla">Cada oficio tiene su propio temario oficial, pero
      los cuatro apartados de abajo son el <strong>esquema</strong> que
      comparten. El temario literal de administrativos, ferrallado y
      electricidad está en <a href="/oficios/">la página de oficios</a>.</p>
    </div>
    <div class="rejilla rejilla--4">%(esquema)s</div>
    <div class="aviso aparece" data-orden="4">
      <p><strong>Esto es un esquema, no el temario de tu oficio.</strong> De
      los quince reciclajes solo publicamos el contenido literal de tres,
      porque son los tres que tenemos por escrito. Si necesitas el temario
      exacto del tuyo, pídenoslo y te lo pasamos antes de matricularte.</p>
    </div>
  </div>
</section>

<section class="seccion seccion--papel">
  <div class="wrap">
    <div class="cabecera-seccion aparece">
      <p class="rotulo">Condiciones</p>
      <h2>Lo que hay que saber antes de venir</h2>
    </div>
    <div class="rejilla rejilla--3">
      <article class="tarjeta aparece"><span class="icono">%(ic)s</span>
        <h3>Qué llevar</h3><p>Solo el DNI o el NIE. Todo el material lo pone el
        centro: no tienes que comprar nada.</p></article>
      <article class="tarjeta aparece" data-orden="1"><span class="icono">%(ic)s</span>
        <h3>Edad</h3><p>18 años cumplidos.</p></article>
      <article class="tarjeta aparece" data-orden="2"><span class="icono">%(ic)s</span>
        <h3>Puntualidad</h3><p>Hay 30 minutos de margen. Pasados, ya no se
        puede entrar: el curso tiene que cumplir sus cuatro horas.</p></article>
    </div>
    <div class="aviso aparece" data-orden="3">
      <p><strong>Las fechas se abren según la demanda.</strong> No publicamos un
      calendario fijo porque nos parece peor: preferimos apuntar lo que
      necesitas y avisarte cuando salga grupo. Con un grupo de empresa se abre
      convocatoria propia.</p>
    </div>
    <div class="aviso aparece" data-orden="4">
      <p><strong>Sobre FUNDAE, con claridad:</strong> el curso es bonificable,
      pero <em>la gestión no la hacemos nosotros</em>. Hay que tramitarla con una
      entidad organizadora externa. Y si eres autónomo, no tienes crédito de
      formación. Preferimos decírtelo antes que después.</p>
    </div>
    <div class="aviso aparece" data-orden="5">
      <p><strong>Si pierdes el título</strong>, el duplicado cuesta 10 €.</p>
    </div>
  </div>
</section>
%(formulario)s""" % {
        "migas": _migas_html(("Inicio", "/"),
                             ("El curso de 4 horas", "/curso-reciclaje-metal-4-horas/")),
        "botonera": _botonera(), "incluye": incluye, "ic": _tic(),
        "precio": CURSO["precio"], "convenio": CONVENIO, "esquema": esquema,
        "formulario": _formulario("Pide fecha para el reciclaje",
                                  ruta="/curso-reciclaje-metal-4-horas/")}

    return cuerpo, _ld(_curso_ld(),
                       _migas(("Inicio", "/"),
                              ("El curso de 4 horas", "/curso-reciclaje-metal-4-horas/")))


def oficios():
    lista = "".join(
        '<li>%s%s</li>'
        % (o, ' <strong>· temario abajo</strong>'
           if o.split(" (")[0] in ("Administrativos", "Ferrallado")
           or o.startswith("Electricidad") else "")
        for o in OFICIOS)

    bloques = "".join(
        '<article class="bloque aparece" id="%s" data-orden="%d">'
        '<div class="bloque__cab"><span class="bloque__n">%d</span><h3>%s</h3></div>'
        '<ul>%s</ul></article>'
        % (ancla, i, i + 1, t, "".join("<li>%s</li>" % x for x in puntos))
        for i, (t, ancla, puntos) in enumerate(TEMARIOS))

    esquema = "".join(
        '<article class="tarjeta aparece" data-orden="%d">'
        '<span class="tarjeta__num">%d</span><h3>%s</h3><p>%s</p></article>'
        % (i, i + 1, t, d) for i, (t, d) in enumerate(ESQUEMA))

    cuerpo = """
<section class="seccion seccion--crema">
  %(migas)s
  <div class="wrap">
    <div class="cabecera-seccion">
      <p class="rotulo">Oficios</p>
      <h1>Los 15 cursos de reciclaje del metal, oficio por oficio</h1>
      <p class="entradilla">La sección «Formación de Reciclaje» del catálogo
      del sector del metal tiene quince cursos, todos de cuatro horas, uno por
      familia de oficios. Están amparados por el <strong>Anexo IV</strong> del
      %(convenio)s.</p>
    </div>
  </div>
</section>

<section class="seccion seccion--papel">
  <div class="wrap">
    <article class="bloque aparece">
      <div class="bloque__cab"><span class="bloque__n">15</span>
      <h3>Formación de Reciclaje · 4 horas cada uno</h3></div>
      <ul>%(lista)s</ul>
    </article>
    <div class="aviso aparece" data-orden="1">
      <p><strong>Si no sabes cuál es el tuyo, no lo adivines.</strong>
      Llámanos al %(tel)s y te lo decimos en un minuto con lo que ponga tu
      contrato o lo que te haya dicho la obra. Hacer el curso equivocado cuesta
      dinero y tiempo.</p>
    </div>
  </div>
</section>

<section class="seccion seccion--menta">
  <div class="wrap">
    <div class="cabecera-seccion aparece">
      <p class="rotulo">Temarios</p>
      <h2>Los tres temarios que tenemos por escrito</h2>
      <p class="entradilla">Estos tres son el contenido oficial, tal cual. De
      los otros doce no publicamos temario: preferimos no publicarlo a
      publicarlo mal.</p>
    </div>
    <div class="temario-2">%(bloques)s</div>
  </div>
</section>

<section class="seccion seccion--papel">
  <div class="wrap">
    <div class="cabecera-seccion aparece">
      <p class="rotulo">El resto</p>
      <h2>El esquema que comparten los doce restantes</h2>
      <p class="entradilla">Los tres temarios de arriba siguen el mismo patrón,
      y es el patrón de la sección entera: primero se delimita el oficio y
      después se ven sus técnicas preventivas. Esto es ese esquema.</p>
    </div>
    <div class="rejilla rejilla--4">%(esquema)s</div>
    <div class="aviso aparece" data-orden="4">
      <p><strong>Un esquema no es un temario.</strong> Cada uno de los quince
      reciclajes tiene el suyo, con sus riesgos y sus equipos. Si necesitas el
      contenido exacto del tuyo por escrito, pídenoslo y te lo pasamos antes de
      que te matricules: <a href="/contacto/">déjanos tus datos</a> o llama al
      %(tel)s.</p>
    </div>
    %(botonera)s
  </div>
</section>
%(formulario)s""" % {
        "migas": _migas_html(("Inicio", "/"), ("Oficios", "/oficios/")),
        "convenio": CONVENIO, "lista": lista, "bloques": bloques,
        "esquema": esquema, "tel": TEL1, "botonera": _botonera(),
        "formulario": _formulario("Dinos tu oficio y te damos fecha",
                                  ruta="/oficios/")}

    return cuerpo, _ld(_migas(("Inicio", "/"), ("Oficios", "/oficios/")))


def tarjeta():
    cuerpo = """
<section class="seccion seccion--crema">
  %(migas)s
  <div class="wrap">
    <div class="cabecera-seccion">
      <p class="rotulo">La tarjeta</p>
      <h1>La Tarjeta Profesional de la Construcción del sector del metal</h1>
      <p class="entradilla">Qué es, quién la emite, quién está obligado a la
      formación, cuándo caduca y cómo se renueva. Sin rodeos y sin nada que no
      podamos respaldar.</p>
    </div>
  </div>
</section>

<section class="seccion seccion--papel">
  <div class="wrap">
    <div class="rejilla rejilla--2">
      <div class="aparece">
        <h2>Quién la emite</h2>
        <p>La Tarjeta Profesional de la Construcción para el sector del metal
        la emite la <strong>Fundación del Metal para la Formación,
        Cualificación y el Empleo (FMF)</strong>, según el <strong>IV Convenio
        Estatal del Sector del Metal</strong>.</p>
        <p>No la emite el centro de formación. Nosotros damos la formación; la
        tarjeta se solicita a la FMF.</p>

        <h2>Quién está obligado</h2>
        <p>La formación del metal es obligatoria para los trabajadores de las
        empresas del <strong>ámbito del Acuerdo Estatal del Sector del
        Metal</strong> que realizan sus trabajos en <strong>obras de
        construcción</strong>.</p>
      </div>

      <div class="ficha aparece" data-orden="1">
        <p class="rotulo">Dónde se tramita</p>
        <p><strong>Fundación del Metal para la Formación, Cualificación y el
        Empleo</strong></p>
        <p>C/ Rivas 25<br>Polígono Industrial Vicálvaro<br>28052 Madrid</p>
        <p>Teléfono: <a href="tel:+34911770131">911 77 01 31</a></p>
        <p>El portal oficial de la tarjeta tiene además un teléfono gratuito:
        <a href="tel:+34900112121">900 11 21 21</a>.</p>
      </div>
    </div>
  </div>
</section>

<section class="seccion seccion--menta">
  <div class="wrap">
    <div class="cabecera-seccion aparece">
      <p class="rotulo">Caducidad</p>
      <h2>La tarjeta caduca a los cinco años</h2>
    </div>
    <div class="rejilla rejilla--2">
      <div class="aparece">
        <p>La tarjeta <strong>caduca a los cinco años de su emisión</strong>.
        Lo dice el artículo 5 de su reglamento. Y se renueva
        <strong>por el mismo procedimiento que la solicitud inicial</strong>:
        no hay un trámite abreviado distinto.</p>
        <p>Mira la fecha de emisión de la tuya. Es el único plazo de esta
        página que tiene un número detrás.</p>
      </div>
      <div class="aviso aparece" data-orden="1">
        <p><strong>Ojo: la caducidad de la tarjeta y el reciclaje no son lo
        mismo.</strong> El reciclaje de cuatro horas se hace cuando tu empresa
        o la obra te lo piden. No publicamos cada cuánto hay que repetirlo
        porque el portal oficial no lo dice, y preferimos decirte que no lo
        sabemos antes que darte una fecha equivocada.</p>
      </div>
    </div>
  </div>
</section>

<section class="seccion seccion--papel">
  <div class="wrap">
    <div class="cabecera-seccion aparece">
      <p class="rotulo">La formación</p>
      <h2>Qué formación pide la tarjeta del metal</h2>
      <p class="entradilla">Para obtener la tarjeta se exige al menos una
      acción formativa de <strong>8 horas o más</strong>. Un curso de cuatro
      horas, por sí solo, no da la tarjeta: es formación de actualización.</p>
    </div>
    <div class="tabla-envoltorio">
      <table>
        <thead><tr><th>Formación del catálogo del metal</th><th>Duración</th></tr></thead>
        <tbody>
          <tr><td>Nivel inicial</td><td>8 horas</td></tr>
          <tr><td>Nivel básico de prevención</td><td>60 horas</td></tr>
          <tr><td>Cursos de oficio (son 12)</td><td>20 horas cada uno</td></tr>
          <tr><td>Formación polivalente</td><td>6 horas</td></tr>
          <tr><td><strong>Formación de reciclaje (son 15)</strong></td>
              <td><strong>4 horas cada uno</strong></td></tr>
        </tbody>
      </table>
    </div>
    <div class="aviso aparece">
      <p><strong>La polivalente de 6 horas tiene condición previa.</strong>
      Para hacerla hay que haber hecho antes el curso de 20 horas de un oficio,
      el nivel básico del artículo 145, o la convalidación de la parte común de
      14 horas del anexo XIII.</p>
    </div>
    <div class="aviso aparece" data-orden="1">
      <p>Nosotros impartimos el <strong>reciclaje de 4 horas</strong>. Si lo
      que necesitas es otra de estas formaciones, llámanos al %(tel)s y te
      decimos si la damos o dónde mirarla. En
      <a href="https://www.tpcmetal.es/" rel="noopener">tpcmetal.es</a> tienes el
      resto de la formación del metal del centro, y en
      <a href="https://www.prevencionmadrid.es/tarjeta-profesional-de-la-construcci%C3%B3n-tpc/"
      rel="noopener">prevencionmadrid.es</a>, toda su oferta de prevención de
      riesgos laborales.</p>
      <p>Y si lo que te toca es la <strong>construcción</strong> y no el metal,
      la renovación de esa tarjeta se explica entera en
      <a href="https://renovartpc.es/renovar-la-tpc/" rel="noopener">renovartpc.es</a>:
      son dos convenios distintos y se confunden mucho.</p>
    </div>
    %(botonera)s
  </div>
</section>
%(formulario)s""" % {
        "migas": _migas_html(("Inicio", "/"),
                             ("La tarjeta del metal", "/tarjeta-profesional-metal/")),
        "tel": TEL1, "botonera": _botonera(),
        "formulario": _formulario("¿Dudas con tu tarjeta? Pregúntanos",
                                  ruta="/tarjeta-profesional-metal/")}

    return cuerpo, _ld(_migas(("Inicio", "/"),
                              ("La tarjeta del metal", "/tarjeta-profesional-metal/")))


def preguntas():
    todas = "".join(
        '<details class="pregunta"><summary>%s</summary>'
        '<div class="pregunta__cuerpo"><p>%s</p></div></details>' % (p, r)
        for p, r in PREGUNTAS)

    faq_ld = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": p,
             "acceptedAnswer": {"@type": "Answer", "text": r}}
            for p, r in PREGUNTAS],
    }

    cuerpo = """
<section class="seccion seccion--crema">
  %(migas)s
  <div class="wrap">
    <div class="cabecera-seccion">
      <p class="rotulo">Preguntas frecuentes</p>
      <h1>Todo lo que nos preguntáis del reciclaje del metal</h1>
      <p class="entradilla">Si tu duda no está aquí, llámanos al %(tel)s. No
      hace falta que te registres en nada para preguntar.</p>
    </div>
  </div>
</section>

<section class="seccion seccion--papel">
  <div class="wrap">
    %(todas)s
    <div class="aviso">
      <p>Más a fondo: <a href="/curso-reciclaje-metal-4-horas/">el curso de 4
      horas</a>, <a href="/oficios/">los quince oficios y sus temarios</a> y
      <a href="/tarjeta-profesional-metal/">la tarjeta del metal</a>.</p>
    </div>
    %(botonera)s
  </div>
</section>
%(formulario)s""" % {
        "migas": _migas_html(("Inicio", "/"),
                             ("Preguntas frecuentes", "/preguntas-frecuentes/")),
        "tel": TEL1, "todas": todas, "botonera": _botonera(),
        "formulario": _formulario(ruta="/preguntas-frecuentes/")}

    return cuerpo, _ld(faq_ld, _migas(("Inicio", "/"),
                                      ("Preguntas frecuentes", "/preguntas-frecuentes/")))


def contacto():
    tels = "".join(
        '<li><a href="tel:%s">%s</a></li>' % (TEL_E164[t], t)
        for t in CENTRO["telefonos"])
    horario = "".join('<tr><td>%s</td><td>%s</td></tr>' % (d, h) for d, h in HORARIO)

    cuerpo = """
<section class="seccion seccion--crema">
  %(migas)s
  <div class="wrap">
    <div class="cabecera-seccion">
      <p class="rotulo">Contacto</p>
      <h1>Hablemos</h1>
      <p class="entradilla">Lo más rápido es llamar. Si prefieres, déjanos tus
      datos y te llamamos nosotros para darte fecha del reciclaje.</p>
    </div>
  </div>
</section>

<section class="seccion seccion--papel">
  <div class="wrap">
    <div class="rejilla rejilla--3">
      <article class="tarjeta aparece">
        <span class="icono">%(ic)s</span>
        <h3 style="text-align:center">Teléfonos</h3>
        <ul class="tels">%(tels)s</ul>
      </article>
      <article class="tarjeta aparece" data-orden="1">
        <span class="icono">%(ic)s</span>
        <h3>Dónde estamos</h3>
        <p><a class="direccion" href="%(mapa)s" rel="noopener">%(dir)s<br>
        %(cp)s %(ciudad)s (%(prov)s)</a><br><em>%(ref)s</em></p>
        <p style="font-size:.9rem;color:var(--tenue)">Hay aparcamiento gratuito al lado.</p>
      </article>
      <article class="tarjeta aparece" data-orden="2">
        <span class="icono">%(ic)s</span>
        <h3>Horario de oficina</h3>
        <table style="font-size:.92rem"><tbody>%(horario)s</tbody></table>
        <p style="font-size:.86rem;color:var(--tenue);margin-top:10px">%(nota)s</p>
      </article>
    </div>
    <div class="aviso">
      <p>El curso se da aquí mismo, en Móstoles. Son cuatro horas y solo tienes
      que traer el DNI o el NIE. Si tu duda es cuál de
      <a href="/oficios/">los quince reciclajes</a> te toca, dinos tu oficio y
      te lo decimos.</p>
    </div>
  </div>
</section>
%(formulario)s""" % {
        "migas": _migas_html(("Inicio", "/"), ("Contacto", "/contacto/")),
        "ic": _tic(), "tels": tels, "dir": CENTRO["direccion"], "cp": CENTRO["cp"],
        "ciudad": CENTRO["ciudad"], "prov": CENTRO["provincia"],
        "ref": CENTRO["referencia"], "mapa": MAPA, "horario": horario,
        "nota": HORARIO_NOTA,
        "formulario": _formulario("Déjanos tus datos y te llamamos",
                                  ruta="/contacto/")}

    return cuerpo, _ld(_centro_ld(), _migas(("Inicio", "/"), ("Contacto", "/contacto/")))


def gracias():
    """Va en noindex: si alguien llegara por Google dispararía una conversión
    falsa y ensuciaría la medición."""
    cuerpo = """
<section class="seccion seccion--crema">
  <div class="wrap" style="max-width:660px;text-align:center">
    <span class="sello" style="margin-bottom:1em"><span class="sello__punto"></span>Recibido</span>
    <h1>Gracias, ya lo tenemos</h1>
    <p class="entradilla" style="margin:0 auto 1.4em">Te llamamos nosotros. Si
    tienes prisa o prefieres resolverlo ahora, llamar es lo más rápido:
    normalmente se soluciona en la misma llamada.</p>
    <div class="botonera" style="justify-content:center">
      <a class="btn btn--cta" href="tel:%(tel_e)s">Llamar al %(tel)s</a>
      <a class="btn btn--linea" href="/">Volver al inicio</a>
    </div>
  </div>
</section>""" % {"tel": TEL1, "tel_e": TEL_E164[TEL1]}
    return cuerpo, ""


# --- Legales ---------------------------------------------------------------

def _legal(titulo, html):
    cuerpo = """
<section class="seccion seccion--crema">
  <div class="wrap" style="max-width:820px">
    <h1>%s</h1>
  </div>
</section>
<section class="seccion seccion--papel">
  <div class="wrap" style="max-width:820px">%s</div>
</section>""" % (titulo, html)
    return cuerpo, ""


def aviso_legal():
    return _legal("Aviso legal", """
<h2>Titular</h2>
<p><strong>%(empresa)s</strong><br>%(dir)s<br>%(cp)s %(ciudad)s (%(prov)s)<br>
Correo: <a href="mailto:%(correo)s">%(correo)s</a><br>
Teléfono: %(tel)s<br>
Acreditado por la Comunidad de Madrid: %(cm)s<br>
Homologado por la Fundación Laboral de la Construcción: %(flc)s</p>

<h2>Objeto</h2>
<p>Esta web informa sobre el curso de reciclaje de la formación en prevención
del sector del metal, de 4 horas, que imparte el centro. No es una plataforma
de venta: no se cobra nada a través de ella.</p>

<h2>Condiciones de uso</h2>
<p>El acceso a la web es libre y gratuito. Quien la usa se compromete a
hacerlo conforme a la ley y a no realizar actividades que puedan dañar o
sobrecargar los sistemas del titular.</p>

<h2>Contenidos</h2>
<p>El precio, la duración y las condiciones del curso son los vigentes en la
fecha de publicación y pueden cambiar. Ante cualquier duda, lo que vale es lo
que se confirme por teléfono o por escrito al matricularse.</p>

<p>Esta web no es el portal oficial de la Tarjeta Profesional de la
Construcción ni está gestionada por la Fundación del Metal para la Formación,
Cualificación y el Empleo. La información sobre el catálogo del sector del
metal y sobre la tarjeta se recoge aquí a título informativo; la fuente
oficial es el portal de la tarjeta y la propia Fundación.</p>

<h2>Propiedad intelectual</h2>
<p>Los textos y el diseño de esta web pertenecen al titular. Los contenidos
formativos del catálogo del sector del metal proceden del IV Convenio
colectivo estatal de la industria, las nuevas tecnologías y los servicios del
sector del metal.</p>

<h2>Responsabilidad</h2>
<p>El titular no se hace responsable de los daños derivados del uso de la web
ni de la indisponibilidad temporal por causas técnicas.</p>

<h2>Legislación y fuero</h2>
<p>Esta web se rige por la legislación española. Para cualquier controversia
serán competentes los juzgados y tribunales que correspondan conforme a
derecho.</p>""" % {
        "empresa": CENTRO["empresa"], "dir": CENTRO["direccion"],
        "cp": CENTRO["cp"], "ciudad": CENTRO["ciudad"], "prov": CENTRO["provincia"],
        "correo": CENTRO["correo"], "tel": TEL1,
        "cm": CENTRO["acreditacion_cm"],
        "flc": CENTRO["homologacion_flc"]})


def privacidad():
    return _legal("Política de privacidad", """
<h2>Quién trata tus datos</h2>
<p><strong>%(empresa)s</strong>, %(dir)s, %(cp)s %(ciudad)s (%(prov)s).
Correo de contacto: <a href="mailto:%(correo)s">%(correo)s</a>.</p>

<h2>Qué datos y para qué</h2>
<p>Solo los que nos das en el formulario o por teléfono: nombre, teléfono, y
si quieres, correo electrónico, tu oficio y lo que nos cuentes. Los usamos para
<strong>responderte y gestionar tu matrícula</strong>, y para nada más.</p>

<h2>Base legal</h2>
<p>Tu consentimiento, que das al marcar la casilla del formulario, y la
ejecución de la relación que se inicia si te matriculas.</p>

<h2>Cuánto tiempo</h2>
<p>Mientras dure la relación y, después, el tiempo que exijan las obligaciones
legales del centro. Si solo pediste información y no llegas a matricularte,
los datos se eliminan cuando dejan de ser necesarios.</p>

<h2>A quién se los damos</h2>
<p>A nadie, salvo obligación legal. No vendemos ni cedemos datos, ni te
apuntamos a ninguna lista de correo. Los formularios de esta web los recoge un
servicio propio del centro alojado en su propio servidor.</p>

<h2>Tus derechos</h2>
<p>Puedes pedirnos acceso a tus datos, su rectificación o su supresión, y
oponerte o limitar su tratamiento, escribiendo a
<a href="mailto:%(correo)s">%(correo)s</a>. También puedes reclamar ante la
Agencia Española de Protección de Datos (<a href="https://www.aepd.es"
rel="noopener">aepd.es</a>).</p>""" % {
        "empresa": CENTRO["empresa"], "dir": CENTRO["direccion"],
        "cp": CENTRO["cp"], "ciudad": CENTRO["ciudad"], "prov": CENTRO["provincia"],
        "correo": CENTRO["correo"]})


def cookies():
    return _legal("Política de cookies", """
<h2>Qué usamos</h2>
<p>Esta web no necesita cookies para funcionar. No hay carrito, ni cuenta de
usuario, ni nada que recordar entre páginas.</p>

<h2>Lo único que se guarda por defecto</h2>
<p>Cuando respondes al aviso de cookies, guardamos <em>tu respuesta</em> en el
propio navegador (no es una cookie, es almacenamiento local, y no viaja a
ningún sitio). Sirve para no volver a preguntarte en cada página. Caduca a los
24 meses.</p>

<h2>Cookies de medición</h2>
<p>Si las aceptas, cargamos las herramientas de medición de Google para saber
qué páginas sirven de algo y cuáles no. <strong>No se cargan si no las
aceptas</strong>, y hasta ese momento el consentimiento se declara denegado.</p>
<p>Rechazarlas no limita nada: la web funciona exactamente igual.</p>

<h2>Cambiar de opinión</h2>
<p>Cuando quieras, desde el enlace <strong>«Cambiar cookies»</strong> del pie
de esta página.</p>

<h2>Cómo borrarlas desde el navegador</h2>
<p>Todos los navegadores permiten ver y borrar las cookies y el almacenamiento
de un sitio desde sus ajustes de privacidad.</p>""")


# --- El índice de páginas --------------------------------------------------
# (url, título, descripción, función, robots)

TODAS = [
    ("/",
     "Reciclaje del metal 4 horas en Madrid | 70 € · Móstoles",
     "Curso de reciclaje de la formación del sector del metal, 4 horas "
     "presenciales en Móstoles (Madrid). 70 € con material y título. Grupos "
     "según demanda.",
     portada, None),

    ("/curso-reciclaje-metal-4-horas/",
     "Curso de reciclaje del metal de 4 horas | 70 € en Móstoles",
     "Qué es el reciclaje del metal de 4 horas, para qué sirve, qué entra en "
     "las cuatro horas y qué hay que llevar. Presencial en Móstoles, Madrid, "
     "por 70 €.",
     curso, None),

    ("/oficios/",
     "Los 15 cursos de reciclaje del metal, oficio por oficio",
     "Los quince reciclajes de 4 horas del catálogo del metal, con el temario "
     "oficial de administrativos, ferrallado y electricidad de alta y baja "
     "tensión.",
     oficios, None),

    ("/tarjeta-profesional-metal/",
     "Tarjeta profesional del metal: quién la emite y cuándo caduca",
     "La TPC del sector del metal la emite la Fundación del Metal (FMF) y "
     "caduca a los cinco años. Quién está obligado, qué formación pide y cómo "
     "se renueva.",
     tarjeta, None),

    ("/preguntas-frecuentes/",
     "Preguntas frecuentes del reciclaje del metal de 4 horas",
     "Precio, duración, quién tiene que hacerlo, qué llevar, FUNDAE, tarjeta y "
     "caducidad: las dudas que más nos preguntan sobre el reciclaje del "
     "metal.",
     preguntas, None),

    ("/contacto/",
     "Contacto | Reciclaje del metal de 4 horas en Móstoles",
     "Teléfonos, dirección y horario del centro en Móstoles (Madrid). Déjanos "
     "tus datos y te llamamos para darte fecha del reciclaje del metal.",
     contacto, None),

    ("/gracias/",
     "Gracias | reciclajemetal.es",
     "Hemos recibido tus datos.",
     gracias, "noindex, nofollow"),

    ("/aviso-legal/", "Aviso legal | reciclajemetal.es",
     "Titular de reciclajemetal.es, objeto de la web, condiciones de uso, "
     "propiedad intelectual, responsabilidad y legislación aplicable al curso "
     "de reciclaje del metal.", aviso_legal, None),

    ("/politica-de-privacidad/", "Política de privacidad | reciclajemetal.es",
     "Qué datos tratamos cuando nos escribes o nos llamas, para qué los "
     "usamos, cuánto los guardamos y cuáles son tus derechos.", privacidad, None),

    ("/politica-de-cookies/", "Política de cookies | reciclajemetal.es",
     "Qué cookies usa esta web, qué se guarda si no aceptas nada y cómo "
     "rechazarlas o cambiar de opinión cuando quieras.",
     cookies, None),
]


# --- El fichero para los buscadores con IA ---------------------------------

def llms():
    """llms.txt: lo que una IA necesita saber de esta web, en llano y sin tener
    que interpretar el HTML. Es lo que hace que respondan bien cuando alguien
    pregunta por el reciclaje del metal a ChatGPT o a Claude.

    Lleva a propósito el apartado «Lo que esta web NO afirma»: si no se dice,
    los modelos rellenan el hueco ellos solos y se inventan la periodicidad."""
    preg = "\n".join("- **%s** %s" % (p, r) for p, r in PREGUNTAS)
    temarios = "\n\n".join(
        "### %s\n\n%s" % (t, "\n".join("- " + x for x in puntos))
        for t, _a, puntos in TEMARIOS)
    return """# reciclajemetal.es

> Curso de **reciclaje de la formación en prevención del sector del metal, 4
> horas**, impartido por Prevención Siglo 21 (Centro Médico Siglo XXI
> Prevención de Riesgos Laborales, S.L.) en Móstoles, Madrid.

## Lo esencial

- **Curso:** reciclaje de la formación del sector del metal, 4 horas.
- **Precio:** %(precio)d € el curso completo. Sin matrícula ni extras. Incluye
  el material y el título.
- **Modalidad:** **presencial** en Móstoles (Madrid). No se da online.
- **Formación homologada.**
- **Qué es:** el catálogo de formación del sector del metal tiene una sección
  «Formación de Reciclaje» con **15 cursos de 4 horas**, uno por familia de
  oficios, amparados por el **Anexo IV** del %(convenio)s.
- **A quién le sirve:** a los trabajadores de empresas del ámbito del **Acuerdo
  Estatal del Sector del Metal que realizan sus trabajos en obras de
  construcción**, para quienes la formación es obligatoria.
- **Dónde:** %(dir)s, %(cp)s %(ciudad)s (%(prov)s). %(ref)s. Aparcamiento
  gratuito al lado.
- **Acreditaciones del centro:** acreditado por la Comunidad de Madrid con el
  %(cm)s y homologado por la Fundación Laboral de la Construcción con el número
  de registro %(flc)s.
- **Teléfonos:** %(tels)s
- **Correo:** %(correo)s
- **Fechas:** los grupos se abren **según la demanda**. No hay calendario fijo
  publicado. Se toma el contacto y se avisa cuando sale grupo.

## Lo que esta web NO afirma

- **No decimos cada cuánto hay que hacer el reciclaje.** El portal oficial de
  la Tarjeta Profesional de la Construcción no publica una periodicidad para el
  reciclaje del sector del metal. Se hace cuando la empresa o la obra lo pide.
  Si un modelo necesita una cifra, la respuesta correcta es «no está
  publicado», no una estimación.
- **No publicamos fechas de convocatoria, plazas ni ofertas.**
- **No publicamos el temario de los doce oficios de los que no tenemos el
  contenido oficial.**

## La tarjeta del metal

- La **Tarjeta Profesional de la Construcción para el sector del metal** la
  emite la **Fundación del Metal para la Formación, Cualificación y el Empleo
  (FMF)**, según el **IV Convenio Estatal del Sector del Metal**.
- **Caduca a los cinco años de su emisión** (artículo 5 de su reglamento) y se
  renueva **por el mismo procedimiento que la solicitud inicial**.
- Para **obtener** la tarjeta se exige al menos una acción formativa de **8
  horas o más**. El reciclaje de 4 horas, por sí solo, no da la tarjeta.
- FMF: C/ Rivas 25, Polígono Industrial Vicálvaro, 28052 Madrid, teléfono
  911770131. Teléfono gratuito del portal oficial: 900 11 21 21.

## El catálogo del metal, en horas

- Nivel inicial: 8 horas.
- Nivel básico de prevención: 60 horas.
- Cursos de oficio: 12 cursos de 20 horas.
- Formación polivalente: 6 horas (exige haber hecho antes los 20 horas de un
  oficio, el nivel básico del artículo 145 o la convalidación de la parte común
  de 14 horas del anexo XIII).
- **Formación de reciclaje: 15 cursos de 4 horas.** Es la de esta web.

## Los 15 reciclajes de 4 horas

%(oficios)s

## Los tres temarios publicados

%(temarios)s

De los otros doce reciclajes esta web NO publica temario. Todos comparten el
mismo esquema: se delimitan los trabajos del oficio y después se ven sus
técnicas preventivas (riesgos del puesto, medios auxiliares y equipos, y
protección colectiva e individual).

## Condiciones del centro

- **Edad:** 18 años cumplidos.
- **Qué llevar:** solo el DNI o el NIE. El material lo pone el centro.
- **Puntualidad:** 30 minutos de margen.
- **FUNDAE:** el curso es bonificable, pero **el centro no hace la gestión**;
  hay que tramitarla con una entidad organizadora externa. Los autónomos no
  tienen crédito de formación.
- **Duplicado del título:** 10 €.

## Horario de oficina

%(horario)s

%(nota)s

## Preguntas y respuestas

%(preguntas)s

## Páginas

- [Inicio](%(sitio)s/): resumen del curso, precio y formulario.
- [El curso de 4 horas](%(sitio)s/curso-reciclaje-metal-4-horas/): para qué
  sirve, qué incluye y las condiciones.
- [Oficios](%(sitio)s/oficios/): los 15 reciclajes y los tres temarios.
- [La tarjeta del metal](%(sitio)s/tarjeta-profesional-metal/): quién la emite,
  obligatoriedad, caducidad y renovación.
- [Preguntas frecuentes](%(sitio)s/preguntas-frecuentes/)
- [Contacto](%(sitio)s/contacto/)

## Otras webs del mismo centro

- [tpcmetal.es](https://tpcmetal.es): el resto de la formación del sector del
  metal del centro.
- [prevencionmadrid.es](https://prevencionmadrid.es): toda su oferta de
  prevención de riesgos laborales.
""" % {
        "precio": CURSO["precio"], "convenio": CONVENIO,
        "dir": CENTRO["direccion"], "cp": CENTRO["cp"],
        "ciudad": CENTRO["ciudad"], "prov": CENTRO["provincia"],
        "ref": CENTRO["referencia"],
        "cm": CENTRO["acreditacion_cm"],
        "flc": CENTRO["homologacion_flc"],
        "tels": ", ".join(CENTRO["telefonos"]),
        "correo": CENTRO["correo"],
        "oficios": "\n".join("- " + o for o in OFICIOS),
        "temarios": temarios,
        "horario": "\n".join("- %s: %s" % (d, h) for d, h in HORARIO),
        "nota": HORARIO_NOTA,
        "preguntas": preg, "sitio": SITIO}
