# CLAUDE.md — reciclajemetal.es

Web del centro de Pedro dedicada **solo** al curso de **reciclaje de la
formación en prevención del sector del METAL, 4 horas**. 70 €, presencial en
Móstoles, formación ya homologada. Estática, sin dependencias, generada con
Python.

    python _web/generar.py     # construye las 10 páginas
    python _web/auditar.py     # las audita en Chrome de verdad; sale 1 si falla

Es copia del andamiaje de `tpc60horas-web`: mismo `estilo.css`, mismo `web.js`,
mismo generador y misma auditoría. **El contenido es nuevo y no se parece al de
ninguna otra web del centro**, por la regla `no-duplicar-contenido-entre-webs`:
la hermana de construcción es `renovartpc.es` y si se copian textos compiten
entre ellas en Google. Por lo mismo, **todavía no hay enlaces a renovartpc.es**
(lo pidió Pedro).

## Lo que NO dice esta web, y es a propósito

**No dice cada cuánto hay que hacer el reciclaje.** Pedro dice «cada 4 años»,
pero el portal oficial de la TPC (trabajoenconstruccion.com) **no publica
ninguna periodicidad** para el reciclaje del metal. La web habla de «cuando tu
empresa o la obra te lo pida» y de que la **tarjeta caduca a los cinco años de
su emisión**, que eso sí tiene fuente (artículo 5 de su reglamento). Hay
`# PENDIENTE PEDRO: periodicidad del reciclaje` en:

- `_web/centro.py`, junto a `CURSO["renovacion_anios"]` — **ese campo existe
  pero NO se usa en ninguna página**. Es la trampa más fácil de pisar: alguien
  lo ve y lo pinta.
- `_web/paginas.py`, en la cabecera y en la función `tarjeta()`, sobre el
  párrafo exacto que habría que cambiar.

**No hay número de homologación de este curso.** Pedro dice que está
homologado y así se dice, con esas palabras. El número del pie (`0505101086`)
es la homologación del **centro** en la Fundación Laboral de la Construcción, y
`CM 87/2006` su acreditación en la Comunidad de Madrid. Son del centro, no de
este curso, y Pedro los quiere en todas sus webs.

**No hay fechas de convocatoria, ni plazas, ni ofertas, ni «últimas plazas».**
Prohibido por Pedro. Los grupos se abren según la demanda y así se cuenta.

**No hay temario de doce de los quince oficios.** Solo tenemos el contenido
oficial de **administrativos, ferrallado y electricidad de alta y baja
tensión**. De los otros doce se publica el **esquema** que comparten los tres,
dicho como esquema, y se invita a pedir el temario exacto. Inventarlo sería la
forma más rápida de que alguien venga con el curso equivocado.

**Contenedor de Tag Manager: GTM-56SQ9M6R** (lo creó Ana, de Dlega, el
23/09/2026; puesto el 24/09/2026 en `centro.py › GTM`, commit `dbf8cc6`). Va
como `data-gtm` en el `<html>` y `web.js` lo lee de ahí. Las etiquetas las pone
Ana; la propiedad de Analytics es **G-JWWXHLFPJV** (cuenta «Webs Pedro Rubio –
Siglo 21»). `_web/auditar.py` se pone rojo si alguien mete uno a mano
en el HTML o si la medición se carga sin consentimiento.

## Lo que sí está verificado

Todo lo del convenio sale del portal oficial de la TPC:

