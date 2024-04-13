# Ohjelman Yleisrakenne

## 1. LZW

### -   LZWCompressor-luokka

Tämä luokka vastaa tekstitiedoston pakkaamisesta LZW-pakkauksen avulla. Sen `compress`-metodi lukee annetun tiedoston ja sitten pakkaa tiedoston käyttäen LZW-algoritmia. Pakattu data tallennetaan binääri muodossa annettuun tiedostoon.

### -   LZWDecompressor

Luokka vastaa pakatun tiedoston purkamisesta takaisin alkuperäiseen muotoon. Sen `decompress`-metodi lukee annetun pakatun tiedosto ja samaa sanakirjaa kuten pakkausvaiheessa ja purkaa tiedoston käyttäen LZW-algoritmia. Purettu data tallennetaan annettuun tiedostoon.

Molemmat luokat käyttävät käyttävät UTF-8 -koodausta luonollisentekstin käsittelyssä.

##  HuffmanComding

### -   Huffmancompress-luokka
Luokka vastaa tesktitiedoston pakkaamisen ja purkamisen Huffman-koodauksen avulla. Tämä luokka muodostaa Huffman-puun ja sisältää useita apumetodeja, jotka käsittelevät koodauksen eri vaiheet, kuten prioriteetin tekimisen, puun rakentamisen, tekstin pakkaamisen ja purkamisen sekä tiedostojen käsittelyn.

Luokka käyttää UTF-8 -koodausta luonollisentekstin käsittelyssä.


## Main
Tiedosto main.py vastaa ohjelman käyttöliittymästä. Ohjelma antaa käyttäjän valita termminaalissa eri toimintoja, esim tiedostojen pakkaamisen ja purkamisen Huffman-koodauksella tai LZW-pakkauksella.

# Suorituskyky- ja O-analyysivertailu
Huffman-koodaus: Aikavaatimuus O(nlogn)
LZW: Aikavaatimuus O(n)

## Vertailu
En ole vielä päässyt ihan vertailemaan suorituskykyjä, mutta tässä havaintoja:
Jos tiedostoissa on paljon samoja merkkejm, niin Huffman-koodaus voi olla parempi tehokas valinta.
Jos samoja merkkijonoja esiintyy paljon, niin tällöin LZW-pakkaus voi olla parempi.

# Työn mahdolliset puutteet ja parannusehdotukset
Voisi refakturoida koodia ja tehostaa tietorakenteita. Lisäksi voisi lisätä enemmän kommentteja

# Laajojen kielimallien käyttö
- DeepL: kääntään englannin kielistä materiaali, jotta ymmärtäisn paremmin.
- ChatGPT: avustaa virheiden tunnistamisessa ja käsitteiden selittämisessä. Lisäksi pyysin selvennystä, kun jäin jumiin.


# Viitteet
- Huffman-koodaus: [Wikipedia: Huffman coding](https://en.wikipedia.org/wiki/Huffman_coding), [Geeksforgeeks: Huffman coding](https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/), [Youtube](https://www.youtube.com/watch?v=iiGZ947Tcck&pp=ygUOaHVmZm1hbiBjb2Rpbmc%3D)
- Lempel-Ziv-Welch (LZW): [Wikipedia: Lempel-Ziv-Welch](https://en.wikipedia.org/wiki/Lempel-Ziv-Welch), [Geeksforgeeks: LZW (Lempel–Ziv–Welch) ](https://www.geeksforgeeks.org/lzw-lempel-ziv-welch-compression-technique/), [Youtube](https://www.youtube.com/watch?v=j2HSd3HCpDs&t=745s&pp=ygUDbHp3)