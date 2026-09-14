# Fachbetriebs-Websites – Baukasten v1

*Seitenkonzept, Datensteckbrief, Startseiten-Template und sechs Leistungstexte für die Websites der zertifizierten BKM-Fachbetriebe · Umsetzung in WordPress mit Astra und Elementor (Standardversion) · Version 1.1 · Stand 14.09.2026*

**Grundlage:** bkm-mannesmann.de/fachbetriebe/ (PLZ-Suche) und bkm-mannesmann.de/wettringen/ (bestehende Landingpage als Struktur-Vorlage), Kundenbroschüre Fachbetrieb v1, Systemarchitektur Master und Module 01/02/03/05/06/11, Fachbetrieb Leistungen.pdf, BKM Brand Voice, Zielgruppen-Avatare P3 und P4.

**Festlegungen aus dem Briefing (14.09.2026):** Umfang schlank (Startseite + Leistungsseiten + Diagnose/Kontakt + Rechtliches) · Leistungen: Kernpaket Keller und Wand (sechs Leistungen) plus vier optionale Module je Betrieb · Ansprache „Du“ (großgeschrieben, wie auf den bestehenden Landingpages) · Zusagen der Landingpage (kostenlose Diagnose, Festpreis, Antwort in 24 Std., meist 1–3 Tage) gelten für alle Betriebe · Domains bkm-[ort].de bestehen bereits und werden von BKM verwaltet · Der Fachbetrieb ist rechtlich eigenständiger Anbieter seiner Website (eigenes Impressum); BKM gestaltet und betreibt die Websites als Marketingservice · Technik: WordPress, Theme Astra, Elementor Standard (kein Pro) · Pilot: bkm-duesseldorf.de.

**Wie dieses Dokument benutzt wird:** Teil A und B sind das Konzept (einmal lesen, einmal entscheiden). Teil C ist das Formular, das jeder Fachbetrieb ausfüllt. Teil D bis G sind die fertigen Texte mit Platzhaltern – sie werden einmal in der Master-Site angelegt und danach für jeden Betrieb nur noch mit den Steckbrief-Daten befüllt. Teil H beschreibt den Produktionsweg in WordPress. Teil I enthält die Qualitätsprüfung und die offenen Punkte, die BKM vor dem Rollout entscheiden sollte.

---

# TEIL A – KONZEPT IN KÜRZE

## A.1 Das Ziel

Rund 40 zertifizierte Fachbetriebe bekommen je eine eigene Website, die den Kunden in seiner Region abholt, ihm die sechs Kernleistungen verständlich erklärt und ihn zu einem kleinen, unverbindlichen nächsten Schritt führt: der Feuchtigkeitsdiagnose vor Ort. Die Websites sollen mit möglichst wenig Aufwand entstehen und gepflegt werden. Das gelingt nur, wenn 90 Prozent des Inhalts für alle Betriebe identisch sind und die restlichen 10 Prozent aus einem Formular kommen.

## A.2 Zwei Ebenen, eine Logik

**Ebene 1 – bkm-mannesmann.de/fachbetriebe/ (bestehend).** Die zentrale Einstiegsseite mit PLZ-Suche. Sie beantwortet die Frage „Wer ist in meiner Nähe?“ und leitet auf die Website des zuständigen Fachbetriebs weiter. Sie bleibt, wie sie ist; nur die Verlinkung der Suchergebnisse zeigt künftig auf die Fachbetriebs-Websites.

**Ebene 2 – die Fachbetriebs-Website (neu, z. B. bkm-duesseldorf.de).** Die Domains bkm-[ort].de bestehen bereits und liegen bei BKM. BKM gestaltet und betreibt die Websites als Marketingservice für die Betriebe; Anbieter der jeweiligen Website bleibt der Betrieb als eigenständiger Unternehmer – mit eigenem Impressum. Sie beantwortet die Fragen „Was habe ich?“, „Was macht der Betrieb dagegen?“ und „Wie geht es weiter?“. Ihre Startseite folgt der Struktur der bestehenden Landingpage; dazu kommen sechs Leistungsseiten, eine Diagnose-/Kontaktseite und die rechtlichen Seiten.

**Was mit den bestehenden Landingpages unter bkm-mannesmann.de/[ort]/ passiert:** Sie sollten nicht wortgleich neben der neuen Startseite bestehen bleiben (doppelter Inhalt schwächt beide Seiten in der Suche). Empfehlung: Die Landingpage auf der BKM-Domain wird zum Kurzprofil (Steckbrief, Einsatzgebiet, Diagnose-Formular, Link zur Fachbetriebs-Website) – oder sie leitet per 301 auf die Fachbetriebs-Website weiter, sobald diese live ist. Entscheidung siehe Teil I.

## A.3 Die Prinzipien

**Kunde vor Betrieb.** Jede Seite beginnt beim Problem des Kunden, nicht bei der Firma. Der Betrieb erscheint als Ansprechpartner, nicht als Held.

**Ursache vor Produkt.** Die Leistungsseiten erklären, welches Schadensbild auf welche Ursache hinweist und nach welchem Prinzip die Sanierung arbeitet. Produktnamen kommen nicht vor; sie gehören ins Angebot.

**Grenzen vor Versprechen.** Jede Leistungsseite sagt, was die Maßnahme nicht leistet. Das ist der wichtigste Vertrauensbaustein gegenüber Wettbewerbern, die alles versprechen.

**Ein nächster Schritt.** Auf jeder Seite ist der Weg zur Diagnose vor Ort in einem Klick erreichbar. Keine Verknappung, kein „Jetzt Angebot anfordern“.

**Ein Text, 40 Orte.** Alle Texte enthalten Platzhalter für Betrieb, Ort, Region, Einsatzgebiet und Kontakt. Was regional klingen soll, kommt aus zwei Steckbrief-Feldern (Regionssatz, Bausubstanz-Satz), nicht aus 40 Einzeltexten.

---

# TEIL B – SEITENARCHITEKTUR JE FACHBETRIEBS-WEBSITE

## B.1 Sitemap

| Nr. | Seite | URL-Pfad | Aufgabe | Vorlage |
|---|---|---|---|---|
| 1 | Startseite | / | Abholen, Vertrauen, Ablauf, Leistungen anteasern, Diagnose anbieten | Teil D |
| 2 | Leistungen (Übersicht) | /leistungen/ | Sechs Leistungen in einer Karte pro Leistung, Einstieg über Schadensbild | Teil E |
| 3 | Horizontalsperre | /horizontalsperre/ | Aufsteigende Feuchtigkeit | Teil F.1 |
| 4 | Flächensperre | /flaechensperre/ | Querdurchfeuchtung, nicht freilegbare Wände | Teil F.2 |
| 5 | Innenabdichtung | /innenabdichtung/ | Seitlich eindringende Feuchtigkeit, Keller von innen | Teil F.3 |
| 6 | Wand-Boden-Anschluss | /wand-boden-anschluss/ | Wasser am Übergang Wand/Boden nach Regen | Teil F.4 |
| 7 | Rissverpressung | /rissverpressung/ | Wasserführende Risse und Fugen | Teil F.5 |
| 8 | Sanierputz | /sanierputz/ | Salzschäden, Putz platzt trotz trockener Wand | Teil F.6 |
| 9 | Diagnose vor Ort | /diagnose/ | Formular, Ablauf des Termins, Kontakt | Teil G |
| 10 | Impressum | /impressum/ | Rechtliches des Betriebs (der Betrieb ist Anbieter der Website) | Steckbrief |
| 11 | Datenschutz | /datenschutz/ | Rechtliches (zentrale Vorlage, Betrieb als Verantwortlicher) | zentrale Vorlage |
| M1 | Schimmel & Kondensation (optional) | /schimmel-kondensation/ | Feuchtigkeit aus der Raumluft | Teil F.8 |
| M2 | Fassadenschutz (optional) | /fassadenschutz/ | Schlagregen auf saugfähigen Fassaden | Teil F.8 |
| M3 | Bodenbeschichtung (optional) | /bodenbeschichtung/ | Keller- und Garagenböden | Teil F.8 |
| M4 | Mauerwerksverfestigung (optional) | /mauerwerksverfestigung/ | Mürbes Mauerwerk im Altbau | Teil F.8 |

Bewusst nicht enthalten: „Über uns“ (die Vorstellung des Betriebs steht auf der Startseite im Ansprechpartner-Block), „Referenzen“ (kann später als Modul ergänzt werden), Blog/Ratgeber (bleibt zentral auf bkm-mannesmann.de; die Fachbetriebs-Seiten verlinken dorthin).

## B.2 Navigation

Hauptmenü (Astra Header): Leistungen (Dropdown mit den sechs Leistungen) · Ablauf (Anker auf der Startseite) · Häufige Fragen (Anker) · Kontakt (→ /diagnose/). Rechts im Header ein Button „Kostenlose Diagnose“ (→ /diagnose/) und die Telefonnummer als Klick-to-Call.

Footer (Astra Footer-Builder): Spalte 1 Betrieb mit Adresse, Telefon, E-Mail · Spalte 2 Leistungen (sechs Links) · Spalte 3 Einsatzgebiet (Orte als Text) und Link „Zertifizierter BKM-Fachbetrieb – mehr über das System“ (→ bkm-mannesmann.de) · unterste Zeile Impressum, Datenschutz, BKM-Siegel.

## B.3 Die feste Struktur jeder Leistungsseite

Alle sechs Leistungsseiten haben dieselben acht Blöcke in derselben Reihenfolge. Das macht die Seiten für den Kunden vergleichbar und für die Produktion kopierbar: Ein Elementor-Template, sechs Mal befüllt.

1. **Hero** – H1 mit Leistung und Ort, ein Satz, der das Schadensbild benennt, Button „Kostenlose Diagnose“.
2. **Woran Du es erkennst** – drei bis fünf typische Anzeichen (Icon-Liste). Formuliert als Hinweis, nie als Diagnose.
3. **Woher es kommt** – die Ursache in Alltagssprache, dann der Fachbegriff.
4. **Wie die Sanierung arbeitet** – das Prinzip der Lösung und der Ablauf beim Fachbetrieb in drei bis fünf Schritten.
5. **Was Du wissen solltest** – Grenzen der Maßnahme, was sie nicht leistet, was dazugehört.
6. **Was danach kommt** – Trocknung, Folgeschichten, Anstrich, Nutzung.
7. **Häufige Fragen** – fünf Fragen (Elementor Accordion), zusätzlich als FAQ-Schema.
8. **Der nächste Schritt** – Diagnose-CTA mit Ort, Kontaktblock des Betriebs.

## B.4 Seitentitel und Meta-Beschreibungen (Vorlagen)

| Seite | Title (max. ca. 60 Zeichen) | Meta-Description (max. ca. 155 Zeichen) |
|---|---|---|
| Startseite | Mauertrockenlegung & Kellersanierung in [ORT] – [BETRIEB_KURZ] | Feuchte Wände oder nasser Keller in [ORT] und [REGION]? Zertifizierter BKM-Fachbetrieb: kostenlose Diagnose vor Ort, Sanierung von innen, meist ohne Aufgraben. |
| Leistungen | Leistungen gegen Feuchtigkeit in [ORT] – [BETRIEB_KURZ] | Horizontalsperre, Innenabdichtung, Rissverpressung, Sanierputz und mehr – welche Lösung zu welchem Schaden passt. Fachbetrieb in [ORT]. |
| Horizontalsperre | Horizontalsperre in [ORT] – nachträglich, ohne Aufgraben | Feuchte Wand von unten? Nachträgliche Horizontalsperre im Injektionsverfahren in [ORT] und [REGION]. Kostenlose Diagnose vor Ort. |
| Flächensperre | Flächensperre in [ORT] – Mauerwerk in der Tiefe abdichten | Wand von der Seite feucht und nicht freilegbar? Flächensperre durch Rasterinjektion in [ORT]. Wann sie passt, wann nicht. |
| Innenabdichtung | Kellerabdichtung von innen in [ORT] – Innenabdichtung | Kellerwand großflächig feucht? Innenabdichtung nach WTA in [ORT] und [REGION] – ohne Baugrube, auch bei Reihenhäusern. |
| Wand-Boden-Anschluss | Wasser im Keller nach Regen? Wand-Boden-Anschluss in [ORT] | Pfützen am Übergang von Wand und Boden: Abdichtung der Aufstandsfuge von innen in [ORT]. Kostenlose Diagnose. |
| Rissverpressung | Rissverpressung in [ORT] – Risse und Fugen dauerhaft dicht | Wasser tritt aus einem Riss? Zweistufige Rissverpressung in [ORT] und [REGION]: erst stoppen, dann dauerhaft schließen. |
| Sanierputz | Sanierputz in [ORT] – wenn Putz trotz trockener Wand abplatzt | Salzausblühungen und abplatzender Putz? Sanierputz nach WTA in [ORT]. Was er leistet – und was nicht. |
| Diagnose | Kostenlose Feuchtigkeitsdiagnose in [ORT] – Termin anfragen | Ein Termin, ein Blick auf die Wand, eine ehrliche Einschätzung. Diagnose vor Ort in [ORT] und [EINSATZGEBIET_KURZ] – unverbindlich. |

## B.5 Strukturierte Daten

Auf jeder Seite ein JSON-LD-Block `LocalBusiness` (Name, Adresse, Telefon, E-Mail, Einsatzgebiet als `areaServed`, Öffnungszeiten wenn angegeben, `sameAs` auf das Profil unter bkm-mannesmann.de). Auf jeder Leistungsseite zusätzlich `Service` (Name der Leistung, `provider` = Betrieb, `areaServed`) und `FAQPage` mit den fünf Fragen. Die Blöcke werden in der Master-Site als HTML-Widget angelegt und enthalten dieselben Platzhalter wie die Texte (siehe Teil H).

## B.6 Interne Verlinkung

Startseite → alle sechs Leistungsseiten (Leistungs-Teaser) und → /diagnose/. Jede Leistungsseite → /diagnose/ (Hero-Button und Schlussblock), → zwei verwandte Leistungen (im Block „Was Du wissen solltest“, z. B. Horizontalsperre → Sanierputz, Innenabdichtung), → Startseiten-Anker „Ablauf“. Jede Seite → bkm-mannesmann.de (Footer: „Zertifizierter BKM-Fachbetrieb“). bkm-mannesmann.de/fachbetriebe/ → Startseite des Betriebs (PLZ-Ergebnis).

---

# TEIL C – DATENSTECKBRIEF JE FACHBETRIEB

## C.1 Prinzip

Der Steckbrief ist das einzige, was ein Fachbetrieb liefern muss. Er wird als Online-Formular (z. B. Google Form, WPForms auf bkm-mannesmann.de oder eine Tabelle) bereitgestellt. Jede Zeile entspricht einem Platzhalter in den Texten. Pflichtfelder sind so gewählt, dass die Website ohne die optionalen Felder vollständig funktioniert.

## C.2 Die Felder

