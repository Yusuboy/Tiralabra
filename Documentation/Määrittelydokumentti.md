# Määrittelydokumentti

## 1. Ohjelmointikieli ja muut kielet

Käytän projektissani Python-ohjelmointikieltä. En hallitse muita kieliä riittävn hyvin, jotta voisin antaa vertaispalautetta niistä. 

## 2. Algoritmit ja tietorakenteet

Projektissa toteutan Huffman-koodauksen ja Lempel-Ziv-Welch (LZW) -algoritmin. Tietorakenteista käytän mm. binääripuita ja taulukoita.

## 3. Ongelman ratkaisu

Ratkaisen tiedoston pakkaamisen ja purkamisen ongelman. Tavoitteena on saavuttaa noin 40-60% pakkausteho alkuperäiseen kokoon nähden. Projektissa vertaillaan myös Huffman-koodauksen ja LZW-algoritmin suorituskykyä keskenään.

## 4. Syötteet ja niiden käyttö

Ohjelma saa syötteenä pakattavan tekstitiedoston, jonka se pakkaa valitulla algoritmilla ja tuottaa pakatun tiedoston. Pakatun tiedoston voi sitten antaa ohjelmalle purkamista varten, jolloin se palauttaa alkuperäisen tiedoston.

## 5. Aika- ja tilavaativuudet

- Huffman-koodaus: Aikavaativuus O(n log n), tilavaativuus riippuu syötteen määrästä
- Lempel-Ziv-Welch (LZW): Aikavaativuus vaihtelee syötteen mukaan, tilavaativuus riippuu syötteen määrästä

## 6. Vertailu

Projektissa vertaillaan Huffman-koodauksen ja LZW-algoritmin suorituskykyä keskenään. Vertailussa otetaan huomioon pakkausteho ja purkamisen nopeus.
## 7. Viitteet

- Huffman-koodaus: [Wikipedia: Huffman coding](https://en.wikipedia.org/wiki/Huffman_coding), [Geeksforgeeks: Huffman coding](https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/)
- Lempel-Ziv-Welch (LZW): [Wikipedia: Lempel-Ziv-Welch](https://en.wikipedia.org/wiki/Lempel-Ziv-Welch), [Geeksforgeeks: LZW (Lempel–Ziv–Welch) ](https://www.geeksforgeeks.org/lzw-lempel-ziv-welch-compression-technique/), 

## 8. Harjoitustyön Ydin

Projektin ydin on luonnolista kieltä sisältävän tekstitiedoston  pakkaaminen ja purkaminen käyttäen kahta erilaista pakkausalgoritmia, Huffman-koodausta ja Lempel-Ziv-Welch (LZW) -algoritmia. Projektissa vertaillaan näiden suorituskykyä keskenään.
## 9. Opinto-ohjelma ja käytetty kieli

Opinto-ohjelma: Tietojenkäsittelytieteen kandidaatti (TKT)
Dokumentaatiossa käytetty kieli: suomi
