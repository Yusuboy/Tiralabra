# Testausdokumentti

# Kattavuusraportti
### Tämän hetken testikattavuus:
![Testikattavuus](https://github.com/Yusuboy/Tiralabra/blob/main/Dokumentaatio/Viikkoraportit/coverage2.png)
## Codecov
Testikattavuuden seurantaan on integroitu Codecoveen. Testien kattavuuksien tarkempia tietoja voi tarkastella Codecovissa.

# LZW-pakkausalgoritmin testaus


## Testattu toiminnallisuus
Tiedoston pakkaaminen ja purkaminen LZW-pakkausalgoritmilla.


## Miten testaus tehtiin
- Testit suoritettiin automaattisilla yksikkötesteillä käyttäen Pythonin unittest-kirjastoa.
- Testiluokka `TestLZW` luotiin, ja siihen määriteltiin testitapaus `test_compress_decompress`, joka testaa tiedoston pakkaamisen ja purkamisen.
- Lisäksi testattiin testitapauksilla `test_non_existent_input_file_compress` ja `test_non_existent_input_file_decompress` pakkaus- ja purkausoperaatioiden käyttäytymistä olemattomien syötetiedostojen tapauksessa.

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
  - `test_heap_build`: Testaa, että keko rakennetaan oikein.
  - `test_merge_nodes`: Testaa, että solmut yhdistetään oikein.
  - `test_encoded_text`: Testaa, että teksti koodataan oikein.

## Syötteet
- Testit suoritettiin käyttämällä esimerkkitekstitiedostoa (`test.txt`), joka sisältää luonnollista tekstiä ja on kooltaan 1.1MB.

## Testien toistettavuus
- Testit voidaan toistaa suorittamalla testiluokka `TestHuffman`.

## Empiirisen testauksen tulokset graafisessa muodossa
- Empiiristä testausta ei ole suoritettu. Yksikkötestit kattavat algoritmien toiminnallisuuden varmistaen, että toiminnot suoritetaan oikein.