| Nr. | Platzhalter | Feld | Pflicht | Vorgabe | Ausfüllhinweis für den Betrieb |
|---|---|---|---|---|---|
| 1 | [BETRIEB] | Vollständige Firmierung | Pflicht | max. 60 Zeichen | Wie im Impressum, z. B. „ARS Abdichtungstechnik GmbH“. |
| 2 | [BETRIEB_KURZ] | Kurzname | Pflicht | max. 25 Zeichen | Für Titel und Buttons, z. B. „ARS Abdichtungstechnik“. |
| 3 | [ORT] | Standort | Pflicht | ein Ort | Der Ort, unter dem die Website läuft (Domain bkm-[ort].de), z. B. „Wettringen“. |
| 4 | [PLZ] | Postleitzahl Standort | Pflicht | 5 Ziffern | – |
| 5 | [ADRESSE] | Straße und Hausnummer | Pflicht | – | Geschäftsadresse. |
| 5a | [SITZ_ORT] | Ort der Geschäftsadresse | Pflicht | – | Kann vom Website-Ort abweichen, z. B. Website „Düsseldorf“, Sitz „Monheim am Rhein“. Erscheint nur in Adresse, Impressum und LocalBusiness-Daten. |
| 6 | [REGION] | Regionsbegriff | Pflicht | max. 30 Zeichen, mit Artikel im Dativ | So, wie man es sagt: „im Münsterland“, „im Rheinland“, „im Raum Augsburg“, „in Ostwestfalen“. Wird in Sätzen wie „Feuchte Wände [REGION]?“ verwendet. |
| 7 | [EINSATZGEBIET] | Einsatzgebiet ausführlich | Pflicht | max. 200 Zeichen | Konkrete Städte und Landkreise, z. B. „Wettringen, Rheine, Steinfurt, Emsdetten, Greven, Münster und Umgebung bis ca. 50 km“. |
| 8 | [EINSATZGEBIET_KURZ] | Einsatzgebiet kurz | Pflicht | max. 60 Zeichen | „von Wettringen bis Münster“, „im Kreis Steinfurt und in Münster“. |
| 9 | [TELEFON] | Telefon | Pflicht | – | Die Nummer, unter der ein Mensch abnimmt. |
| 10 | [TELEFON_LINK] | Telefon für Klick-to-Call | Pflicht | +49… ohne Leerzeichen | Wird automatisch aus Feld 9 gebildet, wenn nicht angegeben. |
| 11 | [EMAIL] | E-Mail | Pflicht | – | Ein Postfach, das täglich gelesen wird. |
| 12 | [ANSPRECHPARTNER] | Name des Ansprechpartners | Pflicht | max. 40 Zeichen | Vor- und Nachname der Person, die die Diagnose-Termine macht. |
| 13 | [FUNKTION] | Funktion | Pflicht | max. 40 Zeichen | „Inhaber“, „Bauleitung Abdichtung“, „Ansprechpartnerin für die Schadensaufnahme“. |
| 14 | [FOTO_ANSPRECHPARTNER] | Foto | Pflicht | mind. 1200 px breit, Querformat | In Arbeitssituation (am Messgerät, im Gespräch, am Kellerabgang). Keine verschränkten Arme, kein Stockfoto. |
| 15 | [LOGO] | Logo | Pflicht | SVG oder PNG mit Transparenz, auch Weißvariante | – |
| 16 | [JAHRE_PARTNER] | Jahre als BKM-Systempartner | Pflicht | Zahl | Wird in der Vertrauensleiste gezeigt („7 Jahre BKM Systempartner“). BKM prüft gegen die Partnerliste. |
| 17 | [VORSTELLUNG] | Persönliche Vorstellung | Pflicht | 250–450 Zeichen, Du-Form gegenüber dem Kunden | Wer ihr seid, seit wann, was euch bei Feuchtigkeitsschäden wichtig ist. Keine Floskeln, keine Superlative. Muster in C.3. |
| 18 | [BAUSUBSTANZ_SATZ] | Satz zur Bausubstanz der Region | Pflicht | 1–2 Sätze, max. 300 Zeichen | Was ist typisch für Häuser in eurer Region? Muster in C.3. Wird im Problem-Block der Startseite und in den Leistungsseiten verwendet. |
| 19 | [ORTE_LISTE] | Weitere Orte für die Startseite | optional | 5–12 Orte, kommagetrennt | Orte, in denen ihr regelmäßig arbeitet. Erscheinen als Text im Ansprechpartner-Block und im Footer (hilft bei der lokalen Suche). |
| 20 | [GOOGLE_BEWERTUNG] | Google-Bewertung | optional | Wert und Anzahl, Link zum Profil | Nur, wenn ein Google-Unternehmensprofil mit mindestens 10 Bewertungen existiert. Sonst wird der Block ausgeblendet. |
| 21 | [OEFFNUNGSZEITEN] | Erreichbarkeit | optional | z. B. „Mo–Fr 7:30–17:00 Uhr“ | Für Kontaktblock und LocalBusiness-Daten. |
| 22 | [VERTRAUENSBAUSTEIN] | Belegbare Qualifikation | optional | max. 200 Zeichen | Meisterbrief, Sachverständigenqualifikation, Jahre im Handwerk, weitere Zertifizierungen. Nur Belegbares. |
| 23 | [FOTO_TEAM] | Team- oder Baustellenfoto | optional | Querformat | Für den Ansprechpartner-Block, wenn vorhanden. |
| 24 | [IMPRESSUM] | Impressumsangaben | Pflicht | – | Der Betrieb ist Anbieter seiner Website und für das Impressum selbst verantwortlich: Inhaber/Geschäftsführung, Handelsregister oder Handwerkskammer, USt-IdNr., Verantwortlicher i. S. d. Presserechts, Berufsbezeichnung/Kammer. BKM setzt die Angaben ein, prüft sie aber nicht rechtlich. |
| 25 | [DOMAIN] | Domain | fest | bkm-[ort].de | Besteht bereits und wird von BKM verwaltet; der Betrieb muss nichts tun. |
| 26 | [MODULE] | Optionale Leistungsmodule | Pflicht (Auswahl) | Mehrfachauswahl | Welche der vier Module sollen auf der Website erscheinen: Schimmel & Kondensation · Fassadenschutz · Bodenbeschichtung · Mauerwerksverfestigung. Nur Leistungen ankreuzen, die der Betrieb tatsächlich ausführt. |

## C.3 Musterformulierungen

**Persönliche Vorstellung (Feld 17) – drei Muster, die der Betrieb anpasst, nicht übernimmt:**

Muster 1: „Unser Betrieb ist seit [JAHR] in [ORT] zu Hause. Seit [JAHR] haben wir uns auf Feuchtigkeitsschäden und Bauwerksabdichtung spezialisiert, weil uns aufgefallen ist, wie viele Eigentümer mit widersprüchlichen Empfehlungen alleingelassen werden. Bei uns beginnt jede Sanierung mit einem Termin vor Ort – und mit der Frage, woher die Feuchtigkeit kommt.“

Muster 2: „Ich bin [NAME] und mache bei [BETRIEB_KURZ] die Schadensaufnahmen vor Ort. Mein Anspruch: Du sollst nach unserem Termin verstehen, was mit Deiner Wand los ist – auch dann, wenn am Ende keine Sanierung nötig ist.“

Muster 3: „Als Sanierungsbetrieb in zweiter Generation kennen wir die Häuser [REGION] und ihre typischen Feuchtigkeitsprobleme. Mit den Sanierungssystemen von BKM Mannesmann arbeiten wir seit [JAHR]. Unser Team ist dafür geschult, und wir dokumentieren jede Sanierung so, dass Du sie nachvollziehen kannst.“

**Satz zur Bausubstanz (Feld 18) – drei Muster:**

Muster Münsterland: „Im Münsterland treffen ältere Wohnhäuser aus Ziegel, sanierte Bestandsimmobilien und neuere Einfamilienhäuser aufeinander. Feuchtigkeit im Mauerwerk kann bei jedem dieser Gebäudetypen auftreten.“

Muster Stadt/Altbau: „In [ORT] stehen viele Gründerzeit- und Nachkriegshäuser, die nie eine Sperrschicht gegen aufsteigende Feuchtigkeit bekommen haben – damals Standard, heute die häufigste Ursache für feuchte Kellerwände.“

Muster ländlich/lehmig: „Rund um [ORT] sind die Böden oft lehmig und wenig durchlässig. Nach Starkregen steht Wasser länger an den Kellerwänden an, als viele Abdichtungen aus den 60er- und 70er-Jahren vertragen.“

## C.4 Freigabeprozess

Der Betrieb füllt den Steckbrief aus und liefert Logo und Foto. BKM prüft die Pflichtfelder auf Vollständigkeit, die optionalen Felder auf Belegbarkeit und Brand Voice (keine Garantie- oder Superlativaussagen), setzt die Daten in die geklonte Site ein (Teil H) und schickt dem Betrieb einen Vorschau-Link. Der Betrieb gibt frei oder korrigiert seine eigenen Felder; die festen Texte werden nicht je Betrieb geändert. Änderungswünsche an festen Texten gehen an die Redaktion und fließen in die nächste Version für alle ein.

---

# TEIL D – STARTSEITEN-TEMPLATE

*Struktur wie die bestehende Landingpage (Wettringen), ergänzt um einen Leistungs-Teaser (Block 6), der auf die sechs Leistungsseiten führt. Jeder Block entspricht einem Elementor-Container. Platzhalter in eckigen Klammern kommen aus dem Steckbrief (Teil C).*

## Block 1 – Hero

**H1:** Feuchte Wände [REGION]? Dein BKM-Fachbetrieb für Mauertrockenlegung und Kellersanierung in [ORT]

**Subline:** Feuchtigkeit hat Hausverbot.

**Text:** [BETRIEB] ist zertifizierter BKM-Fachbetrieb für Bauwerksabdichtung – mit Sitz in [ORT] und Einsatzgebiet [EINSATZGEBIET_KURZ]. Der erste Schritt ist nicht die Sanierung, sondern herauszufinden, woher die Feuchtigkeit kommt. Genau damit fangen wir an.

**Button (primär):** Kostenlose Diagnose (→ /diagnose/) · **Button (sekundär):** [TELEFON] anrufen (tel:[TELEFON_LINK])

## Block 2 – Vertrauensleiste (drei Merkmale, BKM-Systempartner-Siegel)

Kein Aufgraben in den meisten Fällen · [JAHRE_PARTNER] Jahre BKM-Systempartner · Sanierung meist in 1–3 Arbeitstagen

## Block 3 – Das Problem

**H2:** Feuchtigkeit wird nicht von allein besser

**Text:** [BAUSUBSTANZ_SATZ] Eine feuchte Wand zeigt immer nur das Ende einer Geschichte – nicht ihren Anfang. Dieselbe dunkle Stelle kann von unten aufsteigen, von der Seite durch die Wand drücken, durch einen Riss eindringen oder aus der Raumluft kommen. Behandelt wird jede dieser Ursachen anders. Deshalb lohnt sich der genaue Blick, bevor irgendjemand etwas verkauft.

**Drei Risiken (Icon-Boxen mit Bild):**

*Gesundheit* – Feuchte Wände können Bedingungen schaffen, unter denen Schimmel entsteht. Das Risiko steigt mit der Dauer, nicht über Nacht.

*Energie* – Feuchtes Mauerwerk dämmt schlechter. Der Raum kühlt aus, die Heizung arbeitet gegen die Wand.

*Wert* – Sichtbare Feuchteschäden fallen jedem Käufer und jedem Gutachter auf. Dokumentierte Sanierung ist das Gegenteil davon.

## Block 4 – Ablauf (Anker „ablauf“)

**H2:** Drei Schritte, die Klarheit schaffen

**Intro:** Du schilderst uns Dein Anliegen. Wir sehen uns die Situation vor Ort an, messen und erklären Dir, was wir sehen. Erst dann geht es um eine Lösung.

**Schritt 1 – Feuchtigkeitsbefund.** Vor-Ort-Analyse mit kalibrierter Messtechnik. Nicht nur der Fleck wird betrachtet, sondern Wandaufbau, Anschlüsse, Rohrdurchführungen und die Frage, wann es feuchter wird. *Label: kostenlos und unverbindlich*

**Schritt 2 – Planbare Sanierung.** Auf Grundlage des Befunds bekommst Du einen Sanierungsplan mit Festpreis, in dem steht, was gemacht wird, warum – und was nicht nötig ist. *Label: schriftlich und nachvollziehbar*

**Schritt 3 – Fachgerechte Ausführung.** Wir sanieren mit abgestimmten BKM-Systemen, in der Regel von innen und ohne Aufgraben. Was gemacht wird, dokumentieren wir mit Fotos und Messwerten. *Label: DIN 18533 und WTA konform*

## Block 5 – Ansprechpartner

**H2:** Ein Ansprechpartner [EINSATZGEBIET_KURZ].

**Text:** [VORSTELLUNG]

**Karte/Person:** [FOTO_ANSPRECHPARTNER] · [ANSPRECHPARTNER], [FUNKTION] · [TELEFON] · [EMAIL]

**Einsatzgebiet:** [EINSATZGEBIET] *(optional darunter: [ORTE_LISTE])*

*(optional, nur wenn Feld 22 ausgefüllt: [VERTRAUENSBAUSTEIN])*

## Block 6 – Leistungen (neu)

**H2:** Es gibt nicht die eine Lösung. Es gibt die passende.

**Intro:** Jede Sanierung unterbricht einen bestimmten Weg des Wassers. Welche zu Deinem Haus passt, entscheidet der Befund. Das sind die sechs Leistungen, mit denen wir [REGION] am häufigsten arbeiten:

**Sechs Karten (Icon-Box mit Link):**

*Horizontalsperre* – Wenn die Wand unten feucht ist und der Fleck nach oben schwächer wird. Neue Sperrschicht per Injektion, ohne Aufgraben. → /horizontalsperre/

*Innenabdichtung* – Wenn die Kellerwand großflächig feucht ist. Abdichtung von innen nach WTA, auch bei Reihenhäusern. → /innenabdichtung/

*Flächensperre* – Wenn die Wand von der Seite feucht ist und von außen nicht erreichbar. Mauerwerk in der Tiefe wasserabweisend machen. → /flaechensperre/

*Wand-Boden-Anschluss* – Wenn nach Regen Wasser am Übergang von Wand und Boden steht. Fuge verpressen, Dichtkehle einbauen. → /wand-boden-anschluss/

*Rissverpressung* – Wenn Wasser aus einem Riss oder einer Fuge kommt. Erst stoppen, dann dauerhaft schließen. → /rissverpressung/

*Sanierputz* – Wenn Putz und Farbe abplatzen, obwohl die Wand trocken oder schon abgedichtet ist. Salze aufnehmen, Oberfläche trocken halten. → /sanierputz/

**Link darunter:** Alle Leistungen im Überblick → /leistungen/

## Block 7 – Das Ergebnis

**H2:** Ein Keller, der wieder Platz bieten kann

**Vier Punkte:** Trockener, nutzbarer Raum · Schimmelprävention durch behobene Ursache · Weniger Wärmeverlust über feuchte Wände · Dokumentation, die auch beim Verkauf zählt

**Bild:** Referenzbild sanierter Keller (zentral von BKM gestellt, bis eigene Referenzfotos freigegeben sind)

**Button:** Jetzt sanieren lassen (→ /diagnose/)

## Block 8 – Diagnose-Formular (Anker „diagnose“)

**H2:** Dein erster Schritt: Befund vor Ort

**Text:** Ein geschulter Fachberater besucht Dich in [ORT] und [REGION], misst die Feuchtigkeit und erklärt Dir, was er sieht. Das ist eine Untersuchung, kein Verkaufsgespräch.

**Was Du bekommst:** Feuchtemessung mit kalibrierter Messtechnik · Dokumentierter Befund mit Ursachenanalyse · Festpreisangebot, wenn eine Sanierung sinnvoll ist · Kein Kaufzwang

**Formularfelder:** Name* · E-Mail* · Telefon* · Postleitzahl* · Kurz: Was hast Du beobachtet? (optional) · Datenschutz-Checkbox*

**Unter dem Formular:** ✓ Unverbindlich ✓ Antwort in 24 Stunden ✓ Fachbetrieb vor Ort

## Block 9 – Vertrauensraster (vier Kacheln)

