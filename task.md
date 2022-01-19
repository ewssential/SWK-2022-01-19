# SWK Coding Dojo

## Allgemeines
Toastmasters international(kurz: TMI) ist eine überregionale Vereinigung von Rhetorikvereinen. Bei regelmässigen Klubtreffen werden Reden gehalten und bewertet. 

1x im Jahr veranstaltet TMI überregionale Redewettbewerbe.Menschen aus verschiedenen Klubs treffen sich an einem Ort für die Durchführung von Redewettbewerben. Der Wettbewerb wird entweder auf deutsch oder auf englisch durchgeführt. Es gibt pro Treffen mehrere Wettbewerbsarten:
* Den klassischen Redewettbewerb: n Teilnehmer halten jeweils eine Rede, die dann bewertet wird
* Der Stegreifredenwettbewerb:n Teilnehmer halten eine improvisierte Rede, die dann bewertet wird
* Der Redebewertungswettbewerb: n Teilnehmer bewerten eine Rede. Diese Bewertungsrede wird danach bewertet. 

Die Wettbewerbe finden nacheinander statt.

### Rollenbeschreibung
Jeder Besucher des Redewettbewerbs kann unterschiedliche Rollen einnehmen:
* Es gibt den reinen Zuschauer, der nichts weiter macht, als zuzuschauen.
* Es gibt aber auch Wettbewerbsteilnehmer. 
* Es gibt daneben noch diverse Ämter. Pro Wettbewerb sind unterschiedliche Ämter zu besetzen: neben den Teilnehmern gibt es pro Wettbewerb 
* 3-5 Preisrichter (der Einfachheit gehen wir für diese Aufgabe immer von 5 Preisrichtern aus)
* einen Moderator 
* zwei Zeitnehmer, 
* zwei Auszähler der Stimmzettel, 
* einen Wettbewerbsleiter
* einen Saaldiener


Die Preisrichter bewerten die Leistung des Wettbewerbsteilnehmers, und benutzen dazu einen Stimmzettel. Die beiden Auszähler werten die Stimmzettel nach dem Wettbewerb aus. Der Wettbewerbsleiter überwacht den gesamten Ablauf des Wettbewerbs. Der Saaldiener führt die Teilnehmer zur Bühne.Die beiden Zeitnehmer signalisieren mit einer Ampel die Redezeit und notieren die Zeiten der Rede. Der Moderator führt durch den Wettbewerb.

### Ablauf
Zeitlich vor dem Redewettbewerb haben sich die Besucher online angemeldet und haben angegeben, ob sie bereit sind, eins oder mehrere der beschriebenen Ämter eines Wettbewerbs zu übernehmen. Sie dürfen aber nur für ein Amt bei einem Wettbewerb ausgewählt werden. Sie dürfen kein Amt übernehmen, wenn sie Teilnehmer des betreffenden Wettbewerbs sind.

### Input
In einer CSV-Datei sind sämtliche Daten gespeichert des Besuchers gespeichert(Name und Kontaktdaten des Besuchers, welche Sprachen er spricht, welche Ämter er bereit ist, zu übernehmen und ob er Teilnehmer an einem oder mehreren Wettbewerben ist, und ob er ein erfahrenes Mitglied bei Toastmasters International ist)

## Aufgabenstellung
AUFGABE: Die zu erstellende Software liest die CSV-Datei ein und gibt pro Wettbewerb folgendes aus:
* Wettbewerb „Art des Wettbewerbs”
    * Liste der Teilnehmer
    * Moderator 
    * Wettbewerbsleiter
    * Zwei Zeitnehmer
    * Einen Saaldiener
    * Zwei Auszähler
    * 5 Preisrichter
    * Saaldiener

Es soll dann jeweils der Vor- und Nachname ausgegeben werden, zusammen mit der Klubnummer, und der Mitgliedsnummer bei TMI.

### Nebenbedingungen 
* Besucher, die als Sprache „deutsch” bei der Anmeldung angegeben haben, dürfen nur für deutschsprachige Wettbewerbe in Betracht gezogen werden. Analog für „englisch”. Haben sie bei der Anmeldung „deutsch/englisch” angegeben, entfällt diese Einschränkung
* Eine Person kann in einem Wettbewerb nur ein Amt besetzen.
* Eine Person kann bei mehreren Wettbewerben jeweils ein Amt übernehmen
* Ein Teilnehmer eines Wettbewerbs kann nicht gleichzeitig ein Amt bei demselben Wettbewerb übernehmen, aber durchaus ein Amt bei einem anderem Wettbewerb.
* Preisrichter sollen (sofern möglich) aus verschiedenen Klubs kommen (damit kein Teilnehmer unbewusst bevorzugt wird).
* Preisrichter und Wettbewerbsleiter müssen ein erfahrenes (Level 1+2 = ja) Mitglied bei TMI sein

