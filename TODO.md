# TODO – Sheet 1 (Abgabe Do 26.11.2026)

Legende: 🧠 = selbst verstehen/entscheiden (Kolloquium!) · ⚙️ = Code/Rechnen, Claude kann helfen

## Erledigt
- [x] Repo-Struktur, `build_context.py`, `fca_tools.py`, Tests, Report-Vorlage
- [x] Rohdaten aller 32 Sportarten (Wikipedia/Olympedia), gegen offiziellen Medaillenspiegel geprüft
- [x] Top 25 festgelegt (kein Gleichstand an der Grenze)

## Dienstag 24.11. – Grundlagen + Schritt 1–2
- [ ] ⚙️ Setup lokal: `git clone`, venv, `pip install -r requirements.txt`, Graphviz installieren, `pytest` läuft
- [ ] 🧠 Sportarten final wählen (12–15) und begründen; Ziel: lesbares Diagramm (aktuell 14 Sportarten → 269 Begriffe, zu viel)
- [ ] ⚙️ `SPORTS` im Skript anpassen, `olympics.cxt` neu bauen
- [ ] 🧠 Schritt 1 schreiben: Anteil Kreuze, Nation mit meisten Sportarten, Sportart mit meisten Nationen, Informationsverlust + Beispielnation
- [ ] 🧠 Ableitungsoperatoren A′, B′, B″ verstehen (Erklärung mit Claude)
- [ ] 🧠 Schritt 2 (a)–(c): Formel aufschreiben, von Hand an der Tabelle prüfen, mit `fca_tools` gegenchecken
- [ ] 🧠 „Abgeschlossen“ in Journalisten-Sprache formulieren

## Mittwoch 25.11. – Schritt 3–5
- [ ] 🧠 NextClosure / lektische Ordnung verstehen
- [ ] 🧠 Handrechnung auf 5 Sportarten (Papier), erste 3 Schritte mit Begründung; mit `next_closure(..., trace=True)` prüfen; Foto nach `handrechnung/`
- [ ] 🧠 Anzahl Begriffe vs. 2^|M|; Kontext mit 2^n Begriffen (Kontranominalskala); warum Sportdaten weit darunter bleiben
- [ ] ⚙️ Liniendiagramm zeichnen (reduzierte Beschriftung), ggf. Layout verbessern
- [ ] 🧠 Schritt 4: ≥ 3 Aussagen aus dem Diagramm ablesen (Unterordnung, unvergleichbar, Lage der Top 5)
- [ ] ⚙️ Schritt 5: Medaillen-Zwillinge, reduzierbare Sportarten finden (Funktion für Reduzierbarkeit ergänzen)
- [ ] 🧠 Schritt 5: Bedeutung von Reduzierbarkeit erklären, Form des reduzierten Verbands prüfen

## Donnerstag 26.11. – Schritt 6 + Abgabe
- [ ] 🧠 3–5 Befunde mit Begriff (Umfang/Inhalt), im Diagramm markiert; ≥ 1 Befund, den der Medaillenspiegel nicht zeigt
- [ ] ⚙️ Gold-Variante (`--gold-only`) bauen, Diagramm
- [ ] 🧠 Robustheit: Welche Befunde überleben die Gold-Variante?
- [ ] 🧠 Bericht fertigstellen (≤ 5 Seiten + Anhang), Quelle + Abrufdatum drin
- [ ] ⚙️ Export als PDF, Seitenzahl prüfen
- [ ] 🧠 `AI_LOG.md` vervollständigen (TODO-Felder: was geprüft/geändert)
- [ ] 🧠 Stichproben der Rohdaten selbst gegen Wikipedia prüfen
- [ ] Abgabe-Checkliste im README durchgehen, abgeben

## Kolloquium-Vorbereitung
- [ ] 🧠 Ableitung und Hülle auf der eigenen Tabelle von Hand rechnen können
- [ ] 🧠 Zu jedem Befund den Begriff im Diagramm zeigen können

## Offen / zu klären
- [ ] Abgabezeit am 26.11. (Uhrzeit?) und Abgabeweg (Moodle?)
- [ ] Sprache des Berichts (Blatt ist Englisch)
- [ ] Format und Inhalt der allgemeinen KI-Richtlinie für `AI_LOG.md`
