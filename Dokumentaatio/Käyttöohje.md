## **Asennus**
1. Kloonaa repositorio koneellesi.
```
git clone git@github.com:Yusuboy/Tiralabra.git
```
2. Siirry juurihakemistoon ja ja asenna riippuvuudet.
```
poetry install
```
## **Komentorivikäskyt**
 **Ohejelman voi käynistää komennolla:**
```bash
poetry run invoke start
```

### **Testaus**

**Testit suoritetaan komennollla:**
```bash
poetry run invoke test
```

### **Testikattavuus**
**Testikattavuusraportin voi generoida komennolla:**
```bash
poetry run invoke coverage-report
```

### **Pylint**
**Tiedoston .pylintrc määrittelemät tarkistukset voi suorittaa komennolla:**
```bash
poetry run invoke lint
```


# Ohjelman käyttö

## Ohjelman käynnistys

Kun ohjelma käynnistetään ensimmäisen kerran, se avataan terminaalissa. Ensimmäisen käynnistyksen yhteydessä näytetään taulukko, jossa on listattuna käytettävissä olevat tekstitiedostot ja binääritiedostot. Taulukon lisäksi käyttäjää pyydetään valitsemaan yksi toiminnoista: "Compress with Huffman", "Decompress with Huffman", "Compress with LZW", "Decompress with LZW" tai "Exit", jolla ohjelma voidaan sulkea.

![Taulukko alkutilanteesta](https://github.com/Yusuboy/Tiralabra/blob/main/Dokumentaatio/images/alotus.png)

## Toimintojen valitseminen

Kun käyttäjä valitsee haluamansa toiminnon, hänelle avautuu mahdollisuus syöttää haluamansa tiedoston nimi. Jos käyttäjä valitsee pakkaustoiminnon ("Compress with Huffman" tai "Compress with LZW"), hän syöttää haluamansa tekstitiedoston nimen, joka pakataan binääritiedostoksi. Jos taas käyttäjä valitsee purkutoiminnon ("Decompress with Huffman" tai "Decompress with LZW"), hän syöttää haluamansa binääritiedoston nimen, joka puretaan takaisin tekstitiedostoksi. Jos tiedostonimiä syötettäessä tapahtuu virhe, ohjelma ilmoittaa siitä käyttäjälle.
![Taulukko alkutilanteesta](https://github.com/Yusuboy/Tiralabra/blob/main/Dokumentaatio/images/alotus2.png) 
**Huomio:** Tekstitiedostoja ei voi purkaa. Jos käyttäjä yrittää purkaa tekstitiedoston, ohjelma ilmoittaa siitä.

## Pakkaus- ja purkaustoimintojen käyttö

### Pakkaus toimintojen käyttö

Kun käyttäjä valitsee "Compress with Huffman" tai "Compress with LZW", valitun tekstitiedoston sisältö pakataan vastaavaa algoritmia käyttäen binääritiedostoksi. Tämän jälkeen käyttäjä näkee tilastotiedot, jotka sisältävät alkuperäisen tiedoston koon, pakatun tiedoston koon, pakkaussuhteen sekä pakkausajan.

![Taulukko alkutilanteesta](https://github.com/Yusuboy/Tiralabra/blob/main/Dokumentaatio/images/alotus3.png) 

### Purkaus toimintojen käyttö

Kun käyttäjä valitsee "Decompress with Huffman" tai "Decompress with LZW", valitun binääritiedoston sisältö puretaan takaisin tekstitiedostoksi. Tämän jälkeen käyttäjä näkee purkausajan.

![Taulukko alkutilanteesta](https://github.com/Yusuboy/Tiralabra/blob/main/Dokumentaatio/images/alotus4.png) 


## Lopetus

Kun käyttäjä valitsee "Exit", ohjelma sulkeutuu.
