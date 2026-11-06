/* Botones Llamar y WhatsApp en el movil (Pedro 05/11/2026). El mismo fichero para todas las webs:
   el telefono sale de la tabla por dominio. Solo se ven por debajo de 820 px (botones-movil.css).
   v e/f (06/11/2026, Pedro con la propuesta de Ana/Dlega): en TODAS, botones redondos FLOTANTES abajo a la derecha,
   que siguen en pantalla al hacer scroll (antes habia barra abajo, botones en la portada o franja arriba).
   Si la web ya tiene su WhatsApp flotante (Joinchat en las de Ana; .wa-flotante, .wasap... en las nuestras) o su
   Llamar flotante al mismo numero, ese no se repite: se pinta solo lo que falte, encima de los suyos.
   formacion-online.es fuera: ya tiene su barra fija abajo con los dos telefonos y WhatsApp.
   Para quitarlo de una web: borrar su linea de la tabla (o el include de nginx / el plugin de WordPress). */
(function () {
  var WEBS = {
    'prevencionmadrid.es': '+34916170423',
    'curso-tpc.es': '+34630292516',
    'prevencionsiglo21.com': '+34916170423',
    'prevencionsiglo21.es': '+34916170423',
    'prevencion.com': '+34916170423',
    'seguridad-laboral.net': '+34916170423',
    'prevencion.cc': '+34916170423',
    'prevencion.online': '+34630292516',
    'prevencion-online.es': '+34916170423',
    'cursos-prevencion.net': '+34630292516',
    'prevencionderiesgoslaborales.org': '+34691101010',
    'prevencionderiesgoslaborales.info': '+34916170423',
    'prevencion-de-riesgos-laborales.net': '+34916170423',
    'cursoconstruccion.es': '+34916170423',
    'cursoconstruccion.com': '+34916170423',
    'formacionmadrid.es': '+34916170423',
    'tarjetaconstruccion.net': '+34916170423',
    'tarjetaprofesionaldelaconstruccion.online': '+34916170423',
    'tpcmetal.es': '+34630292516',
    'tpc20horas.es': '+34916170423',
    'tpc60horas.es': '+34916170423',
    'reciclajemetal.es': '+34916170423',
    'renovartpc.es': '+34916170423',
    'cursosconstruccion.es': '+34916170423',
    'tarjeta-tpc.es': '+34630292516'
  };
  var WA = 'https://wa.me/34630292516', MOVIL = '+34630292516';
  var tel = WEBS[location.hostname.replace(/^www\./, '')];
  if (!tel || document.getElementById('bm')) return;
  // Pedro 06/11: en todas tambien se puede llamar al 630 292 516 (si la web no lo tiene ya)
  var tels = tel === MOVIL ? [tel] : [tel, MOVIL];
  // lo que la web ya tiene flotando ABAJO (enlace fijo, o dentro de algo fijo a 1-2 niveles); la cabecera fija y lo escondido fuera de la pantalla no cuentan
  function fijo(e) { var r = e.getBoundingClientRect(); if (!r.height || r.top < innerHeight * 0.4 || r.top >= innerHeight) return false; for (var i = 0; e && e !== document.body && i < 3; i++, e = e.parentElement) if (getComputedStyle(e).position === 'fixed') return true; return false; }
  var suyos = [].filter.call(document.querySelectorAll('a[href*="wa.me"],a[href*="whatsapp.com"],a[href^="tel:"]'), fijo);
  var jc = document.querySelector('.joinchat'); // WhatsApp flotante del plugin Joinchat (aparece a los segundos)
  var hayWA = jc || suyos.some(function (a) { return /wa\.me|whatsapp/.test(a.href); });
  function nueve(t) { return t.replace(/\D/g, '').slice(-9); }
  tels = tels.filter(function (t) { return !suyos.some(function (a) { return /^tel:/.test(a.getAttribute('href')) && nueve(a.getAttribute('href')) === nueve(t); }); });
  if (!tels.length && hayWA) return;
  function bon(t) { return t.replace(/^\+34/, '').replace(/(\d{3})(\d{3})(\d{3})/, '$1 $2 $3'); }
  var iT = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M6.6 10.8a15.1 15.1 0 006.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 013 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z"/></svg>';
  var iW = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 00-8.6 15.1L2 22l5-1.3A10 10 0 1012 2zm0 18.2c-1.5 0-3-.4-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1112 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 01-3.3-2.9c-.2-.4.3-.4.8-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 00-.7.3 3 3 0 00-.9 2.2 5.2 5.2 0 001.1 2.8 11.9 11.9 0 004.6 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.1-1.2l-.4-.2z"/></svg>';
  var dos = tel !== MOVIL; // dos numeros en la web: cada Llamar lleva sus 3 primeras cifras
  var d = document.createElement('div');
  d.id = 'bm';
  d.className = 'bm-C' + (dos ? ' bm-2' : '') + (jc && /joinchat--left/.test(jc.className) ? ' bm-izq' : '');
  d.innerHTML = (hayWA ? '' : '<a class="bm-b bm-w" href="' + WA + '" target="_blank" rel="noopener" aria-label="WhatsApp 630 292 516">' + iW + '</a>') +
    tels.map(function (t) { return '<a class="bm-b bm-l" href="tel:' + t + '" aria-label="Llamar al ' + bon(t) + '">' + iT + (dos ? '<small>' + bon(t).slice(0, 3) + '</small>' : '') + '</a>'; }).join('');
  document.body.appendChild(d);
  document.documentElement.classList.add('bm-con-C');
  // Que no tapen el aviso de cookies ni lo fijo de abajo: se ponen encima de la franja de abajo mientras exista
  // (y de lo pequeño fijo que haya en su columna),
  // y encima del boton de Joinchat cuando este se ve (si aun no ha salido, se le deja su hueco).
  var movil = window.matchMedia('(max-width:820px)');
  function ajustar() {
    if (!movil.matches) return;
    var H = innerHeight, abajo = 0, cand = [], yo = d.getBoundingClientRect();
    [].forEach.call(document.body.children, function (e) { cand.push(e); [].push.apply(cand, e.children); });
    cand.forEach(function (e) {
      if (e === d || e.contains(d) || (jc && (e === jc || e.contains(jc)))) return;
      var s = getComputedStyle(e);
      if (s.position !== 'fixed' || s.display === 'none' || s.visibility === 'hidden') return;
      var r = e.getBoundingClientRect();
      if (r.height < 8 || r.width < 8 || r.top < H * 0.25) return;
      // franjas de abajo (cookies) y lo que caiga en nuestra columna (p. ej. el boton de «subir arriba»)
      if ((r.bottom > H - 10 && r.width > innerWidth * 0.6) || (r.bottom > H * 0.6 && r.left < yo.right && r.right > yo.left)) abajo = Math.max(abajo, H - r.top);
    });
    var base = abajo ? abajo + 12 : 18;
    if (jc) {
      var b = jc.querySelector('.joinchat__button'), rb = b && b.getBoundingClientRect();
      base = rb && rb.height ? Math.max(base, H - rb.top) + 12 : base + 72;
    }
    d.style.bottom = base + 'px';
  }
  ajustar();
  setInterval(ajustar, 800); // ponytail: sondeo cada 0,8 s (unos 50 elementos); MutationObserver si algun dia pesa
})();