BKM-Systempartner – Geschult auf abgestimmte Sanierungssysteme · Fachgerecht – Ursache vor Maßnahme, Details im Angebot · Persönlich – Regional. Klar. Erreichbar. · Nachvollziehbar – Dokumentation mit Messwerten und Fotos

*(optional, nur wenn Feld 20 ausgefüllt: Google-Bewertung [GOOGLE_BEWERTUNG] mit Link)*

## Block 10 – Kontakt

[BETRIEB] · [ADRESSE], [PLZ] [SITZ_ORT] · Telefon [TELEFON] · [EMAIL] · [OEFFNUNGSZEITEN]

## Block 11 – Häufige Fragen (Anker „faq“, Elementor Accordion)

*Ist die erste Schadensanalyse wirklich kostenfrei?* – Ja. Der Termin vor Ort mit Messung und Einschätzung kostet Dich nichts und verpflichtet Dich zu nichts. Ein Angebot bekommst Du nur, wenn eine Sanierung aus unserer Sicht sinnvoll ist.

*Warum ein spezialisierter Fachbetrieb und nicht der Maler oder Maurer?* – Weil die Diagnose entscheidet. Ein Betrieb, der auf Bauwerksabdichtung spezialisiert und für die Systeme geschult ist, unterscheidet aufsteigende, seitliche, drückende und Kondensationsfeuchte – und wählt danach die Maßnahme. Sonst wird oft das Symptom behandelt und die Ursache bleibt.

*Welche Gewährleistung gilt?* – Für die Ausführung gilt die gesetzliche Gewährleistung. Was darüber hinaus zugesagt wird, steht schriftlich im Angebot. Dazu bekommst Du eine Dokumentation mit Messwerten, Fotos und den eingesetzten Materialien.

*Wie lange dauert eine Mauertrockenlegung [REGION]?* – Die Arbeiten selbst meist 1–3 Tage, je nach Umfang auch länger. Danach braucht die Wand Zeit zum Trocknen: Wochen, bei dicken, stark durchfeuchteten Wänden Monate. Putz und Anstrich kommen nach der Trocknung. Der konkrete Zeitplan steht im Angebot.

*Muss für die Abdichtung der Garten aufgegraben werden?* – In den meisten Fällen nicht. Im Bestand wird heute von innen abgedichtet: über Bohrlöcher, Abdichtungsschichten und Detailarbeiten an der Wandoberfläche. Aufgraben von außen ist die Ausnahme – bei Neubau, offener Baugrube oder auf ausdrücklichen Wunsch.

*Kommt die Feuchtigkeit wieder?* – Wenn die Ursache richtig erkannt und die passende Maßnahme fachgerecht ausgeführt wurde, nach heutigem Kenntnisstand nicht aus dieser Quelle. Was passieren kann: Eine zweite, bisher unauffällige Ursache tritt hervor – zum Beispiel Kondensat in einem nun besser genutzten Keller. Deshalb steht im Angebot, was abgedichtet wird und was nicht.

## Block 12 – Abschluss

**H2:** Feuchtigkeit nicht aufschieben

**Text:** Feuchtigkeit im Mauerwerk verschwindet nicht von allein, solange ihre Quelle weiter liefert. Nichts davon passiert über Nacht – aber je früher Ursache und Umfang klar sind, desto kleiner fällt die Maßnahme meist aus. Du musst heute nicht wissen, welche Sanierung Du brauchst. Du musst nur den ersten Schritt gehen.

**Buttons:** Diagnose sichern (→ /diagnose/) · Direkt anrufen (tel:[TELEFON_LINK])

---

# TEIL E – LEISTUNGSÜBERSICHT (/leistungen/)

**H1:** Leistungen gegen Feuchtigkeit in [ORT] und [REGION]

**Intro:** Feuchtigkeit hat mehr als einen Weg ins Haus: von unten, von der Seite, mit Druck, durch Schwachstellen oder aus der Raumluft. Jede Leistung auf dieser Seite unterbricht einen dieser Wege. Welche zu Deinem Haus passt, zeigt der Befund vor Ort – nicht die Ferndiagnose. Wenn Du Dein Schadensbild wiedererkennst, findest Du hier den Einstieg.

**Sechs Karten, jeweils: Schadensbild als Überschrift → Leistung → ein Satz → Link.**

*Die Wand ist unten feucht, der Fleck wird nach oben schwächer, weiße Ränder.* → **Horizontalsperre.** Eine neue Sperrschicht knapp über dem Boden unterbricht den Weg nach oben. → /horizontalsperre/

*Die Kellerwand ist großflächig feucht, nach Regen deutlicher, muffiger Geruch.* → **Innenabdichtung.** Die Wand wird von innen gegen das Wasser abgeschlossen – ohne Baugrube. → /innenabdichtung/

*Die Wand ist von der Seite feucht, aber von außen nicht erreichbar (Anbau, Nachbarhaus, Teilunterkellerung).* → **Flächensperre.** Das Mauerwerk wird in seiner Tiefe wasserabweisend gemacht. → /flaechensperre/

*Nach Regen steht Wasser dort, wo Wand und Boden zusammentreffen.* → **Wand-Boden-Anschluss.** Die Fuge wird verpresst und mit einer Dichtkehle eingebunden. → /wand-boden-anschluss/

*Wasser tritt an einem Riss, einer Fuge oder einem Rohr aus.* → **Rissverpressung.** Erst wird das Wasser gestoppt, dann der Riss dauerhaft und beweglich geschlossen. → /rissverpressung/

*Putz und Farbe platzen ab, weiße Ablagerungen kommen wieder – obwohl die Wand trocken oder abgedichtet ist.* → **Sanierputz.** Salze werden im Putz aufgenommen, die Oberfläche bleibt trocken. → /sanierputz/

**Infobox „Was Du wissen solltest“:** In vielen Häusern kommen mehrere Wege zusammen – eine Wand, in der Feuchtigkeit aufsteigt, kann zugleich seitlich Erdfeuchte aufnehmen. Deshalb kombinieren wir Leistungen, wenn der Befund es verlangt, und lassen weg, was nicht nötig ist. Beides steht im Angebot.

**Optionale Karten (nur bei aktivierten Modulen, Teil F.8):** *Schimmel in Ecken, hinter Möbeln, an Fensterlaibungen – ohne Feuchtestreifen.* → **Schimmel & Kondensation** → /schimmel-kondensation/ · *Die Fassade wird bei Regen dunkel, Frostabplatzungen, Algen.* → **Fassadenschutz** → /fassadenschutz/ · *Der Keller- oder Garagenboden staubt, ist uneben oder feucht.* → **Bodenbeschichtung** → /bodenbeschichtung/ · *Mörtel bröckelt, Steine sitzen locker.* → **Mauerwerksverfestigung** → /mauerwerksverfestigung/

**Hinweis (Text, ohne eigene Seite):** Weitere Themen rund um Feuchtigkeitsschutz erklärt BKM Mannesmann zentral im Ratgeber (→ bkm-mannesmann.de/ratgeber).

**CTA:** Du erkennst Dein Schadensbild nicht wieder? Dann ist der Befund vor Ort der richtige erste Schritt. → Kostenlose Diagnose

---

# TEIL F – DIE SECHS LEISTUNGSSEITEN

*Alle sechs Seiten folgen der Acht-Block-Struktur aus B.3. Fachliche Grundlage: Systemarchitektur Module 01, 02, 03, 05, 06, 11 und die Kundenbroschüre v1. Keine Produktnamen, keine Preise, keine Garantieformeln. Block 8 („Der nächste Schritt“) ist auf allen sechs Seiten identisch und steht einmal am Ende von Teil F.*

## F.1 Horizontalsperre (/horizontalsperre/)

### Block 1 – Hero

**H1:** Horizontalsperre in [ORT]: Wenn die Wand von unten feucht wird

**Text:** Ein feuchter Streifen unten an der Wand, der nach oben schwächer wird, weiße Ränder, Putz, der absandet – das ist das typische Bild, wenn Feuchtigkeit aus dem Boden in der Wand aufsteigt. Die nachträgliche Horizontalsperre unterbricht diesen Weg. Von innen, über kleine Bohrlöcher, ohne Aufgraben.

**Button:** Kostenlose Diagnose in [ORT]

### Block 2 – Woran Du es erkennst

- Der Feuchtebereich beginnt am Boden und verläuft in etwa waagerecht; nach oben wird er schwächer.
- Weiße, flauschige oder krustige Ränder an der Grenze zwischen feucht und trocken.
- Putz, der sich löst, sandig abrieselt oder hohl klingt – vor allem im unteren Wandbereich.
- Farbe wirft Blasen oder blättert ab, Sockelleisten sind feucht oder verfärbt.
- Das Bild ist über das Jahr ähnlich – nicht nur nach Regen, nicht nur im Sommer.

Das sind Hinweise, keine Diagnose. Ein waagerechter Feuchtestreifen spricht für aufsteigende Feuchtigkeit, beweist sie aber nicht. Sicherheit gibt die Messung vor Ort.

### Block 3 – Woher es kommt

Eine Wand ist kein massiver Block. Mauerwerk, Mörtel und Putz sind von feinen Poren durchzogen, ähnlich wie ein sehr dichter Schwamm. Steht die Wand auf feuchtem Boden und fehlt die Sperrschicht zwischen Fundament und Mauerwerk – oder ist sie über die Jahrzehnte schadhaft geworden –, saugt die Wand Feuchtigkeit aus dem Erdreich auf und leitet sie nach oben. Mit dem Wasser wandern Salze aus dem Boden in die Wand. Beim Trocknen bleiben sie an der Oberfläche zurück: die weißen Ränder.

Fachleute nennen das kapillar aufsteigende Feuchtigkeit. Besonders häufig ist sie in Häusern, die vor den 1960er-Jahren gebaut wurden – dort war eine Sperrschicht oft nicht vorgesehen. [BAUSUBSTANZ_SATZ]

### Block 4 – Wie die Sanierung arbeitet

**Das Prinzip:** Der Weg nach oben muss unterbrochen werden – durch eine neue Sperrschicht in der Wand, knapp über dem Boden. Dafür wird ein Injektionsmittel in eine Reihe kleiner Bohrlöcher eingebracht. Es verteilt sich in den Poren des Mauerwerks und macht die Porenwände wasserabweisend. Die Poren selbst bleiben offen: Wasser kann nicht mehr aufsteigen, Wasserdampf kann weiter entweichen. Die Wand oberhalb der Sperre trocknet aus.

**Der Ablauf bei [BETRIEB_KURZ]:**

1. **Befund.** Feuchtigkeit an mehreren Stellen messen, Salzbelastung beurteilen, Wandaufbau und Wandstärke feststellen, drückendes Wasser ausschließen. Daraus folgt, welches Injektionsverfahren zu Deiner Wand passt.
2. **Vorbereitung.** Geschädigten Altputz großzügig entfernen – deutlich über den sichtbaren Schaden hinaus, weil Feuchtigkeit und Salze weiter reichen als der Fleck. Raum abdecken, angrenzende Bereiche abtrennen.
3. **Bohren und injizieren.** Eine Bohrlochreihe im festgelegten Abstand, meist in der Lagerfuge, in Ecken zusätzliche Bohrungen. Dann wird das Injektionsmittel eingebracht – je nach Verfahren als Creme oder als Flüssigkeit, mit oder ohne leichten Druck.
4. **Verschließen.** Die Bohrlöcher werden mit einem speziellen Mörtel geschlossen. Der Eingriff ist punktuell; die Wand bleibt stehen.
5. **Dokumentieren.** Messwerte, Fotos, Bohrbild und eingesetzte Materialien werden festgehalten.

### Block 5 – Was Du wissen solltest

**Sie hilft nur gegen Feuchtigkeit von unten.** Kommt die Feuchtigkeit seitlich durch die Kellerwand, braucht es zusätzlich oder stattdessen eine Innenabdichtung oder eine Flächensperre. Oft kommen beide Wege zusammen – dann kombinieren wir.

**Sie ist nichts für drückendes Wasser.** Wenn nach Starkregen oder bei hohem Grundwasser Wasser mit Druck an der Wand ansteht, reicht es nicht, die Wand wasserabweisend zu machen. Dann braucht es eine Abdichtung, die diesem Druck standhält. Genau deshalb wird das im Befund geprüft.

**Sie braucht Zeit.** Das Injektionsmittel muss erst wirken – rechne mit mehreren Wochen, bevor die Wand messbar zu trocknen beginnt. Trocknungsgeräte bringen vorher nichts.

**Sie ist selten allein fertig.** Die Salze bleiben in der Wand. Deshalb folgt nach der Trocknung fast immer ein Sanierputz, der die Salze aufnimmt – sonst platzt auch der neue Putz.

Verwandte Leistungen: → Innenabdichtung · → Sanierputz

### Block 6 – Was danach kommt

Nach dem Eingriff braucht die Wand Wochen, bei dicken, stark durchfeuchteten Wänden Monate, um auszutrocknen. In dieser Zeit erscheinen oft weiße Salzausblühungen auf der Oberfläche. Das ist kein Mangel, sondern ein Zeichen, dass die Wand Feuchtigkeit und Salze abgibt. Nicht überstreichen, sondern trocken abbürsten – oder uns Bescheid geben. Danach folgen Haftbrücke, Sanierputz und ein Anstrich, der Wasserdampf durchlässt. Dichte Farben, Tapeten oder Gipsprodukte gehören nicht auf eine sanierte Wand. Was Deine Wand verträgt und ab wann, erfährst Du bei der Übergabe.

### Block 7 – Häufige Fragen

*Muss dafür der Boden oder die Wand aufgestemmt werden?* – Nein. Die Horizontalsperre wird über eine Reihe kleiner Bohrlöcher an der Wandoberfläche eingebracht – von innen oder von außen, ohne Baugrube und ohne die Wand zu öffnen. Was entfernt wird, ist der geschädigte Altputz.

*Wie lange hält eine nachträgliche Horizontalsperre?* – Bei richtig erkannter Ursache und fachgerechter Ausführung ist eine Injektionssperre auf Jahrzehnte ausgelegt; das Injektionsmittel bleibt in der Wand und verbraucht sich nicht. Wichtig ist, dass keine zweite Ursache übersehen wird – deshalb der Befund vor dem Angebot.

*Wie tief und in welchem Abstand wird gebohrt?* – Das hängt von Wandstärke, Steinart und Verfahren ab und steht im Angebot. Für die Wirkung entscheidend ist, dass die Sperrlinie lückenlos ist – in Ecken und an Anschlüssen wird deshalb zusätzlich gebohrt.

*Kann ich das selbst machen?* – Für eng begrenzte, klare Fälle gibt es Produkte zur Eigenanwendung. Die Grenze liegt bei der Diagnose: Wer die Ursache nicht sicher kennt, behandelt mit dem besten Produkt womöglich das falsche Problem. Wir sagen Dir beim Termin auch, wenn die Antwort lautet: Das kannst Du selbst.

*Was kostet eine Horizontalsperre in [ORT]?* – Das lässt sich ohne Blick auf die Wand nicht seriös sagen: Länge und Dicke der Wand, Steinart, Salzbelastung, Vorarbeiten und ob Sanierputz enthalten ist, bestimmen den Preis. Nach dem Befund bekommst Du ein Festpreisangebot, in dem jede Position erklärt ist.

## F.2 Flächensperre (/flaechensperre/)

### Block 1 – Hero

**H1:** Flächensperre in [ORT]: Wenn die Wand von der Seite feucht ist und von außen nicht erreichbar

