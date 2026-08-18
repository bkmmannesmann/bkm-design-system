# Standards Registry

Die Registry verwaltet ausschließlich bibliografische Metadaten, Status, Quelle, Scope, betroffene Zeichnungskomponenten und offene Verifikationen. Sie enthält keine Normvolltexte und erzeugt keine normative Konformitätsaussage.

| Regel | Umsetzung |
|---|---|
| Primärquelle | Jede Quelle verweist auf ISO, DIN Media, DIN, WTA oder eine andere offizielle Stelle. |
| Ausgabe und Status | `edition`, `status` und `checked_at` werden sichtbar gespeichert. |
| Projektbezug | `applicability` bleibt `NORMATIVE_VERIFICATION_REQUIRED`, bis ein Mensch die konkrete Anwendbarkeit prüft. |
| Keine Volltexte | `normative_text_in_repository` ist stets `false`. |
| Keine Agentenfreigabe | Automatisierte Erzeugung schreibt ausschließlich `DRAFT` und setzt keine Review-Flags. |

Der Prüfablauf lautet: Quelle identifizieren, Primärquelle prüfen, Ausgabe und Status erfassen, Anwendbarkeit je Detail prüfen, cross-checken, offene Fragen dokumentieren und erst dann fachlich implementieren.
