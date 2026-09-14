# Prototyp bkm-duesseldorf.de – Arbeiten am Design

- `style.css` – das gesamte Design. Oben im `:root` stehen alle Tokens (Farben, Schriften, Radius, Breiten). Farben ändern = nur dort.
- `index.html` – Startseite. Achtung: die Datei hat keinen eigenen `<head>`, weil die Artifact-Plattform ihn beim Veröffentlichen ergänzt. Lokal im Browser öffnen funktioniert trotzdem.
- `leistungen.html`, `diagnose.html`, sechs Leistungsseiten – vollständige HTML-Dateien.
- `build.py` – erzeugt alle Seiten neu. Die Leistungstexte kommen direkt aus `Fachbetriebs-Websites_Baukasten_v1.md` (Teil F.1–F.6), die Betriebsdaten stehen im Dictionary `V` oben im Skript. Ausführen: `python3 build.py` (Python 3, keine Abhängigkeiten).

Wer nur am Design arbeitet, ändert `style.css` und lädt die Seiten im Browser neu. Wer Texte oder Struktur ändert, arbeitet in `build.py` bzw. im Baukasten und baut neu.

Schriften kommen von Google Fonts (Barlow Condensed, Source Sans 3); ohne Internet fällt der Browser auf Arial zurück.