**Text:** Manche Wände lassen sich nicht freilegen: Der Nachbar steht direkt daneben, ein Anbau überdeckt die Außenwand, der Keller ist nur teilweise unterkellert. Wenn Erdfeuchte seitlich durch so eine Wand zieht, macht die Flächensperre das Mauerwerk in seiner Tiefe wasserabweisend – über ein Raster aus Bohrkanälen, von innen.

**Button:** Kostenlose Diagnose in [ORT]

### Block 2 – Woran Du es erkennst

- Die Wand ist nicht nur unten, sondern flächig feucht – oft bis über die Höhe des Geländes draußen.
- Verfärbungen und Salzausblühungen verteilt über die Fläche, nicht als waagerechter Streifen.
- Nach längerem Regen deutlicher, in trockenen Wochen schwächer.
- Die Außenseite der Wand ist nicht zugänglich: Grenzbebauung, Anbau, Terrasse, Garage, Teilunterkellerung.
- Muffiger Geruch, der auch nach Lüften bleibt.

Hinweise, keine Diagnose – ob eine Flächensperre passt oder eine Innenabdichtung die bessere Wahl ist, entscheidet der Befund.

### Block 3 – Woher es kommt

Kellerwände stehen mit ihrer Außenseite im Erdreich. Ist die Abdichtung auf dieser Außenseite nie vorhanden gewesen, beschädigt oder gealtert, nimmt die Wand seitlich Feuchtigkeit auf – durch dieselben feinen Poren, in denen Feuchtigkeit auch nach oben steigt. Fachleute sprechen von Querdurchfeuchtung oder seitlich eindringender Feuchtigkeit. Sie tritt großflächig auf und bringt Salze mit, die an der Innenseite ausblühen. [BAUSUBSTANZ_SATZ]

### Block 4 – Wie die Sanierung arbeitet

**Das Prinzip:** Bei der Horizontalsperre wird eine einzelne Linie in die Wand gelegt. Bei der Flächensperre werden mehrere Bohrlochreihen versetzt übereinander – im Schachbrettmuster – über die betroffene Fläche verteilt. Das Injektionsmittel verteilt sich in den Poren und macht das Mauerwerk in seiner Tiefe wasserabweisend. Die Wand kann seitlich kein Wasser mehr aufnehmen, bleibt aber dampfdurchlässig.

**Der Ablauf bei [BETRIEB_KURZ]:**

1. **Befund.** Feuchteverteilung messen, Salzbelastung und Wandaufbau beurteilen, drückendes Wasser ausschließen, prüfen, ob die Wand von außen erreichbar ist. Daraus folgt: Flächensperre, Innenabdichtung oder beides.
2. **Vorbereitung.** Altputz und ungeeignete Beschichtungen entfernen, Raum schützen.
3. **Bohrraster und Injektion.** Bohrkanäle im festgelegten Raster über die Fläche, meist bis etwa 50 cm über die sichtbare Schadgrenze hinaus; in Ecken zusätzliche Bohrungen. Einbringen des Injektionsmittels.
4. **Verschließen und dokumentieren.** Bohrlöcher mit Mörtel schließen; Raster, Messwerte und Materialien festhalten.

### Block 5 – Was Du wissen solltest

**Sie ist eine Lösung für Sonderfälle.** Bei seitlicher Feuchtigkeit im Keller ist die Innenabdichtung im Bestand die Standardlösung. Die Flächensperre kommt dort zum Einsatz, wo die Wand nicht freigelegt werden kann oder wo eine Innenabdichtung ergänzt werden soll, weil die Wand dahinter stark durchfeuchtet ist.

**Sie ist nichts für drückendes Wasser.** Steht Wasser mit Druck an der Wand an, braucht es eine Abdichtung nach Norm, keine Injektion, die nur wasserabweisend macht.

**Sie ersetzt nicht die Horizontalsperre.** Steigt zusätzlich Feuchtigkeit von unten auf, wird beides kombiniert.

**Sie ist mit Sanierputz erst fertig.** Die Salze in der Wand brauchen nach der Trocknung einen Putz, der sie aufnimmt.

Verwandte Leistungen: → Innenabdichtung · → Horizontalsperre

### Block 6 – Was danach kommt

Wie bei der Horizontalsperre: mehrere Wochen Reaktionszeit, danach Wochen bis Monate Trocknung, Salzausblühungen in dieser Zeit sind normal. Anschließend Haftbrücke, Sanierputz und ein dampfdurchlässiger Anstrich. Keine dichten Schichten auf der sanierten Wand.

### Block 7 – Häufige Fragen

*Warum nicht einfach die Wand von außen abdichten?* – Wenn die Wand von außen erreichbar ist und eine Baugrube ohnehin offen ist, kann das sinnvoll sein. Im Bestand ist Aufgraben aber aufwendig, teuer und bei Grenzbebauung oft unmöglich. Deshalb wird heute meist von innen gearbeitet: mit Innenabdichtung, Flächensperre oder beidem.

*Flächensperre oder Innenabdichtung – was ist besser?* – Keins ist „besser“, sie arbeiten unterschiedlich. Die Innenabdichtung schließt die Wand auf der Innenseite gegen das Wasser ab; die Wand dahinter bleibt feucht, der Raum wird trocken. Die Flächensperre macht das Mauerwerk selbst wasserabweisend. Was zu Deiner Wand passt, hängt von Wandaufbau, Durchfeuchtung, Wasserbelastung und Zugänglichkeit ab.

*Wie viele Bohrlöcher werden gesetzt?* – Das ergibt sich aus Fläche, Wandstärke und Steinart und steht im Angebot. Der Eingriff bleibt punktuell; die Wand wird nicht geöffnet.

*Kann ich eine Flächensperre selbst einbringen?* – Einzelne Produkte zur Eigenanwendung gibt es, doch bei flächiger Durchfeuchtung ist die Abgrenzung zu drückendem Wasser und die Entscheidung zwischen Flächensperre und Innenabdichtung eine Fachfrage. Bei unklarer Ursache empfehlen wir den Befund vor Ort.

*Was kostet eine Flächensperre in [ORT]?* – Fläche, Wandstärke, Steinart, Vorarbeiten und der anschließende Putzaufbau bestimmen den Preis. Nach dem Befund bekommst Du ein Festpreisangebot mit erklärten Positionen.

## F.3 Innenabdichtung (/innenabdichtung/)

### Block 1 – Hero

**H1:** Kellerabdichtung von innen in [ORT]: Wenn die Kellerwand großflächig feucht ist

**Text:** Wenn Erdfeuchte seitlich durch die Kellerwand zieht, muss die Wand gegen das Wasser abgeschlossen werden. Im Bestand geschieht das heute in den meisten Fällen von innen: ohne Baugrube, ohne Änderung an der Fassade, auch bei Reihenhäusern und enger Bebauung. Die Innenabdichtung nach WTA ist bei [BETRIEB_KURZ] die Standardlösung für seitlich eindringende Feuchtigkeit [REGION].

**Button:** Kostenlose Diagnose in [ORT]

### Block 2 – Woran Du es erkennst

- Größere Bereiche der Kellerwand sind feucht oder dunkel verfärbt, nicht nur ein Streifen am Boden.
- Nach Regen oder bei Schneeschmelze wird es deutlicher.
- Salzausblühungen und abplatzender Putz verteilt über die Fläche.
- Muffiger Kellergeruch, eingelagerte Dinge werden klamm.
- In schweren Fällen: Wasser, das an der Wand herunterläuft oder am Boden steht.

Hinweise, keine Diagnose. Ob es sich um Bodenfeuchte, Sickerwasser oder drückendes Wasser handelt, entscheidet über den Aufbau der Abdichtung – und das klärt der Befund.

### Block 3 – Woher es kommt

Die Außenseite der Kellerwand liegt ständig am Erdreich. Fehlt die Abdichtung dort, ist sie gealtert oder beschädigt, nimmt die Wand seitlich Feuchtigkeit auf. Bei wenig durchlässigem Boden oder nach Starkregen kann Wasser zusätzlich an der Wand anstehen und mit Druck wirken. Mit dem Wasser kommen Salze, die an der Innenseite ausblühen und Putz und Farbe sprengen. Fachleute unterscheiden Bodenfeuchte, nicht drückendes Wasser und drückendes Wasser – und wählen danach die Abdichtung. [BAUSUBSTANZ_SATZ]

### Block 4 – Wie die Sanierung arbeitet

**Das Prinzip:** Auf der Innenseite der Wand wird eine mineralische Abdichtung aufgebaut, die auch Wasserdruck von der Rückseite aushält. Ecken, der Übergang zu Boden, Rohrdurchführungen und Risse werden in diese Abdichtung eingebunden – denn dort versagen Abdichtungen, nicht in der Fläche. Wichtig zu verstehen: Die Wand hinter der Abdichtung bleibt feucht. Der Raum wird trocken.

**Der Ablauf bei [BETRIEB_KURZ]:**

1. **Befund.** Feuchteverteilung, Salze, Wasserbelastung (Bodenfeuchte, Sickerwasser, drückendes Wasser), Risse, Rohrdurchführungen, Wand-Boden-Fuge und Untergrund prüfen. Daraus folgt der Aufbau: Schichtdicke, Details, ergänzende Maßnahmen.
2. **Vorbereitung.** Altputz, lose Farbe und ungeeignete Beschichtungen vollständig entfernen, Fehlstellen und Ausbrüche mit Mörtel schließen. Der Untergrund entscheidet über alles, was danach kommt.
3. **Details zuerst.** Am Übergang von Wand und Boden wird eine abgerundete Dichtkehle aus Mörtel ausgebildet. Wasserführende Risse und die Wand-Boden-Fuge werden vorher verpresst. Rohrdurchführungen bekommen Dichtkehle und Manschette.
4. **Abdichtung in zwei Lagen.** Die mineralische Abdichtung wird in mindestens zwei Lagen aufgetragen; Dichtbänder und Manschetten werden in die erste Lage eingebettet. Schichtdicke nach Wasserbelastung.
5. **Aufbau darauf.** Vorspritzmörtel, Sanierputz und ein dampfdurchlässiger Anstrich. Bei Bedarf zusätzlich Horizontalsperre (wenn Feuchtigkeit auch von unten aufsteigt) oder Flächensperre (bei stark durchfeuchteter, nicht freilegbarer Wand).
6. **Dokumentieren.** Untergrund, Schichten, Details, Messwerte, Fotos.

### Block 5 – Was Du wissen solltest

**Die Wand bleibt feucht, der Raum wird trocken.** Das ist kein Nachteil, aber es erklärt, warum Sanierputz und ein Anstrich, der Wasserdampf durchlässt, zwingend dazugehören.

**Drückendes Wasser ändert den Aufbau.** Bei Grundwasser oder aufstauendem Sickerwasser werden Schichtdicke, Boden-Wand-Übergang und oft auch die Bodenplatte in die Abdichtung einbezogen. Ein Angebot, das nur Quadratmeter Wand ausweist, hat das meist nicht berücksichtigt.

**Außen bleibt die Ausnahme.** Eine Abdichtung von außen ist im Bestand die Sonderlösung: bei Neubau, ohnehin offener Baugrube, aus besonderen baulichen Gründen oder auf Deinen ausdrücklichen Wunsch. Wir sagen Dir, wenn das bei Dir der bessere Weg ist.

**Details entscheiden.** Kehle, Ecken, Rohre, Übergänge – kleine Flächen, großer Anteil an der Sorgfalt. Sie stehen ausdrücklich im Angebot.

Verwandte Leistungen: → Wand-Boden-Anschluss · → Rissverpressung · → Sanierputz

### Block 6 – Was danach kommt

Die Abdichtung selbst ist nach wenigen Tagen belastbar; der Putzaufbau folgt nach den vorgesehenen Wartezeiten. Der Raum ist während der Arbeiten nicht nutzbar, das übrige Haus in aller Regel schon. Nach Abschluss: kein Regal direkt an der frischen Wand in den ersten Wochen, keine dichten Farben, Tapeten oder Fliesen ohne Rücksprache. Bei richtigem Lüften bleibt der Raum nutzbar – als Lager, Werkstatt, Hobbyraum oder, je nach Gebäude, als Wohnraum.

### Block 7 – Häufige Fragen

*Kann eine Abdichtung von innen wirklich dauerhaft halten?* – Ja, wenn sie richtig aufgebaut ist. Die dafür entwickelten mineralischen Abdichtungen sind so ausgelegt, dass sie Wasserdruck von der Rückseite standhalten, und werden nach anerkannten Regelwerken (DIN 18533, WTA-Merkblatt) ausgeführt. Entscheidend sind Untergrund, Schichtdicke, Dichtkehle und die Einbindung aller Details.

*Muss der Estrich geöffnet werden?* – Am Rand des Bodens kann es nötig sein, einen schmalen Streifen Estrich zu öffnen, um die Wand-Boden-Fuge zu erreichen und die Dichtkehle auszubilden. Ganze Böden werden nicht aufgestemmt.

*Wie lange dauert eine Innenabdichtung?* – Die Arbeiten selbst dauern je nach Umfang wenige Tage bis ein bis zwei Wochen, einschließlich Wartezeiten zwischen den Schichten. Der Zeitplan für Deinen Keller steht im Angebot.

*Reicht eine Dichtschlämme aus dem Baumarkt?* – Für einen dauerhaft trockenen Keller reicht ein Anstrich nicht. Es geht um den Aufbau: Untergrundvorbereitung, Dichtkehle, zwei Lagen in passender Dicke, Details, Sanierputz. Fehlt ein Glied, sucht sich das Wasser den nächsten Weg – meist an einer Ecke oder einem Rohr.

*Was kostet eine Kellerabdichtung von innen in [ORT]?* – Fläche, Untergrund, Wasserbelastung, Zahl der Details und der Putzaufbau bestimmen den Preis. Nach dem Befund bekommst Du ein Festpreisangebot; jede Position ist erklärt, auch der Umgang mit Befunden, die erst während der Arbeiten sichtbar werden.

## F.4 Wand-Boden-Anschluss (/wand-boden-anschluss/)

### Block 1 – Hero

**H1:** Wasser im Keller nach Regen? Wand-Boden-Anschluss abdichten in [ORT]

**Text:** Eine Pfütze genau dort, wo Wand und Boden zusammentreffen – nach jedem stärkeren Regen wieder. Dahinter steckt oft eine Fuge, die bei vielen Häusern nie richtig abgedichtet wurde: der Übergang zwischen Bodenplatte und aufgehendem Mauerwerk. Diese Fuge wird von innen verpresst und mit einer Dichtkehle in die Abdichtung eingebunden.

**Button:** Kostenlose Diagnose in [ORT]

### Block 2 – Woran Du es erkennst

- Wasser oder Pfützen entlang der Wand am Boden, meist nach Starkregen, Schneeschmelze oder bei hohem Grundwasser.
- Feuchte, verfärbte oder verschimmelte Sockelleisten; Wasserflecken am unteren Wandrand.
- Modriger Geruch, der nach Regen stärker wird.
- Abblätternder Putz und Salzbildung in einem schmalen Band direkt über dem Boden.
- Die Wand darüber ist sonst weitgehend trocken.

Hinweise, keine Diagnose. Ähnlich sieht es aus, wenn ein Riss im Boden, eine Rohrdurchführung oder eine undichte Leitung die Ursache ist – das grenzt der Befund ab.

### Block 3 – Woher es kommt

