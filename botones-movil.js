/* Botones Llamar y WhatsApp en el movil (Pedro 05/11/2026). El mismo fichero para todas las webs:
   la opcion y el telefono salen de la tabla por dominio. Solo se ven por debajo de 820 px (botones-movil.css).
   A = barra fija abajo, B = botones en la portada (tras el h1), C = flotantes abajo a la derecha, D = franja fija arriba.
   Para quitarlo de una web: borrar su linea de la tabla (o el include de nginx / el plugin de WordPress). */
(function () {
  var WEBS = {
    'prevencionmadrid.es': ['C', '+34916170423'],
    'formacion-online.es': ['D', '+34630292516'],
    'curso-tpc.es': ['C', '+34630292516'],
    'prevencionsiglo21.com': ['B', '+34916170423'],
    'prevencionsiglo21.es': ['B', '+34916170423'],
    'prevencion.com': ['B', '+34916170423'],
    'seguridad-laboral.net': ['B', '+34916170423'],
    'prevencion.cc': ['B', '+34916170423'],
    'prevencion.online': ['B', '+34630292516'],
    'prevencion-online.es': ['B', '+34916170423'],
    'cursos-prevencion.net': ['B', '+34630292516'],
    'prevencionderiesgoslaborales.org': ['A', '+34691101010'],
    'prevencionderiesgoslaborales.info': ['A', '+34916170423'],
    'prevencion-de-riesgos-laborales.net': ['A', '+34916170423'],
    'cursoconstruccion.es': ['A', '+34916170423'],
    'cursoconstruccion.com': ['A', '+34916170423'],
    'formacionmadrid.es': ['A', '+34916170423'],
    'tarjetaconstruccion.net': ['A', '+34916170423'],
    'tarjetaprofesionaldelaconstruccion.online': ['A', '+34916170423'],
    'tpcmetal.es': ['A', '+34630292516'],
    'tpc20horas.es': ['A', '+34916170423'],
    'tpc60horas.es': ['A', '+34916170423'],
    'reciclajemetal.es': ['A', '+34916170423'],
    'renovartpc.es': ['A', '+34916170423'],
    'cursosconstruccion.es': ['A', '+34916170423'],
    'tarjeta-tpc.es': ['C', '+34630292516']
  };
  var WA = 'https://wa.me/34630292516';
  var web = WEBS[location.hostname.replace(/^www\./, '')];
  if (!web || document.getElementById('bm')) return;
  var op = web[0], tel = web[1];
  var bonito = tel.replace(/^\+34/, '').replace(/(\d{3})(\d{3})(\d{3})/, '$1 $2 $3');
  var iT = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M6.6 10.8a15.1 15.1 0 006.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 013 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z"/></svg>';
  var iW = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 00-8.6 15.1L2 22l5-1.3A10 10 0 1012 2zm0 18.2c-1.5 0-3-.4-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1112 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 01-3.3-2.9c-.2-.4.3-.4.8-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 00-.7.3 3 3 0 00-.9 2.2 5.2 5.2 0 001.1 2.8 11.9 11.9 0 004.6 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.1-1.2l-.4-.2z"/></svg>';
  var aT = '<a class="bm-b bm-l" href="tel:' + tel + '" aria-label="Llamar al ' + bonito + '">';
  var aW = '<a class="bm-b bm-w" href="' + WA + '" target="_blank" rel="noopener" aria-label="WhatsApp 630 292 516">';
  var d = document.createElement('div');
  d.id = 'bm';
  d.className = 'bm-' + op;
  if (op === 'A') d.innerHTML = aT + iT + '<span>Llamar<small>' + bonito + '</small></span></a>' + aW + iW + '<span>WhatsApp<small>Respuesta rápida</small></span></a>';
  else if (op === 'B') d.innerHTML = aT + iT + 'Llamar</a>' + aW + iW + 'WhatsApp</a><div class="bm-n">' + bonito + '</div>';
  else if (op === 'C') d.innerHTML = aW + iW + '</a>' + aT + iT + '</a>';
  else d.innerHTML = '<span class="bm-n">' + bonito + '</span>' + aT + iT + 'Llamar</a>' + aW + iW + 'WhatsApp</a>';
  if (op === 'B') {
    var h = [].filter.call(document.querySelectorAll('h1'), function (e) { var r = e.getBoundingClientRect(); return r.height > 0 && r.top < 700; })[0];
    if (h) h.insertAdjacentElement('afterend', d); else document.body.insertBefore(d, document.body.firstChild);
  } else document.body.appendChild(d);
  document.documentElement.classList.add('bm-con-' + op);
  // Que no tapen el aviso de cookies ni lo fijo de abajo de la web: con la barra (A) lo de abajo sube 64 px;
  // con los flotantes (C) los botones se ponen encima de la franja de abajo mientras exista.
  if (op !== 'A' && op !== 'C') return;
  var movil = window.matchMedia('(max-width:820px)');
  function ajustar() {
    if (!movil.matches) return;
    var H = innerHeight, abajo = 0, cand = [];
    [].forEach.call(document.body.children, function (e) { cand.push(e); [].push.apply(cand, e.children); });
    cand.forEach(function (e) {
      if (e === d || e.contains(d)) return;
      var s = getComputedStyle(e);
      if (s.position !== 'fixed' || s.display === 'none' || s.visibility === 'hidden') return;
      var r = e.getBoundingClientRect();
      if (r.height < 8 || r.width < 8 || r.top < H * 0.25) return;
      if (op === 'A' && r.bottom > H - 64 && !e.hasAttribute('data-bm-subido')) {
        e.setAttribute('data-bm-subido', '');
        e.style.setProperty('bottom', ((parseFloat(s.bottom) || 0) + 64) + 'px', 'important');
      }
      if (op === 'C' && r.bottom > H - 10 && r.width > innerWidth * 0.6) abajo = Math.max(abajo, H - r.top);
    });
    if (op === 'C') d.style.bottom = (abajo ? abajo + 12 : 18) + 'px';
  }
  ajustar();
  setInterval(ajustar, 800); // ponytail: sondeo cada 0,8 s (unos 50 elementos); MutationObserver si algun dia pesa
})();