| | |
|---|---|
| Qué es | Sección **«Formación de Reciclaje»** del catálogo del metal: **15 cursos de 4 horas** |
| Amparo | **Anexo IV** del IV Convenio colectivo estatal de la industria, las nuevas tecnologías y los servicios del sector del metal |
| Quién está obligado | Trabajadores de empresas del ámbito del **Acuerdo Estatal del Sector del Metal** que trabajan en **obras de construcción** |
| Quién emite la tarjeta | **Fundación del Metal para la Formación, Cualificación y el Empleo (FMF)**, según el IV Convenio Estatal del Sector del Metal |
| Caducidad | **5 años** desde la emisión (art. 5 del reglamento). Se renueva por el **mismo procedimiento** que la solicitud inicial |
| Para obtener la tarjeta | Hace falta al menos una acción formativa de **8 horas o más**. El reciclaje de 4 h, solo, **no da la tarjeta** |
| Catálogo del metal | inicial 8 h · básico 60 h · 12 oficios de 20 h · polivalente 6 h (con requisito previo) · **15 reciclajes de 4 h** |
| FMF | C/ Rivas 25, P. I. Vicálvaro, 28052 Madrid · 911770131. Portal oficial: 900 11 21 21 |

Y las reglas del centro, que las dictó Pedro:

| | |
|---|---|
| Precio | **70 €**, curso completo, con material y título |
| Modalidad | **Presencial** en Móstoles (Calle La Fragua 1) |
| Qué llevar | Solo DNI o NIE |
| Edad | 18 años cumplidos |
| Puntualidad | 30 minutos de margen |
| FUNDAE | Bonificable **sí**, pero **el centro no hace la gestión**: entidad organizadora externa. Autónomos, sin crédito |
| Duplicado del título | 10 € |
| Fechas | **Según la demanda.** No hay calendario fijo publicado, a propósito |

## Trampas de este repositorio

Son las mismas de `tpc60horas-web`, porque el andamiaje es el mismo. Las que
ya costaron un disgusto allí:

- **El minificador de CSS y el `:not()`.** Un `replace("not(", "not (")` a
  secas rompe `a:not(.btn)` y el navegador **tira la regla sin decir nada**.
  Por eso `generar.py` cuenta las llaves antes y después y se niega a generar
  si no cuadran.
- **Los degradados no se ven con `backgroundColor`.** Van en
  `background-image`; `auditar.py` saca los colores del degradado y se queda
  con el peor. Un arnés que solo mire lo primero da 1.00 y es mentira.
- **Los botones no pueden ser pastel.** Letra blanca a 17 px en negrita pide
  4,5:1. El pastel vive en los fondos, no en los botones.
- **Chrome headless en este PC no baja de ~500 px de ancho.** El corte de
  420 px **no se está probando**; lo que hay por debajo de 500 se mira a mano.

Y una propia de esta web:

- **Los nombres de los quince oficios son literales del catálogo.** Están en
  `OFICIOS` de `paginas.py` y de ahí salen la lista, el `<select>` del
  formulario y el `llms.txt`. No se acortan «para que quepan»: si alguien
  busca «instalaciones, reparaciones, montajes, estructuras metálicas» quiere
  encontrar eso exactamente.

## Estructura

    _web/centro.py     datos del centro y del curso (aquí se cambia todo)
    _web/paginas.py    el contenido, página a página, y los datos del convenio
    _web/generar.py    plantilla, minificado y montaje
    _web/auditar.py    la auditoría (fichero + Chrome)
    estilo.css         la hoja ORIGINAL; se edita aquí y se regenera
    web.js             cookies, consentimiento, formulario y entradas

La hoja va **incrustada y minificada** en cada página (bloquea el pintado) y el
guion va **aparte con `defer`** (no lo bloquea y se guarda una vez).

## El formulario

Va al servicio propio de Pedro: `formularios.tpcmetal.es/enviar/reciclajemetal`.

**SIN DAR DE ALTA EL SITIO EN EL SERVIDOR NO ENTREGA NADA.** Hace falta añadir
`reciclajemetal` a `/etc/formularios/config.json` del VPS. Es un paso de root.

Los campos son **siete y con inicial mayúscula**: `Nombre`, `Email`,
`Telefono`, `Curso`, `Mensaje`, `Acepto`, `Origen`. Con otro nombre no es que
lleguen mal: **no llegan**. El desplegable del oficio va dentro de `Curso`
porque es uno de esos siete.