Zwischen der Bodenplatte und der Wand, die darauf steht, liegt eine Fuge. Sie ist eine der Schwachstellen jedes Kellers: Setzungen, Erschütterungen und dauerhafter Druck können sie rissig werden lassen; bei vielen Bestandsgebäuden war sie nie abgedichtet. Steht nach Regen Wasser im Erdreich an – weil der Boden wenig durchlässig ist, die Drainage fehlt oder die Außenabdichtung gealtert ist –, sucht es sich den einfachsten Weg: durch diese Fuge in den Keller. Fachleute sprechen von der Aufstandsfuge oder dem Wand-Sohlen-Anschluss. [BAUSUBSTANZ_SATZ]

### Block 4 – Wie die Sanierung arbeitet

**Das Prinzip:** Die Fuge wird von innen gezielt verschlossen und in die umgebende Abdichtung eingebunden. Zwei Dinge greifen ineinander: Ein Harz füllt die Fuge und alle Hohlräume dahinter, eine Dichtkehle aus Mörtel überbrückt den Übergang an der Oberfläche.

**Der Ablauf bei [BETRIEB_KURZ]:**

1. **Befund.** Wann tritt das Wasser auf, wo genau, wie viel? Boden, Wand, Rohrdurchführungen und Risse werden geprüft, um sicherzugehen, dass die Fuge die Ursache ist – und nicht nur der Austrittspunkt.
2. **Freilegen.** Der Estrich wird entlang der Wand eingeschnitten und ein etwa 15–20 cm breiter Streifen entfernt, damit die Fuge zugänglich ist.
3. **Vorbereiten und Dichtkehle.** Der Bereich wird mit einer Dichtschlämme vorbereitet; dann wird eine abgerundete Dichtkehle aus druckwasserfestem Mörtel ausgebildet.
4. **Verpressen.** Nach dem Aushärten werden im festen Abstand Bohrungen schräg bis auf die Bodenplatte gesetzt und mit Packern versehen. Durch sie wird ein Harz in die Fuge gepresst. Läuft gerade Wasser, wird zuerst ein schnell schäumendes Harz eingebracht, das den Wassereintritt stoppt; danach ein elastisches Harz, das die Fuge dauerhaft und beweglich schließt und alle Hohlräume füllt.
5. **Einbinden und dokumentieren.** Die Kehle wird in die Flächenabdichtung eingebunden (Innenabdichtung oder Dichtband in der Abdichtungslage), der Boden wird wiederhergestellt. Fotos, Bohrbild und Materialien werden festgehalten.

### Block 5 – Was Du wissen solltest

**Meist ist es ein Baustein, nicht die ganze Lösung.** Wo Wasser durch die Fuge kommt, ist oft auch die Wand seitlich belastet. Dann gehört der Wand-Boden-Anschluss zu einer Innenabdichtung dazu. Ob nur die Fuge oder auch die Fläche saniert werden muss, sagt der Befund.

**Bei Beton geht es anders.** In Kellern aus wasserundurchlässigem Beton (Weiße Wanne, Tiefgarage) wird nach dem Verpressen ein spezielles Dichtband über die Fuge geklebt. Das ist ein eigenes System.

**Ein Riss im Boden sieht ähnlich aus.** Deshalb wird vor dem Angebot geprüft, woher das Wasser wirklich kommt – eine Rohrdurchführung oder eine undichte Leitung wird anders behandelt.

Verwandte Leistungen: → Innenabdichtung · → Rissverpressung

### Block 6 – Was danach kommt

Der Estrichstreifen wird nach dem Aushärten wieder geschlossen. Die Kehle bleibt sichtbar, wenn kein Putz- oder Bodenaufbau darüber kommt – sie ist Teil der Abdichtung und darf nicht abgeschlagen werden. Regale und Einbauten sollten nicht direkt an die Kehle gestellt werden, damit sie kontrollierbar bleibt. Wurde zugleich eine Innenabdichtung ausgeführt, gelten deren Trocknungs- und Putzschritte.

### Block 7 – Häufige Fragen

*Warum nicht einfach die Fuge mit Silikon oder Dichtmasse zuschmieren?* – Weil das Wasser mit Druck von hinten kommt. Eine Oberflächenmasse hält dem nicht stand und löst sich nach dem nächsten Regen. Das Harz wird deshalb in die Fuge und die Hohlräume dahinter gepresst, und die Kehle übernimmt den Übergang an der Oberfläche.

*Muss der ganze Boden raus?* – Nein. Geöffnet wird nur ein schmaler Streifen entlang der betroffenen Wand, etwa 15–20 cm breit. Der übrige Boden bleibt.

*Hält das auch bei drückendem Wasser?* – Das eingesetzte Harz ist auf Wasser unter Druck ausgelegt und reagiert bei Wasserkontakt zu einem elastischen Schaum, der den Eintritt stoppt. Bei dauerhaft drückendem Wasser wird der Anschluss aber Teil einer Innenabdichtung, die auch Wand und ggf. Bodenplatte einbezieht.

*Wie lange dauert das?* – Für einen einzelnen Wandabschnitt in der Regel ein bis drei Arbeitstage einschließlich Aushärtezeiten. Der konkrete Zeitplan steht im Angebot.

*Was kostet die Abdichtung des Wand-Boden-Anschlusses in [ORT]?* – Die Länge der betroffenen Fuge, der Bodenaufbau, die Wasserbelastung und die Frage, ob eine Innenabdichtung dazugehört, bestimmen den Preis. Nach dem Befund bekommst Du ein Festpreisangebot mit erklärten Positionen.

## F.5 Rissverpressung (/rissverpressung/)

### Block 1 – Hero

**H1:** Rissverpressung in [ORT]: Wenn Wasser durch einen Riss oder eine Fuge kommt

**Text:** Ein Riss in der Kellerwand, aus dem es nach Regen feucht wird oder sogar läuft. Eine Arbeitsfuge im Beton, die nass bleibt. Solche Schwachstellen sind eng begrenzt – und werden gezielt geschlossen: Erst wird das Wasser gestoppt, dann der Riss dauerhaft und beweglich abgedichtet. Von innen, ohne Aufgraben.

**Button:** Kostenlose Diagnose in [ORT]

### Block 2 – Woran Du es erkennst

- Ein eng begrenztes, linien- oder punktförmiges Schadensbild statt einer feuchten Fläche.
- Feuchte oder nasse Spur entlang eines Risses, manchmal mit Kalkfahnen oder Ablagerungen.
- Wasser, das bei bestimmten Wetterlagen sichtbar aus dem Riss austritt oder läuft.
- Arbeitsfugen im Beton (waagerechte Linien, an denen betoniert wurde), die dunkel und feucht bleiben.
- Feuchte Stellen um Rohr- oder Kabeldurchführungen.

Hinweise, keine Diagnose. Nicht jeder Riss führt Wasser, und nicht jeder feuchte Riss ist allein die Ursache – das grenzt der Befund ab.

### Block 3 – Woher es kommt

Risse entstehen durch Belastung, Schwinden beim Aushärten von Beton, Setzungen des Bodens oder Temperaturspannungen. Solange sie trocken sind, sind viele davon harmlos. Zum Problem werden sie, wenn Wasser im Erdreich an der Wand ansteht und der Riss der einfachste Weg nach innen ist. Ähnlich verhalten sich Arbeitsfugen im Beton und schlecht eingebundene Rohrdurchführungen. Fachleute sprechen von wasserführenden Rissen und Fugen. Sie sind oft der Grund, wenn ein Keller trotz früherer Maßnahmen wieder feucht wurde. [BAUSUBSTANZ_SATZ]

### Block 4 – Wie die Sanierung arbeitet

**Das Prinzip:** In den Riss wird über Bohrungen ein Harz gepresst, das ihn in seiner ganzen Tiefe füllt. Das geschieht zweistufig: Ein schnell schäumendes Harz stoppt zuerst das fließende Wasser; ein elastisches Harz schließt danach den Riss dauerhaft und bleibt beweglich, damit er bei Temperatur- und Lastwechseln nicht wieder aufreißt. Beide Schritte werden nicht vermischt – jeder hat seine Aufgabe.

**Der Ablauf bei [BETRIEB_KURZ]:**

1. **Befund.** Rissverlauf, Rissbreite, ob der Riss aktiv arbeitet, ob und wie viel Wasser fließt, welcher Untergrund (Mauerwerk oder Beton), ob Hohlräume dahinter liegen. Nicht jeder Riss braucht eine Verpressung – das sagen wir Dir.
2. **Bohren und Packer setzen.** Schräg zum Riss werden im festen Abstand Bohrungen gesetzt, die den Riss in der Tiefe kreuzen. Darin werden Packer (Injektionsventile) eingebaut.
3. **Wasser stoppen.** Bei fließendem Wasser wird das schäumende Harz injiziert, bis der Wasserfluss steht.
4. **Dauerhaft schließen.** Anschließend wird das elastische Harz eingepresst, bis der Riss in seiner gesamten Tiefe gefüllt ist. Der Druck richtet sich nach dem Untergrund – Beton verträgt mehr als Mauerwerk.
5. **Verschließen und einbinden.** Packer entfernen, Bohrlöcher mit Mörtel schließen, angrenzende Flächenabdichtung prüfen und bei Bedarf ergänzen. Dokumentation mit Fotos und Materialien.

### Block 5 – Was Du wissen solltest

**Ein Riss ist oft nur der Austrittspunkt.** Wo Wasser durch einen Riss kommt, steht es meist auch an der Fläche daneben an. Ob die Verpressung allein reicht oder eine Innenabdichtung dazugehört, entscheidet der Befund.

**Bei Beton folgt ein zweiter Schritt.** In wasserundurchlässigem Beton (Weiße Wanne, Tiefgarage) wird nach der Verpressung ein Dichtband über Fuge oder Riss geklebt – ein eigenes System, das die Injektion ergänzt.

**Verpressung ist nicht Verfestigung.** Bei mürbem Mauerwerk mit ausgewaschenen Fugen und Hohlräumen geht es um Stabilität, nicht um Dichtheit – dafür gibt es ein eigenes Verfahren. Wir grenzen das im Befund ab.

**Kein Fall für die Eigenanwendung.** Rissverpressung braucht Druckgeräte, das passende Harz für den jeweiligen Fall und Erfahrung mit dem Untergrund.

Verwandte Leistungen: → Innenabdichtung · → Wand-Boden-Anschluss

### Block 6 – Was danach kommt

Das Harz ist nach kurzer Zeit ausreagiert; der Bereich kann nach dem Verschließen der Bohrlöcher verputzt werden. Trat das Wasser über längere Zeit aus, ist der umgebende Putz meist salzbelastet – dann folgt ein Sanierputz auf dem betroffenen Bereich. Beobachte die Stelle nach den nächsten Starkregen; bleibt sie trocken, ist die Sache erledigt. Sollte sich an anderer Stelle Feuchtigkeit zeigen, ist das kein Versagen der Verpressung, sondern ein Hinweis auf eine zweite Ursache – sag uns Bescheid.

### Block 7 – Häufige Fragen

*Ist jeder Riss ein Problem?* – Nein. Viele Risse sind trocken und harmlos. Zu prüfen sind Risse, die Wasser führen, sich verändern oder im erdberührten Bereich liegen. Das beurteilt der Befund – auch, ob ein Riss auf ein statisches Problem hinweist, das anders zu behandeln ist.

*Warum zwei Harze?* – Weil zwei Aufgaben zu lösen sind. Fließendes Wasser muss zuerst gestoppt werden, sonst spült es das Abdichtungsmaterial aus. Erst dann kann der Riss mit einem elastischen Harz dauerhaft gefüllt werden. Ein einziges Material kann nicht beides.

*Hält die Verpressung, wenn der Riss weiter arbeitet?* – Das elastische Harz bleibt beweglich und macht Bewegungen im üblichen Rahmen mit. Bei Rissen, die sich deutlich weiter öffnen, muss zuerst die Ursache der Bewegung geklärt werden.

*Wie lange dauert eine Rissverpressung?* – Einzelne Risse werden meist an einem Tag verpresst, einschließlich Vorbereitung und Verschluss der Bohrlöcher. Mehrere Risse oder Fugen entsprechend länger. Der Zeitplan steht im Angebot.

*Was kostet eine Rissverpressung in [ORT]?* – Länge und Zahl der Risse, Untergrund, Wasserbelastung und die Frage, ob eine Flächenabdichtung dazugehört, bestimmen den Preis. Nach dem Befund bekommst Du ein Festpreisangebot mit erklärten Positionen.

## F.6 Sanierputz (/sanierputz/)

### Block 1 – Hero

**H1:** Sanierputz in [ORT]: Wenn Putz und Farbe abplatzen, obwohl die Wand trocken ist

**Text:** Die Wand ist trockengelegt oder abgedichtet – und trotzdem kommen weiße Ablagerungen wieder, der Putz platzt ab, die Farbe hält nicht. Dahinter stecken Salze, die das Wasser über Jahre in die Wand gebracht hat. Ein Sanierputz nach WTA gibt ihnen Platz, ohne dass die Oberfläche Schaden nimmt.

**Button:** Kostenlose Diagnose in [ORT]

### Block 2 – Woran Du es erkennst

- Weiße, krustige oder flauschige Ablagerungen, die nach dem Abbürsten wiederkommen.
- Putz, der absandet, sich löst oder hohl klingt – auch wenn die Wand sich nicht mehr feucht anfühlt.
- Farbe, die blättert oder Blasen wirft, obwohl mehrfach überstrichen wurde.
- Ausbesserungen halten immer kürzer.
- Die Wand wurde bereits trockengelegt oder abgedichtet, oder ihre Feuchtigkeitsursache wird gerade behoben.

Hinweise, keine Diagnose. Wichtig ist die Frage, ob die Ursache der Feuchtigkeit behoben ist – sonst ist der Sanierputz die falsche Reihenfolge.

### Block 3 – Woher es kommt

Wasser, das durch eine Wand wandert, bringt Salze mit: aus dem Boden, aus dem Mörtel, aus dem Stein. Beim Trocknen bleiben sie zurück und reichern sich über Jahre in Putz und Mauerwerk an. Diese Salze haben zwei unangenehme Eigenschaften: Sie ziehen Feuchtigkeit aus der Luft, sodass die Wand klamm bleibt, obwohl kein Wasser mehr nachkommt. Und sie brauchen beim Kristallisieren mehr Platz als in gelöster Form – so sprengen sie Putz und Farbe von innen. Fachleute sprechen von hygroskopischen Salzen und Salzsprengung. Ein normaler Putz kommt damit nicht zurecht; er ist zu dicht und hat keinen Platz für die Salze.

### Block 4 – Wie die Sanierung arbeitet

**Das Prinzip:** Ein Sanierputz hat innen ein großes Volumen feiner Luftporen. In ihnen lagern sich die Salze ab, ohne die Oberfläche zu zerstören. Gleichzeitig lässt der Putz Wasserdampf ungehindert nach außen, damit die Wand weiter austrocknen kann, und nimmt an der Oberfläche kein Wasser auf. Ein Sanierputzsystem besteht aus mehreren Lagen, die aufeinander abgestimmt sind – nach WTA-Merkblatt.

**Der Ablauf bei [BETRIEB_KURZ]:**

1. **Befund.** Feuchtigkeit und Salzbelastung messen, Ursache klären. Ist die Feuchtequelle nicht behoben, wird zuerst sie behandelt – Horizontalsperre, Innenabdichtung oder Rissverpressung – und der Sanierputz folgt danach.
2. **Altputz entfernen.** Geschädigter Putz wird bis deutlich über die sichtbare Schadgrenze hinaus abgeschlagen – in der Regel rund 80 cm –, weil Salze und Feuchtigkeit weiter reichen als der Fleck. Fugen werden ausgekratzt, der Untergrund gereinigt. Bei starker Salzbelastung wird ein Salzumwandler aufgebracht.
3. **Haftbrücke.** Ein Vorspritzmörtel sorgt dafür, dass der Sanierputz auf dem Untergrund hält.
4. **Sanierputz auftragen.** In der nötigen Schichtdicke, je nach Versalzungsgrad in einer oder mehreren Lagen, mit den vorgesehenen Wartezeiten.
5. **Oberfläche und Anstrich.** Feinputz nach Wunsch, dann ein Anstrich, der Wasserdampf durchlässt – in der Regel eine Silikatfarbe. Dokumentation mit Messwerten, Aufbau und Materialien.

