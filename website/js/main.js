/* BKM Mannesmann — progressive enhancement, keine Dependencies. */
(function () {
  "use strict";
  document.documentElement.classList.remove("no-js");

  /* ---------- Mobile Navigation ---------- */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("is-open")) {
        nav.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.focus();
      }
    });
  }

  /* ---------- Scroll-Reveals (einmalig, reduced-motion-sicher) ---------- */
  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var targets = document.querySelectorAll(".reveal, .reveal-group");
  if (reduced || !("IntersectionObserver" in window)) {
    targets.forEach(function (el) { el.classList.add("is-visible"); });
  } else if (targets.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -10% 0px", threshold: 0.1 });
    targets.forEach(function (el) { io.observe(el); });
  }

  /* ---------- Feuchte-Check ---------- */
  var check = document.getElementById("feuchte-check");
  if (check) initCheck(check);

  function initCheck(root) {
    var steps = Array.prototype.slice.call(root.querySelectorAll(".check-step"));
    var result = root.querySelector(".check-result");
    var bar = root.querySelector(".trocknungslinie .bar");
    var counter = root.querySelector("[data-step-counter]");
    var idx = 0;

    function show(i) {
      steps.forEach(function (s, n) { s.hidden = n !== i; });
      result.hidden = true;
      idx = i;
      if (bar) bar.style.width = ((i) / steps.length) * 100 + "%";
      if (counter) counter.textContent = "Frage " + (i + 1) + " von " + steps.length;
      var heading = steps[i].querySelector("h2");
      if (heading) heading.focus({ preventScroll: false });
    }

    function answered(step) {
      return step.querySelector("input:checked") !== null;
    }

    root.addEventListener("click", function (e) {
      var next = e.target.closest("[data-next]");
      var prev = e.target.closest("[data-prev]");
      var restart = e.target.closest("[data-restart]");
      if (next) {
        var step = steps[idx];
        var err = step.querySelector(".step-error");
        if (!answered(step)) {
          if (err) { err.hidden = false; }
          return;
        }
        if (err) err.hidden = true;
        if (idx + 1 < steps.length) { show(idx + 1); } else { finish(); }
      }
      if (prev && idx > 0) show(idx - 1);
      if (restart) {
        root.querySelectorAll("input").forEach(function (i) { i.checked = false; });
        show(0);
      }
    });

    function finish() {
      steps.forEach(function (s) { s.hidden = true; });
      if (bar) bar.style.width = "100%";
      if (counter) counter.textContent = "Ergebnis";
      var a = {};
      ["ort", "symptom", "dauer", "ausmass", "gebaeude"].forEach(function (k) {
        var el = root.querySelector('input[name="' + k + '"]:checked');
        a[k] = el ? el.value : "";
      });
      render(a);
      result.hidden = false;
      var h = result.querySelector("h2");
      if (h) h.focus();
    }

    function render(a) {
      var ursache = result.querySelector("[data-ursache]");
      var text = result.querySelector("[data-erklaerung]");
      var empf = result.querySelector("[data-empfehlung]");
      var diy = result.querySelector("[data-diy-hinweis]");

      /* Heuristik: bewusst vorsichtig formuliert — ersetzt keine Vor-Ort-Diagnose. */
      var u, e;
      if ((a.ort === "keller" || a.ort === "erdgeschoss") && (a.symptom === "feucht-unten" || a.symptom === "ausbluehungen")) {
        u = "Wahrscheinlich: aufsteigende oder seitlich eindringende Feuchtigkeit";
        e = "Feuchte Zonen im unteren Wandbereich und Salzausblühungen deuten im Keller meist auf kapillar aufsteigende Feuchtigkeit oder drückendes Erdreich hin. Eine fehlende oder defekte Horizontalsperre ist die häufigste Ursache.";
      } else if (a.symptom === "schimmel-ecke") {
        u = "Wahrscheinlich: Kondensationsfeuchte";
        e = "Schimmel in Raumecken, an Fensterlaibungen oder hinter Möbeln entsteht oft durch Kondenswasser an kalten Oberflächen — nicht zwingend durch einen Bauschaden. Lüftungsverhalten und Wärmebrücken sind die ersten Prüfpunkte.";
      } else if (a.symptom === "putz-platzt") {
        u = "Wahrscheinlich: durchfeuchtetes Mauerwerk mit Salzbelastung";
        e = "Abplatzender Putz und Salzränder zeigen, dass Feuchtigkeit schon länger im Mauerwerk arbeitet. Hier gehören Ursache (Sperrschicht) und Oberfläche (Sanierputz) zusammen betrachtet.";
      } else if (a.ort === "fassade") {
        u = "Wahrscheinlich: Schlagregen- oder Spritzwasserbelastung";
        e = "Durchfeuchtete Fassaden- und Sockelzonen entstehen häufig durch eindringendes Regenwasser oder fehlenden Sockelschutz. Eine Hydrophobierung bzw. Flächensperre schützt dauerhaft.";
      } else {
        u = "Mehrere Ursachen möglich";
        e = "Deine Angaben passen zu mehreren Schadensbildern. Genau dafür gibt es die kostenlose Schadensanalyse: Fotos einsenden, Einschätzung vom Fachmann erhalten.";
      }

      var schwer = a.ausmass === "gross" || a.dauer === "lange";
      if (schwer) {
        empf.textContent = "Unsere ehrliche Empfehlung: Bei diesem Ausmaß solltest du die Ursache von einem zertifizierten BKM-Fachbetrieb prüfen lassen. Eine Sanierung wirkt nur, wenn die Diagnose stimmt.";
        if (diy) diy.hidden = true;
      } else {
        empf.textContent = "Gute Nachricht: Ein begrenztes Schadensbild wie deins lässt sich oft in Eigenleistung beheben — mit dem passenden Home-Line-System und unserer Schritt-für-Schritt-Anleitung. Wenn du lieber abgibst, ist der Fachbetrieb dein Weg.";
        if (diy) diy.hidden = false;
      }
      ursache.textContent = u;
      text.textContent = e;
    }

    show(0);
  }

  /* ---------- Formular-Validierung (Fachbetrieb-Anfrage) ---------- */
  var form = document.querySelector("form[data-validate]");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var valid = true;
      form.querySelectorAll("[required]").forEach(function (input) {
        var field = input.closest(".field");
        var ok = input.value.trim() !== "";
        if (ok && input.type === "email") ok = /.+@.+\..+/.test(input.value);
        if (field) field.classList.toggle("has-error", !ok);
        if (!ok) valid = false;
      });
      if (!valid) {
        var firstErr = form.querySelector(".has-error input, .has-error textarea");
        if (firstErr) firstErr.focus();
        return;
      }
      /* Prototyp: Backend-Anbindung folgt beim Go-Live (siehe roadmap.md). */
      form.hidden = true;
      var success = document.getElementById("form-success");
      if (success) {
        success.hidden = false;
        var h = success.querySelector("h3");
        if (h) h.focus();
      }
    });
  }
})();
