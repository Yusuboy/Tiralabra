# Testausdokumentti

# Kattavuusraportti
![Testikattavuus](https://github.com/Yusuboy/Tiralabra/blob/main/Dokumentaatio/Viikkoraportit/coverage.png)

# LZW-pakkausalgoritmin testaus


## Testattu toiminnallisuus
Tiedoston pakkaaminen ja purkaminen LZW-pakkausalgoritmilla.

## Miten testaus tehtiin
- Testit suoritettiin automaattisilla yksikkötesteillä käyttäen Pythonin unittest-kirjastoa.
- Testiluokka `TestLZW` luotiin, ja siihen määriteltiin testitapaus `test_compress_decompress`, joka testaa tiedoston pakkaamisen ja purkamisen.

## Syötteet
- Testit suoritettiin käyttämällä esimerkkitekstitiedostoa (`test.txt`), joka sisältää luonnollista tekstiä ja on kooltaan 1.1MB.

## Tulokset
- Testi suoritettiin onnistuneesti.
- Alkuperäinen tiedosto ja purettu tiedosto ovat identtiset.
- Pakkaus- ja purkamistoiminnot toimivat oikein.
- Ei havaittu virheitä tai poikkeamia.
## Testien toistettavuus
- Testit voidaan toistaa suorittamalla testiluokka `TestLZW`.
- Testit luovat väliaikaisia tiedostoja (`compressed_test.bin` ja `decompressed_test_file.txt`), jotka poistetaan testien jälkeen `tearDown`-metodissa.

## Empiirisen testauksen tulokset graafisessa muodossa
- Empiiristä testausta ei ole suoritettu. Yksikkötestit kattavat algoritmien toiminnallisuuden varmistaen, että toiminnot suoritetaan oikein.

# Huffman-koodauksen pakkausalgoritmin testaus

## Testattu toiminnallisuus
Tiedoston pakkaaminen ja purkaminen Huffman-koodausalgoritmilla.

## Miten testaus tehtiin
- Testit suoritettiin automaattisilla yksikkötesteillä käyttäen Pythonin unittest-kirjastoa.
- Testiluokka `TestHuffman` luotiin, ja siihen määriteltiin testitapaukset:
  - `test_compress_decompress`: Testaa tiedoston pakkaamisen ja purkamisen Huffman-koodausalgoritmilla.
  - `test_heapnode_equality`: Testaa, että `HeapNode` -luokan vertailu toimii odotetusti.

## Syötteet
- Testit suoritettiin käyttämällä esimerkkitekstitiedostoa (`test.txt`), joka sisältää luonnollista tekstiä ja on kooltaan 1.1MB.

## Testien toistettavuus
- Testit voidaan toistaa suorittamalla testiluokka `TestHuffman`.

## Empiirisen testauksen tulokset graafisessa muodossa
- Empiiristä testausta ei ole suoritettu. Yksikkötestit kattavat algoritmien toiminnallisuuden varmistaen, että toiminnot suoritetaan oikein.