### Block 5 – Was Du wissen solltest

**Sanierputz ist keine Abdichtung.** Er beseitigt nicht die Ursache der Feuchtigkeit, er bewältigt ihre Folgen. Wird er auf eine Wand aufgebracht, in die weiter Wasser eindringt, ist sein Speicher irgendwann erschöpft. Deshalb kommt er nach der Trockenlegung oder Abdichtung – nie statt ihrer.

**Er braucht den richtigen Anstrich.** Dispersionsfarbe, Tapete, Gipsspachtel oder Fliesen würden die Oberfläche dicht machen und die Wirkung aufheben. Auf einen Sanierputz gehört ein diffusionsoffener Anstrich.

**Er ist Teil fast jeder Sanierung.** Nach einer Horizontalsperre, Flächensperre oder Innenabdichtung bleiben die Salze in der Wand. Deshalb ist der Sanierputz auf diesen Seiten immer der letzte Schritt.

Verwandte Leistungen: → Horizontalsperre · → Innenabdichtung

### Block 6 – Was danach kommt

Der Putz braucht Zeit zum Aushärten, bevor gestrichen wird; die Wartezeiten stehen im Angebot. In den ersten Wochen kann die Wand noch Feuchtigkeit abgeben – das ist gewollt. Später: nur mit dampfdurchlässigen Farben streichen, keine Tapeten, keine dichten Beschichtungen, keine Gipsprodukte. Möbel mit etwas Abstand zur Wand aufstellen, regelmäßig lüften. Bei fachgerechtem Aufbau und behobener Ursache hält ein Sanierputz viele Jahre.

### Block 7 – Häufige Fragen

*Reicht es nicht, den alten Putz einfach zu erneuern?* – Nein. Ein normaler Putz auf salzbelastetem Untergrund wird von den Salzen erneut gesprengt – oft schon nach ein bis zwei Wintern. Der Sanierputz ist genau dafür gemacht, die Salze aufzunehmen.

*Kann Sanierputz auf eine feuchte Wand?* – Ja, das ist sein Zweck – aber nur, wenn die Ursache der Feuchtigkeit behoben ist oder gleichzeitig behoben wird. Auf einer Wand, die weiter Wasser aufnimmt, hilft er nur vorübergehend.

*Wie lange hält ein Sanierputz?* – Bei fachgerechtem Aufbau, behobener Ursache und richtigem Anstrich viele Jahre. Wie lange genau, hängt von der Salzmenge in der Wand und der Nutzung des Raums ab.

*Braucht es eine Dampfsperre oder Folie unter dem Putz?* – Nein, im Gegenteil: Der Putz muss atmen können, um Feuchtigkeit abzugeben. Eine dichte Schicht dahinter oder davor würde seine Wirkung aufheben.

*Was kostet Sanierputz in [ORT]?* – Fläche, Schichtdicke (nach Versalzungsgrad), Umfang der Vorarbeiten und der Anstrich bestimmen den Preis. Nach dem Befund bekommst Du ein Festpreisangebot; wenn der Sanierputz Teil einer größeren Sanierung ist, steht er dort als eigene Position.

## F.7 Block 8 – Der nächste Schritt (auf allen sechs Leistungsseiten identisch)

**H2:** Du musst heute noch nicht wissen, welche Sanierung Du brauchst.

**Text:** Der erste Schritt ist, die Ursache zu verstehen. Beim Termin in [ORT] oder [REGION] sehen wir uns Deine Wand an, messen die Feuchtigkeit und erklären Dir, was wir sehen – in Ruhe und in verständlichen Worten. Manchmal ist das Ergebnis eine Sanierung. Manchmal eine Beobachtung über einige Wochen oder ein Hinweis zum Lüften. Was es nicht ist: ein Verkaufsgespräch.

**Buttons:** Kostenlose Diagnose anfragen (→ /diagnose/) · [TELEFON] anrufen (tel:[TELEFON_LINK])

**Kontaktblock:** [BETRIEB] · [ADRESSE], [PLZ] [SITZ_ORT] · [TELEFON] · [EMAIL] · Einsatzgebiet: [EINSATZGEBIET] · Zertifizierter BKM-Fachbetrieb

## F.8 Optionale Leistungsmodule (je Betrieb zuschaltbar)

*Vier weitere Leistungen in derselben Acht-Block-Struktur, etwas kompakter. Sie liegen in der Master-Site als fertige Seiten vor und werden je Betrieb per Steckbrief (Feld 26) ein- oder ausgeblendet. Nicht gewählte Modulseiten werden im Klon gelöscht, ihre Menü- und Übersichtseinträge ebenfalls. Block 8 (F.7) gilt auch hier.*

### M1 – Schimmel und Kondensation (/schimmel-kondensation/)

**Title:** Schimmel an kalten Wänden? Anti-Kondensationsbeschichtung in [ORT] · **Meta:** Schimmel in Ecken, hinter Möbeln, an Fensterlaibungen – ohne Nässe von außen? Ursache klären, Schimmel beseitigen, Oberfläche trocken halten. Fachbetrieb in [ORT].

**Block 1 – Hero.** H1: Schimmel und Kondensation in [ORT]: Wenn die Feuchtigkeit aus der Raumluft kommt · Text: Schimmel in einer Raumecke, hinter dem Schrank, an der Fensterlaibung – aber kein Feuchtestreifen, keine Salzränder. Dann kommt das Wasser oft nicht durch die Wand, sondern aus der Luft: Warme Raumluft schlägt sich an einer kalten Oberfläche nieder. Das wird anders behandelt als eindringende Feuchtigkeit – und genau das klären wir zuerst. · Button: Kostenlose Diagnose in [ORT]

**Block 2 – Woran Du es erkennst.** Schimmel oder Feuchtigkeit in Außenecken, an Fensterlaibungen, hinter Möbeln an Außenwänden · Im Keller vor allem im Sommer, wenn warme Luft hereingelüftet wird · Die Wand fühlt sich kalt an, die Stelle ist flächig feucht, ohne waagerechten Streifen und ohne weiße Ränder · Beschlagene Fenster am Morgen, hohe Luftfeuchte im Raum · Hinweise, keine Diagnose: Schimmel am unteren Ende einer feuchten Wand mit Salzrändern ist eher die Folge eindringender Feuchtigkeit.

**Block 3 – Woher es kommt.** Warme Luft kann viel Wasser aufnehmen. Trifft sie auf eine Oberfläche, die kälter ist als der Taupunkt, gibt sie einen Teil davon als feine Tröpfchen ab – wie eine kalte Flasche im Sommer. Kalte Stellen sind Außenecken, Fensterlaibungen, Wände hinter Möbeln, Wärmebrücken und im Sommer die kühlen Kellerwände. Auf der feuchten Oberfläche findet Schimmel seinen Nährboden. Fachleute sprechen von Kondensation oder Tauwasser. Sie hat nichts mit einer undichten Wand zu tun.

**Block 4 – Wie die Sanierung arbeitet.** Prinzip: Die Oberfläche darf nicht mehr dauerhaft nass sein. Eine Anti-Kondensationsbeschichtung mit sehr vielen winzigen Poren nimmt anfallendes Kondenswasser auf und gibt es später als Wasserdampf wieder an den Raum ab – die Oberfläche bleibt trocken. Bei ausgeprägten Wärmebrücken kann eine Innendämmung aus Kalziumsilikatplatten dazukommen. Ablauf bei [BETRIEB_KURZ]: 1. Befund – Oberflächentemperatur, Raumklima und Feuchteverteilung messen; eindringende Feuchtigkeit ausschließen. 2. Schimmel beseitigen – befallene Stellen mit einem Vorreiniger behandeln, lose Tapeten und Anstriche entfernen. 3. Beschichtung – in mindestens zwei Arbeitsgängen mit Zwischentrocknung, vollflächig einschließlich Ecken und Laibungen. 4. Bei Bedarf Innendämmung – Kalziumsilikatplatten auf Wänden, die nicht zugleich von unten oder von der Seite feucht werden. 5. Hinweise zu Lüften und Heizen – ohne sie hält keine Maßnahme dauerhaft.

**Block 5 – Was Du wissen solltest.** Gegen Feuchtigkeit, die durch die Wand eindringt, hilft die Beschichtung nicht – wer Kondensat und Baufeuchte verwechselt, behandelt das falsche Problem. · Nicht für Flächen mit ständiger Wassereinwirkung (Duschwände). · Dichte Farben oder Tapeten darüber würden die Poren verschließen. · Bei größerem Befall (als Orientierung etwa ein halber Quadratmeter) sollte die Beseitigung fachlich begleitet werden, besonders wenn Kinder, ältere oder empfindliche Menschen im Haus leben. Verwandte Leistungen: → Horizontalsperre · → Innenabdichtung

**Block 6 – Was danach kommt.** Die beschichtete Fläche bleibt matt und wird nicht überstrichen. Entscheidend ist das Verhalten im Raum: im Sommer den Keller nachts oder frühmorgens lüften, nicht am warmen Nachmittag; in Wohnräumen regelmäßig stoßlüften, Möbel mit Abstand zur Außenwand. Kontrolle nach der ersten Heizperiode.

**Block 7 – Häufige Fragen.** *Reicht es nicht, den Schimmel abzuwischen und zu überstreichen?* – Nein. Solange die Oberfläche kalt und feucht bleibt, kommt er wieder. Erst die Ursache – Kondensat oder eindringende Feuchtigkeit – dann die Maßnahme. · *Woher weiß ich, ob es Kondensat ist?* – Von außen nicht sicher. Hinweise: keine Salzränder, kein Feuchtestreifen, Lage an kalten Stellen, Auftreten im Sommer (Keller) oder in der Heizperiode (Wohnräume). Sicherheit gibt die Messung von Oberflächentemperatur und Wandfeuchte. · *Hilft ein Luftentfeuchter?* – Bei Kondensat kann er ein Baustein sein, ersetzt aber weder das Lüften noch die Behandlung der kalten Oberfläche. Kommt die Feuchtigkeit durch die Wand, entfernt er nur, was die Wand ohnehin abgibt. · *Kann ich das selbst machen?* – Die Beschichtung selbst ist mit Pinsel oder Rolle machbar; die Diagnose ist der kritische Schritt. Wir sagen Dir beim Termin, ob Du es selbst machen kannst. · *Was kostet das in [ORT]?* – Fläche, Vorarbeiten und die Frage, ob eine Innendämmung nötig ist, bestimmen den Preis. Nach dem Befund bekommst Du ein Festpreisangebot.

### M2 – Fassadenschutz (/fassadenschutz/)

**Title:** Fassadenschutz in [ORT] – Hydrophobierung gegen Schlagregen · **Meta:** Fassade wird bei Regen dunkel, Frostabplatzungen, Algen? Unsichtbare Hydrophobierung für saugfähige Fassaden in [ORT] und [REGION]. Fachbetrieb vor Ort.

**Block 1 – Hero.** H1: Fassadenschutz in [ORT]: Wenn die Fassade Regen aufsaugt · Text: Eine Fassade, die bei Regen dunkel wird, nimmt Wasser auf. Über die Jahre folgen Frostabplatzungen, Algen und Moos, Kalkfahnen – und eine Außenwand, die schlechter dämmt. Eine Hydrophobierung macht die gereinigte Fassade wasserabweisend, bleibt unsichtbar und lässt die Wand weiter atmen. · Button: Kostenlose Diagnose in [ORT]

**Block 2 – Woran Du es erkennst.** Fassade dunkelt bei Regen großflächig durch und trocknet langsam · Abplatzungen an Putz oder Klinker nach dem Winter · Grüner Belag, Moos oder Algen, vor allem an der Wetterseite · Weiße Kalkfahnen oder Ausblühungen an Fugen · Innen kühle Außenwände, höhere Heizkosten · Hinweise, keine Diagnose: Feuchtigkeit im Sockelbereich mit waagerechtem Streifen ist meist aufsteigende Feuchtigkeit – die wird zuerst behandelt.

**Block 3 – Woher es kommt.** Klinker, Putz, Kalksandstein und Fugenmörtel sind porös. Schlagregen wird kapillar aufgesaugt; bei Frost sprengt das gefrierende Wasser Putz und Stein, in feuchten Poren siedeln sich Algen und Moose an. Eine nasse Fassade dämmt zudem schlechter. Fachleute sprechen von Schlagregenbelastung saugfähiger Fassaden.

**Block 4 – Wie die Sanierung arbeitet.** Prinzip: Ein wasserabweisendes Mittel zieht tief in den Baustoff ein und macht die Porenwände wasserabweisend. Regen perlt ab, Wasserdampf von innen kann weiter entweichen; die Optik bleibt unverändert. Ablauf bei [BETRIEB_KURZ]: 1. Befund – Untergrund (Klinker, Putz, Kalksandstein, Sichtbeton, WDVS), Saugfähigkeit, Risse, Bewuchs, Sockelfeuchte. 2. Reinigung – gesamte Fassade säubern, Algen und Moos entfernen. 3. Instandsetzung – Risse und Fehlstellen schließen, denn an offenen Rissen dringt Wasser hinter die Imprägnierung. 4. Abkleben von Fenstern, Glas und Metall. 5. Hydrophobierung – je nach Untergrund im Flutungsverfahren oder zweimal nass in nass, bis der Baustoff gesättigt ist; 24 Stunden regenfrei. 6. Abperltest und Dokumentation.

**Block 5 – Was Du wissen solltest.** Nicht auf Gips, dichten Natursteinen oder Marmor; WDVS nur mit dem dafür geeigneten Mittel. · Nicht gegen aufsteigende Feuchtigkeit im Sockel und nicht im erdberührten Bereich – dort gelten Horizontalsperre und Abdichtung. · Risse müssen vorher geschlossen sein; eine Hydrophobierung auf gerissener Fassade sperrt Wasser ein statt aus. · Terrassen, Pflaster und Garagenhöfe werden mit einem eigenen Mittel imprägniert. Verwandte Leistungen: → Horizontalsperre · → Rissverpressung

**Block 6 – Was danach kommt.** Die Fassade sieht aus wie vorher, nur bleibt sie bei Regen hell. Nach der Trocknung nichts überstreichen, was die Wirkung aufheben könnte; ein späterer Anstrich sollte mit uns abgestimmt werden. Kontrolle des Abperleffekts nach einigen Jahren; eine Auffrischung ist möglich.

**Block 7 – Häufige Fragen.** *Sieht man die Behandlung?* – Nein. Die Imprägnierung bildet keinen Film und verändert Farbe und Struktur nicht. · *Kann die Wand danach noch atmen?* – Ja. Die Poren bleiben offen für Wasserdampf; nur flüssiges Wasser wird abgewiesen. · *Geht das auch auf gestrichenen Fassaden?* – Auf neuen Dispersions- und Mineralfarbanstrichen ja; das erhöht deren Haltbarkeit. Alte, kreidende Anstriche werden vorher beurteilt. · *Wie lange hält das?* – Viele Jahre; das hängt von Untergrund und Wetterseite ab. Eine Überprüfung nach fünf bis zehn Jahren ist sinnvoll. · *Was kostet Fassadenschutz in [ORT]?* – Fläche, Untergrund, Reinigungs- und Instandsetzungsaufwand und Gerüst bestimmen den Preis. Nach dem Befund bekommst Du ein Festpreisangebot.

