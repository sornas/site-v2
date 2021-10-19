# LaTeX

LaTeX kan vara lite klurigt men när du fått koll på det kommer du charma varenda
examinator från första <del>kompletteringen</del> inlämningen. Garanterat +1
betygssteg.

På den här sidan har vi samlat ett antal exempel inom olika kategorier. Det är
främst menat till dig som redan har koll på LaTeX och vill höja nivån
ytterligare ett snäpp.

Om du vill lära dig mer om LaTeX finns det gott om material på internet. Vi har
samlat några bra länkar här nedan.

Nybörjare:

- [first-latex-doc – A document for absolute LaTeX
  beginners](http://mirrors.ctan.org/info/first-latex-doc/first-latex-doc.pdf).
  9 sidor som går igenom hur du kommer igång med text och matematik.
- [lshort-english – A (Not So) Short Introduction to
  LaTeX2ε](http://mirrors.ctan.org/info/lshort/english/lshort.pdf). Som man
  kanske gissar utifrån namnet är den här introduktionen inte särskilt kort;
  hela 129 sidor! När du har skrivit lite text och fått ut en PDF, kolla igenom
  innehållsförteckningen och testa det som ser intressant ut.

Nästa steg:

- [latex4wp – A LaTeX guide specifically designed for word processor
  users](http://mirrors.ctan.org/info/latex4wp/latex4wp.pdf). När du börjat få
  koll på grunderna kanske du undrar hur du åstadkommer funktionalitet X eller Y
  från ol' reliable Microsoft Word.
- [LaTeX (Wikibooks)](https://en.wikibooks.org/wiki/LaTeX). Likt Wikipedia
  varierar Wikibooks i kvalitet. Det är oavsett en utmärkt referens för en hel
  del ämnen. Vissa sidor är utdaterade så håll ögonen öppna efter nyare och bättre
  sätt att göra saker på.
- [Using LaTeX to Write a PhD
  Thesis](https://www.dickimaw-books.com/latex/thesis/index.html). Namnet till
  trots kan den hjälpa även om du inte skriver en avhandling.

Det går också jättebra att dyka upp på någon av våra meetups med frågor!

## Ekvationer

Stiliga och enkla.

<img src="/static/img/latex/equation.png" alt="Enkel ekvation" class="latex" />

<pre class="latex">
\usepackage{amsmath}

\begin{equation*}
    e^{i \cdot \pi} - 1 = 0
\end{equation*}
</pre>

## tikz

tikz är ett system för att rita figurer direkt i LaTeX. Fördelar:

- Figurerna blir vanlig LaTeX i slutändan. Hyperlänkar, fotnoter och referenser
  fungerar som vanligt (för det mesta).
- När figuren väl är skapad är det enkelt att göra småjusteringar i text och
  annat eftersom ett separat program inte behöver öppnas.
- Vektorgrafik. Ingen rasterisering så långt ögat kan nå.
- Du kan göra komplexa beräkningar och conditional compilation inuti
  figur-innehållet.

Nackdelar:

- Figurer tar för det mesta längre tid att rita.
- Vissa figurer tar orimligt lång tid att rita, även om man justerar för att
  LaTeX generellt tar längre tid att arbeta i.
- Vissa figurer är praktiskt taget omöjliga att rita.
- Det är svårt att få en figur att se enbart helt okej ut. Vanligtvis är den
  alltid väldigt ful eller väldigt fin, aldrig mitt emellan.
- Finjusteringarna kan vara beroendeframkallande för vissa.

### JSP-diagram

Populära i ISY:s datorteknik-kurser. [Jackson Structured Programming
(Wikipedia)](https://en.wikipedia.org/wiki/Jackson_structured_programming).

I praktiken behöver du pilla på `sibling distance`-värdet en del. Det beskriver
avståndet mellan barnen i sidled. Tyvärr har olika barnbarn ingen koll på varandra
så du kan behöva öka avståndet två nivåer upp. I exemplet nedan måste t.ex.
`Selektion 1` ha ganska stort `sibling distance` så att inte C och D-rutorna
överlappar.

`align=center` gör att newlines fungerar inuti rutorna.

<img src="/static/img/latex/jsp.png" alt="JSP-diagram med tikz" class="latex" />

<pre class="latex">
\usepackage{tikz}
\usetikzlibrary{positioning,shadows,shapes,arrows}

\begin{tikzpicture}[
    box/.style={
        rectangle,
        draw=black,
        rounded corners=1mm,
        minimum width=5em,
        minimum height=3em,
        level distance=10cm,
        text centered,
        anchor=north,
        align=center
    },
    circle/.style={
        rectangle,
        draw=black,
        rounded corners=1mm,
        minimum width=5em,
        minimum height=3em,
        level distance=10cm,
        text centered,
        anchor=north,
        label={[xshift=-1.25em, yshift=-2.25ex]north east:$\circ$},
        align=center
    },
]
    \node (JSP) [box] {Root-sekvens}
     [sibling distance=2.5cm]
        child {node (a) [box] {A}}
        child {[sibling distance=4.5cm] node (b) [box] {Selektion 1}
          child {[sibling distance=2cm] node (c) [circle] {Selektion 2}
            child {node (d) [circle] {B}}
            child {node (e) [circle] {C}}
          }
          child {[sibling distance=2cm] node (f) [circle] {Sekvens 2}
            child {node (g) [box] {D}}
            child {node (h) [box] {E}}
          }
        }
    ;
\end{tikzpicture}
</pre>

### Summering av normalfördelningar

Den här var väldigt användbar i författarens gymnasiearbete. Notera att vi
endast matar in ekvationer (någorlunda komplexa sådana också) och låter ett
separat program (`gnuplot`) räkna ut hur linjerna ska gå.

<img src="/static/img/latex/sum_normal_dist.png" alt="Summering av normalfördelningsskurvor" class="latex" />

<pre class="latex">
\usepackage{pgfplots}
\usepackage{pgfplotstable}
\pgfplotsset{compat=1.14}

\begin{tikzpicture}
    \begin{axis}[
        ticks=none,
        xmin=-20, xmax=20,
        ymin=-1, ymax=10
    ]
        \addplot [domain=-25:25, samples=200, forget plot] {
            1/0.5*(2*pi)^0.5 * exp(-((x)^2)/2*0.25)
        };
        \addplot [domain=-25:25, samples=200, forget plot] {
            1/0.3*(2*pi)^0.5 * exp(-((x-7)^2)/2*0.09)
        };
        \addplot [domain=-25:25, samples=200, forget plot] {
            1/0.4*(2*pi)^0.5 * exp(-((x+6)^2)/2*0.16)
        };
        \addplot [blue,domain=-25:25, samples=200] {
            (1/0.5*(2*pi)^0.5 * exp(-((x)^2)/2*0.25))
            + (1/0.3*(2*pi)^0.5 * exp(-((x-7)^2)/2*0.09)) 
            + (1/0.4*(2*pi)^0.5 * exp(-((x+6)^2)/2*0.16))
        };
    \end{axis}
\end{tikzpicture}
</pre>

## Licens

All LaTeX-kod och dess tillhörande PNG-renderingar på den här sidan publiceras
under [CC0](https://creativecommons.org/share-your-work/public-domain/cc0/).
Kort och gott: gör vad du vill!