### M3 – Bodenbeschichtung Keller und Garage (/bodenbeschichtung/)

**Title:** Bodenbeschichtung für Keller und Garage in [ORT] · **Meta:** Kellerboden staubt, ist uneben oder feucht? Abdichtung der Bodenplatte und belastbare Nutzschicht in [ORT] – nach einem Tag befahrbar. Fachbetrieb vor Ort.

**Block 1 – Hero.** H1: Bodenbeschichtung in [ORT]: Wenn der Keller- oder Garagenboden staubt, uneben oder feucht ist · Text: Ein Boden, der sandet, Risse zeigt oder dunkle Feuchteflecken hat, braucht zwei Dinge, die man auseinanderhalten muss: eine Abdichtung, wenn Feuchtigkeit von unten kommt, und eine belastbare Nutzschicht, damit er eben, sauber und robust wird. Beides klären wir vorher – eine Beschichtung allein ist keine Abdichtung. · Button: Kostenlose Diagnose in [ORT]

**Block 2 – Woran Du es erkennst.** Boden staubt oder sandet beim Fegen, ist uneben oder rissig · Dunkle Feuchteflecken oder Ausblühungen am Boden, feuchte Kartons auf dem Boden · Feuchter Übergang zwischen Wand und Boden · Garagenboden mit Abplatzungen, Öl- und Reifenspuren, die sich nicht mehr entfernen lassen · Hinweise, keine Diagnose: ob Feuchtigkeit von unten drückt, kondensiert oder über die Fuge kommt, entscheidet über den Aufbau.

**Block 3 – Woher es kommt.** Alte Bodenplatten haben oft keine oder eine gealterte Abdichtung; Bodenfeuchte steigt kapillar auf, nach Regen kann Wasser leicht drücken. Dazu fehlt vielen Kellerböden eine Nutzschicht – der rohe Beton verschleißt, staubt und reißt. Auf kalten Böden kann zusätzlich Kondensat entstehen. Fachleute trennen deshalb Bodenabdichtung (gegen Wasser) und Bodenbeschichtung (Nutzschicht).

**Block 4 – Wie die Sanierung arbeitet.** Prinzip: Jede Schicht hat eine Aufgabe – Abdichtung, Grundierung, Ausgleich, Nutzschicht, Versiegelung. Ablauf bei [BETRIEB_KURZ]: 1. Befund – Feuchteursache am Boden, Tragfähigkeit und Ebenheit des Untergrunds, Risse, Fugen, Nutzung (Keller, Garage, Werkstatt). 2. Untergrund vorbereiten – Anstriche, lose Teile, Öl und Staub vollständig entfernen (schleifen oder strahlen), Fehlstellen und Risse schließen. 3. Abdichtung – nur bei Feuchtigkeit von unten: mineralische Abdichtung der Bodenplatte mit Dichtkehle zur Wand, in zwei Lagen. 4. Grundierung – Epoxid-Grundierung, frisch mit Quarzsand abgestreut, damit die Nutzschicht hält; Wand-Boden-Übergang mit Dichtband eingebunden. 5. Nutzschicht – selbstverlaufende zementäre Beschichtung, je nach Bedarf 3 bis 35 mm, mit Stachelwalze entlüftet. 6. Versiegelung – in Garagen zwingend, in Kellern auf Wunsch: zweilagig gegen Abrieb, Öl und Wasser. Begehbar nach wenigen Stunden, befahrbar nach 24 Stunden.

**Block 5 – Was Du wissen solltest.** Eine Bodenbeschichtung ist keine Bauwerksabdichtung; bei Feuchtigkeit von unten kommt die Abdichtung zuerst, sonst löst sich jede Beschichtung. · Bewegungs- und Randfugen werden übernommen, nicht überbeschichtet. · Die Versiegelung braucht einige Tage, bevor sie Wasser und Chemie verträgt. · Bei drückendem Wasser wird der Boden Teil einer Innenabdichtung von Wand und Bodenplatte. Verwandte Leistungen: → Innenabdichtung · → Wand-Boden-Anschluss

**Block 6 – Was danach kommt.** Begehbar nach etwa drei bis vier Stunden, mit dem Pkw befahrbar nach 24 Stunden; die Versiegelung ist nach drei Tagen mechanisch und nach sieben Tagen gegen Wasser und Chemikalien belastbar. Reinigung mit milden Reinigern; Du bekommst eine Pflegeanleitung.

**Block 7 – Häufige Fragen.** *Reicht ein Bodenanstrich aus dem Baumarkt?* – Für einen staubenden, trockenen Boden vielleicht kurzfristig. Auf feuchtem oder ungeeignet vorbereitetem Untergrund löst sich jeder Anstrich. Der Unterschied liegt in Untergrundvorbereitung, Abdichtung und Schichtaufbau. · *Kann der Boden auch bei Feuchtigkeit beschichtet werden?* – Ja, wenn vorher abgedichtet wird. Der Befund zeigt, ob das nötig ist. · *Wie lange ist der Raum nicht nutzbar?* – Je nach Umfang zwei bis vier Arbeitstage; danach die Wartezeiten bis zur vollen Belastbarkeit. · *Geht das auch in der Garage mit Autoverkehr?* – Ja, mit Versiegelung. Befahrbar nach 24 Stunden. · *Was kostet eine Bodenbeschichtung in [ORT]?* – Fläche, Untergrundvorbereitung, ob eine Abdichtung nötig ist, Schichtdicke und Versiegelung bestimmen den Preis. Nach dem Befund bekommst Du ein Festpreisangebot.

### M4 – Mauerwerksverfestigung (/mauerwerksverfestigung/)

**Title:** Mauerwerksverfestigung in [ORT] – mürbes Mauerwerk stabilisieren · **Meta:** Bröckelnder Mörtel, Hohlräume, lockere Steine im Altbau? Verfestigung durch Injektion in [ORT] und [REGION] – als Grundlage für Trockenlegung und Abdichtung.

**Block 1 – Hero.** H1: Mauerwerksverfestigung in [ORT]: Wenn Mörtel bröckelt und Steine sich lockern · Text: Altes Mauerwerk kann mit der Zeit mürbe werden: Der Mörtel wird ausgewaschen, Hohlräume entstehen, Steine lockern sich. Bevor so eine Wand trockengelegt oder abgedichtet werden kann, muss sie wieder fest sein. Dafür wird ein dünnflüssiges Harz oder ein mineralischer Mörtel über Bohrungen eingebracht, der Hohlräume füllt und die Steine wieder verbindet. · Button: Kostenlose Diagnose in [ORT]

**Block 2 – Woran Du es erkennst.** Mörtel rieselt aus den Fugen, Fugen sind tief ausgewaschen · Steine sitzen locker, klingen hohl oder lassen sich bewegen · Risse, die entlang der Fugen verlaufen, Ausbrüche · Bruchstein- oder Ziegelmauerwerk in Altbauten, oft in Verbindung mit langjähriger Feuchtigkeit · Hinweise, keine Diagnose: ob die Tragfähigkeit betroffen ist, beurteilt bei Bedarf ein Tragwerksplaner.

**Block 3 – Woher es kommt.** Verwitterung, Setzungen, Erschütterungen und vor allem jahrzehntelange Feuchtigkeit lassen die Bindekraft des Mörtels nachlassen; Wasser wäscht Bestandteile aus, Frost sprengt Fugen. Zurück bleiben Hohlräume und ein Verbund, der nicht mehr trägt. Fachleute sprechen von Materialermüdung und Auswaschung. Häufig betroffen: Bruchsteinkeller und Ziegelmauerwerk vor 1920.

**Block 4 – Wie die Sanierung arbeitet.** Prinzip: Über Bohrungen wird ein sehr dünnflüssiges Harz oder ein fließfähiger mineralischer Mörtel in das Mauerwerk gepresst. Das Material dringt in Risse, Hohlräume und poröse Bereiche ein, härtet aus und verbindet lose Teile kraftschlüssig. Ablauf bei [BETRIEB_KURZ]: 1. Befund – Schadensursache, Hohlraumvolumen, Feuchtezustand, bei Bedarf statische Bewertung. 2. Vorbereitung – lose Teile entfernen, Ausbrüche schließen, Bereich reinigen; nasses Mauerwerk wird zuerst trockengelegt. 3. Injektion – Packer setzen, Harz bei niedrigem Druck einbringen, bis die Hohlräume gefüllt sind; größere Hohlräume mit fließfähigem Mörtel verfüllen. 4. Verschließen – Bohrlöcher mit Mörtel schließen. 5. Folgemaßnahmen – Horizontalsperre, Innenabdichtung oder Sanierputz, je nach Befund.

**Block 5 – Was Du wissen solltest.** Verfestigung ist keine Abdichtung; sie schafft die Grundlage dafür. · Sie ersetzt keine Ursachenbehebung – bleibt die Feuchtigkeit, bleibt das Problem. · Bei schweren strukturellen Schäden ist ein Tragwerksplaner einzubinden. · Kein Fall für die Eigenanwendung: Injektionstechnik, Materialwahl und Statik gehören in Fachhand. Verwandte Leistungen: → Horizontalsperre · → Rissverpressung

**Block 6 – Was danach kommt.** Nach dem Aushärten ist das Mauerwerk wieder tragfähig und kann trockengelegt, abgedichtet und verputzt werden. Die Reihenfolge der Folgemaßnahmen steht im Angebot.

**Block 7 – Häufige Fragen.** *Muss die Wand neu aufgemauert werden?* – In den meisten Fällen nicht. Die Verfestigung stabilisiert von innen, ohne die Wand zu öffnen; nur stark zerstörte Bereiche werden ausgebessert. · *Kann das von innen gemacht werden?* – Ja, in vielen Fällen, besonders wenn der Zugang von außen schwierig ist. · *Wie lange hält das?* – Bei fachgerechter Ausführung und behobener Feuchteursache über Jahrzehnte. · *Gilt das auch für denkmalgeschützte Gebäude?* – Ja, das Verfahren ist substanzschonend; Abstimmung mit der Denkmalbehörde übernehmen wir gern mit Dir. · *Was kostet eine Mauerwerksverfestigung in [ORT]?* – Das Hohlraumvolumen lässt sich vorher nur schätzen; deshalb bekommst Du nach dem Befund ein Angebot mit Festpreis für die Arbeiten und einer klaren Regel für den Materialverbrauch.

---

# TEIL G – DIAGNOSE-/KONTAKTSEITE (/diagnose/)

**H1:** Kostenlose Feuchtigkeitsdiagnose in [ORT] und [REGION]

**Intro:** Du hast eine feuchte Wand, einen nassen Keller oder einen Fleck, den Du nicht einordnen kannst? Hinterlasse hier Deine Kontaktdaten und, wenn Du möchtest, ein oder zwei Fotos. Wir melden uns innerhalb von 24 Stunden bei Dir, um einen Termin zu vereinbaren. Der Termin ist eine Schadensaufnahme, kein Verkaufsgespräch.

**Was beim Termin passiert (drei Karten):**

*Ansehen.* Nicht nur der Fleck: Wandaufbau, Anschlüsse, Rohrdurchführungen, Geländehöhe, Nutzung des Raums. Und Deine Beobachtungen: seit wann, bei welchem Wetter, was schon versucht wurde.

*Messen.* Feuchtigkeit an mehreren Stellen mit kalibrierter Messtechnik, damit die Verteilung erkennbar wird: waagerecht, flächig oder punktförmig. Salze, Risse und Anschlüsse werden beurteilt.

*Erklären.* Du bekommst eine nachvollziehbare Einschätzung, woher die Feuchtigkeit wahrscheinlich kommt, und eine Empfehlung, wie es weitergehen kann. Wenn eine Sanierung sinnvoll ist, folgt ein Festpreisangebot – schriftlich, mit erklärten Positionen.

**Formular (Elementor: WPForms Lite oder Fluent Forms, siehe Teil H):** Name* · E-Mail* · Telefon* · Postleitzahl* · Was hast Du beobachtet? (Freitext, optional) · Foto hochladen (optional, max. 2 Dateien) · Datenschutz-Checkbox* · Button „Termin anfragen“

**Unter dem Formular:** ✓ Unverbindlich ✓ Antwort in 24 Stunden ✓ Fachbetrieb vor Ort ✓ Kein Kaufzwang

**Infobox „Muss ich etwas vorbereiten?“:** Nein. Hilfreich ist, wenn die betroffene Wand zugänglich ist und Du sagen kannst, seit wann es feucht ist, bei welchem Wetter es schlimmer wird und was schon versucht wurde. Wenn Du schon Angebote hast: Bring sie mit. Wir erklären Dir, von welcher Ursache jedes ausgeht.

**Kontaktblock:** [BETRIEB] · [ADRESSE], [PLZ] [SITZ_ORT] · Telefon [TELEFON] · [EMAIL] · [OEFFNUNGSZEITEN] · Einsatzgebiet: [EINSATZGEBIET] · Karte (Elementor Google-Maps-Widget mit Adresse, nur nach Consent – siehe Teil H)

---

# TEIL H – PRODUKTIONSWEG IN WORDPRESS (ASTRA + ELEMENTOR STANDARD)

## H.1 Die Grundentscheidung: eine Master-Site, 40 Klone

Elementor in der Standardversion hat keinen Theme Builder, keine dynamischen Inhalte und kein Formular-Widget. Das ist für dieses Projekt kein Nachteil, solange die Architektur dazu passt: Alle Inhalte werden einmal in einer Master-Site gebaut, die Master-Site wird je Betrieb geklont, und die Platzhalter werden mit einem Suchen-und-Ersetzen-Werkzeug durch die Steckbrief-Daten ersetzt. Danach werden nur noch Logo, Foto und die rechtlichen Seiten eingesetzt.

**Empfohlene Hosting-Architektur: WordPress Multisite mit eigenen Domains.** Eine Installation, ein Astra, ein Elementor, ein Plugin-Satz – und 40 Sites, die jeweils unter ihrer eigenen Domain (bkm-[ort].de) laufen. Updates, Backups und Sicherheit werden einmal gemacht statt 40-mal. Domain-Zuordnung ist seit WordPress 4.5 Kernfunktion (Netzwerkverwaltung → Website bearbeiten → Website-Adresse). Voraussetzungen beim Hoster: Multisite erlaubt, mehrere Domains auf eine Installation, SSL-Zertifikate je Domain (Let's Encrypt). Alternative, wenn der Hoster das nicht kann: Einzelinstallationen, die per „All-in-One WP Migration“ (kostenlos bis 512 MB) aus der Master-Site exportiert und importiert werden – gleicher Ablauf, mehr Pflegeaufwand.

## H.2 Plugin-Satz (alles kostenlos)

| Aufgabe | Plugin | Hinweis |
|---|---|---|
| Seitenbau | Elementor (Standard) | Flexbox-Container aktivieren; Widgets: Heading, Text Editor, Image, Icon Box, Icon List, Button, Accordion, Image Box, HTML, Shortcode, Menu Anchor |
| Theme, Header, Footer | Astra (Standard) | Header-/Footer-Builder im Customizer: Logo, Menü, Button „Kostenlose Diagnose“, HTML-Element für Telefon (Klick-to-Call), Footer-Spalten als Widgets |
| Formulare | Forminator (Datei-Upload enthalten) oder WPForms Lite (ohne Upload) | Einbindung über das Elementor-Shortcode-Widget; Versand an [EMAIL] des Betriebs mit Kopie (BCC) an eine zentrale BKM-Adresse für das Lead-Tracking |
| SEO | Rank Math SEO (Standard) | Title/Meta-Vorlagen aus B.4, XML-Sitemap, Local-SEO-Modul für LocalBusiness-Daten; Platzhalter auch in Title/Meta einsetzen |
| Suchen und Ersetzen | Better Search Replace (Plugin) oder WP-CLI `wp search-replace` | Beide sind serialisierungssicher und ersetzen auch in den Elementor-Daten (`_elementor_data`) |
| Klonen (Multisite) | NS Cloner – Site Copier | Klont die Master-Site inklusive Elementor-Inhalte, Menüs, Customizer-Einstellungen und Formularen |
| Caching | LiteSpeed Cache oder WP Super Cache | je nach Hoster |
| Rechtliches | Cookie-Banner nur, wenn Tracking eingesetzt wird (z. B. Complianz) | ohne Tracking und ohne eingebettete Karte reicht die Datenschutzerklärung; Empfehlung: kein Google Maps einbetten, stattdessen Adresse mit Link „Route planen“ |

Ausdrücklich nicht nötig: Elementor Pro, Astra Pro, ein Page-Builder-Addon-Paket. Sollte später ein dynamischer Weg gewünscht sein (Platzhalter aus einer zentralen Datenquelle statt Suchen/Ersetzen), ist Elementor Pro mit dynamischen Tags und ACF der Upgrade-Pfad – die hier gebauten Seiten lassen sich dann übernehmen.

## H.3 Platzhalter in WordPress

In den Texten dieses Dokuments stehen die Platzhalter in eckigen Klammern ([ORT]). In WordPress werden sie in doppelten geschweiften Klammern angelegt ({{ORT}}), damit sie nicht mit Shortcodes kollidieren und beim Suchen/Ersetzen eindeutig sind. Die Zuordnung ist 1:1. Regeln:

- Platzhalter nur mit Großbuchstaben und Unterstrich, keine Leerzeichen, keine Umlaute.
- Jeder Platzhalter kommt genau so vor, wie er im Steckbrief steht; keine Varianten wie {{Ort}} oder {{ORT }}.
- {{TELEFON_LINK}} nur in Link-Zielen (tel:), {{TELEFON}} nur im sichtbaren Text.
- Platzhalter auch in: Seitentitel und Meta (Rank Math), Header-HTML (Telefon), Footer-Widgets, Formular-Empfängeradresse, Impressum, JSON-LD-Blöcken (HTML-Widget), Bild-Alt-Texten („Kellersanierung in {{ORT}}“).
- Nach dem Ersetzen: Elementor → Werkzeuge → CSS regenerieren, Permalinks einmal speichern, Cache leeren.

**Bilder** sind zentral: Hero, Risiken, Ablaufschritte, Ergebnisbild, Vertrauensraster und Leistungs-Icons kommen aus einem BKM-Bildpaket und sind in allen Sites identisch. Je Betrieb werden nur ausgetauscht: Logo (Header, Footer), Foto des Ansprechpartners (Startseite Block 5), optional Team-/Baustellenfoto. Alt-Texte enthalten den Ort.

## H.4 Aufbau der Master-Site (einmalig)

1. Multisite einrichten, Astra und Plugin-Satz netzwerkweit aktivieren, Master-Site „master“ anlegen (nicht öffentlich, `noindex`).
2. Astra Customizer: Farben und Schrift nach BKM-Vorgabe, Header (Logo, Menü nach B.2, Button, Telefon), Footer (drei Spalten nach B.2, Siegel, Rechtliches). Alles mit Platzhaltern.
3. Elementor: elf Seiten nach B.1 anlegen. Zuerst die Startseite aus Teil D (Blöcke 1–12 als Container). Dann eine Leistungsseite (F.1) vollständig bauen und als Elementor-Vorlage speichern („Leistungsseite“); die fünf weiteren Leistungsseiten aus dieser Vorlage erzeugen und mit F.2–F.6 befüllen. Block 8 (F.7) als gespeicherten Abschnitt anlegen und auf allen sechs Seiten einfügen. Dann Leistungsübersicht (Teil E) und Diagnoseseite (Teil G).
4. Formular in Forminator/WPForms bauen (Felder nach Teil G), Empfänger {{EMAIL}} + BCC BKM, Bestätigungstext („Danke – wir melden uns innerhalb von 24 Stunden“), Shortcode auf Startseite Block 8 und Diagnoseseite einsetzen.
5. Rank Math: Title/Meta je Seite nach B.4, Local-SEO-Daten mit Platzhaltern, Sitemap aktiv. JSON-LD-Blöcke (LocalBusiness auf allen Seiten, Service + FAQPage auf Leistungsseiten) als HTML-Widget am Seitenende mit Platzhaltern.
6. Impressum-Vorlage und Datenschutz-Vorlage (zentral juristisch geprüft; Betrieb als Verantwortlicher, BKM als Hoster/Auftragsverarbeiter – siehe Teil I) mit Platzhaltern anlegen.
7. Menü, interne Links nach B.6, Anker (Menu-Anchor-Widget: „ablauf“, „diagnose“, „faq“) prüfen. Mobile Ansicht aller elf Seiten prüfen.
8. Pilot: Master als „wettringen“ klonen, Steckbrief Wettringen ersetzen, mit dem Betrieb abstimmen, Korrekturen in die Master-Site zurückspielen. Erst dann Welle 1.

## H.5 Ablauf je Betrieb (wiederholbar, ca. 60–90 Minuten)

1. Steckbrief vollständig? Logo und Foto vorhanden? Domain bkm-[ort].de (liegt bei BKM) per DNS auf den Multisite-Server gerichtet? Bestehende Inhalte unter der Domain gesichert und Weiterleitungen alter Pfade geplant?
2. NS Cloner: Master → neue Site „[ort]“; Domain zuordnen, SSL aktivieren.
3. Better Search Replace auf der neuen Site: alle Platzhalter der Reihe nach ersetzen (Trockenlauf zuerst; Tabelle: alle, insbesondere `wp_[id]_postmeta`, `wp_[id]_posts`, `wp_[id]_options`). Reihenfolge: lange Platzhalter vor kurzen ({{EINSATZGEBIET_KURZ}} vor {{EINSATZGEBIET}}, {{TELEFON_LINK}} vor {{TELEFON}}, {{BETRIEB_KURZ}} vor {{BETRIEB}}).
4. Logo und Foto hochladen, im Customizer (Logo) und in Startseite Block 5 (Foto) einsetzen. Optionale Blöcke (Google-Bewertung, Vertrauensbaustein, Orte-Liste) einblenden oder löschen. Nicht gewählte Modulseiten (Feld 26) löschen – samt Menüeintrag, Karte auf /leistungen/ und Footer-Link.
5. Elementor CSS regenerieren, Permalinks speichern, Cache leeren, `noindex` entfernen.
6. Prüfliste H.6 durchgehen, Vorschau-Link an den Betrieb, Freigabe, Live.
7. Nacharbeit außerhalb von WordPress: Google-Unternehmensprofil des Betriebs auf die neue Website verlinken; Site in der Google Search Console anlegen und Sitemap einreichen; PLZ-Suche auf bkm-mannesmann.de/fachbetriebe/ auf die neue Domain zeigen lassen; Umgang mit bkm-mannesmann.de/[ort]/ gemäß Entscheidung in Teil I.

## H.6 Prüfliste vor dem Livegang (je Site)

☐ Keine Platzhalter mehr im Quelltext (Site-Suche nach „{{“ in Better Search Replace: 0 Treffer) · ☐ Telefon klickbar, Nummer korrekt, Formular-Testsendung kommt beim Betrieb und bei BKM an · ☐ Logo und Foto sitzen, Alt-Texte mit Ort · ☐ Alle elf Seiten mobil geprüft · ☐ Title/Meta je Seite mit Ort · ☐ Impressum und Datenschutz vollständig · ☐ Menü und Footer-Links funktionieren, Anker springen · ☐ SSL aktiv, http → https · ☐ Sitemap erreichbar, `noindex` entfernt · ☐ Google-Unternehmensprofil verlinkt · ☐ PLZ-Suche zeigt auf die Site

## H.7 Aufwand und Rollout

Master-Site inklusive Pilot Wettringen: etwa vier bis sechs Arbeitstage (Aufbau, Formular, SEO, Rechtstexte, Mobile-Prüfung, Pilot-Abstimmung). Je weiterer Betrieb: 60–90 Minuten Produktion plus Abstimmung mit dem Betrieb. Rollout in Wellen: Welle 0 Pilot (1 Betrieb) → Welle 1 zehn Betriebe mit vollständigen Steckbriefen → Wellen 2–4 je zehn. Erfahrung: Der Engpass ist nicht die Technik, sondern der Rücklauf der Steckbriefe – deshalb den Steckbrief so früh wie möglich an alle 40 Betriebe schicken und die Reihenfolge nach Rücklauf festlegen.

## H.8 Pflege nach dem Rollout

Feste Texte werden nur in der Master-Site geändert und dann gezielt in die Klone übertragen (Elementor: Abschnitt als Vorlage exportieren/importieren, oder per Suchen/Ersetzen des alten Textblocks). Steckbrief-Änderungen (neue Telefonnummer, neuer Ansprechpartner) macht BKM je Site per Suchen/Ersetzen. Die Betriebe bekommen keinen Redakteurszugang auf Textebene – das hält die 40 Sites einheitlich und die Brand Voice sauber. Wer eigene Referenzfotos oder Bewertungen ergänzen möchte, schickt sie an BKM.

---

# TEIL I – QUALITÄTSPRÜFUNG UND OFFENE PUNKTE

## I.1 Brand-Voice-Prüfung der Texte

Geprüft wurden alle Texte in Teil D bis G gegen die BKM Brand Voice und die Regeln der Kundenbroschüre v1: keine Angstkommunikation, keine unbelegten Superlative, keine Produktnamen, keine Preise, kein „garantiert“, kein „für immer trocken“, Grenzen jeder Maßnahme offen genannt, nächster Schritt auf jeder Seite erkennbar, Du-Form durchgängig. Verbleibende Formulierungen mit „dauerhaft“ beziehen sich auf die Funktion des elastischen Harzes bei der Rissverpressung und auf den Schutzanspruch der Innenabdichtung – beide sind in den technischen Datenblättern so beschrieben.

## I.2 Fachliche Gegenprüfung (Stichproben)

| Aussage auf der Website | Quelle | Status |
|---|---|---|
| Injektionsmittel macht Porenwände wasserabweisend, Poren bleiben dampfdurchlässig | Modul 01, TDS HZ-C / HZ 250 Pro | belegt |
| Altputz rund 80 cm über Schadgrenze entfernen | VA HZ-C, TDS Entfeuchtungsputz, Modul 05 | belegt |
| Mehrere Wochen Reaktionszeit vor Trocknungsgeräten | TDS HZ125 (≥ 3 Wochen), Modul 01 | belegt |
| Flächensperre bis ca. 50 cm über Schadgrenze, Schachbrettraster | TDS HZ125, Fachbetrieb Leistungen.pdf | belegt |
| Innenabdichtung im Bestand Standard, außen Sonderlösung | BKM-Systementscheidung 1 | belegt (Herstellerangabe) |
| Innenabdichtung zwei Lagen, Dichtkehle zwingend, Bänder in erste Lage | VA HDS-2K Pro, Systementscheidung 9 | belegt |
| Injektionsverfahren nicht bei drückendem Wasser | Systementscheidung 6 | belegt |
| Wand-Boden-Anschluss: Estrich 15–20 cm, Dichtkehle, Bohrungen schräg, zweikomponentiges Harz | Fachbetrieb Leistungen.pdf, Modul 11 | belegt |
| Rissverpressung zweistufig, Druck nach Untergrund | TDS SH-1K, TDS SEF-2K, Systementscheidung 4 | belegt |
| Bei WU-Beton folgt Dichtband | TDS BDB, Systementscheidung 5 | belegt |
| Sanierputz speichert Salze, ist keine Abdichtung, diffusionsoffener Anstrich | TDS SP, Systementscheidung 3 und 10 | belegt |
| „nach WTA“ statt „WTA-zertifiziert“ beim Sanierputz | Klärungsbedarf K6 der Systemarchitektur | bewusst so formuliert |
| Salzausblühungen in der Trocknung kein Mangel | VA HZ 250 Pro | belegt (Herstellerangabe) |
| Kostenlose Diagnose, Festpreis, Antwort in 24 Std., 1–3 Tage, kein Aufgraben in den meisten Fällen | bestehende Landingpage Wettringen und Fachbetriebe-Seite | übernommen – siehe I.3 Punkt 1 |

## I.3 Entscheidungen vom 14.09.2026 und verbleibende offene Punkte

**Entschieden:**

1. **Zusagen als Standard.** Kostenlose Diagnose, Festpreis nach Befund, Antwort innerhalb von 24 Stunden, Sanierung meist in 1–3 Tagen gelten für alle Betriebe und bleiben feste Texte.
2. **Domains.** bkm-[ort].de; alle Domains bestehen bereits und werden von BKM verwaltet.
3. **Rollen.** Der Fachbetrieb ist eigenständiger Unternehmer und Anbieter seiner Website; das Impressum liegt bei ihm. BKM gestaltet und betreibt die Websites als Marketingservice. Konsequenz für die Umsetzung: Impressum aus dem Steckbrief (Feld 24) ohne rechtliche Prüfung durch BKM; Datenschutzerklärung als zentrale Vorlage mit dem Betrieb als Verantwortlichem und BKM als Betreiber/Hoster (Empfehlung: die Vorlage einmal juristisch prüfen lassen und einen Vertrag zur Auftragsverarbeitung zwischen BKM und Betrieb vorsehen – dieses Dokument ersetzt keine Rechtsberatung).
4. **Ansprache.** „Du“ großgeschrieben, wie auf den bestehenden Landingpages. Alle Texte in diesem Dokument sind umgestellt.
5. **Bilder.** Zentrales Bildpaket wird von BKM geliefert oder von der Redaktion erstellt; der Prototyp arbeitet mit Bildplatzhaltern.
6. **Weitere Leistungen.** Vier optionale Module (Teil F.8) sind ausgearbeitet und werden je Betrieb über Feld 26 zugeschaltet.
7. **Pilot.** bkm-duesseldorf.de (BKM Abdichtungstechnik GmbH, Monheim am Rhein).

**Noch offen:**

1. **Lead-Routing** (Kopie jeder Formularanfrage an BKM, Zieladresse) – klärt die IT-Abteilung. Betrifft Formular-Einstellung und Datenschutzerklärung.
2. **Umgang mit bkm-mannesmann.de/[ort]/** – Kurzprofil mit Link (empfohlen) oder 301-Weiterleitung, sobald die Fachbetriebs-Website live ist. Zu entscheiden vor Welle 1.
3. **Bestehende Inhalte unter bkm-[ort].de** – die heutigen Fachbetriebs-Websites (z. B. bkm-duesseldorf.de mit eigener Leistungsliste) werden durch die neuen Sites ersetzt; alte URLs, die in Google indexiert sind, brauchen Weiterleitungen auf die passenden neuen Seiten.

## I.4 Nächste Schritte

1. Prototyp bkm-duesseldorf.de (Startseite, Leistungsübersicht, sechs Leistungsseiten, Diagnoseseite) als Vorlage für den Elementor-Aufbau prüfen und freigeben.
2. Steckbrief als Formular anlegen und an alle 40 Betriebe schicken.
3. Master-Site nach H.4 bauen, Pilot Düsseldorf live, Korrekturen in die Master-Site, Welle 1.

---

*Erstellt für die BKM MANNESMANN AG · Version 1.1 · 14.09.2026*
