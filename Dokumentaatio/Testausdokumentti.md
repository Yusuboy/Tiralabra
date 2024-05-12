# Testausdokumentti

# Kattavuusraportti
### Tämän hetken testikattavuus:
![Testikattavuus](https://github.com/Yusuboy/Tiralabra/blob/main/Dokumentaatio/Viikkoraportit/coverage_7.png)
## Codecov
Testikattavuuden seurantaan on integroitu Codecoveen. Testien kattavuuksien tarkempia tietoja voi tarkastella Codecovissa.

# LZW-pakkausalgoritmin testaus


## Testattu toiminnallisuus
Tiedoston pakkaaminen ja purkaminen LZW-pakkausalgoritmilla.


## Miten testaus tehtiin
- Testit suoritettiin automaattisilla yksikkötesteillä käyttäen Pythonin unittest-kirjastoa.
- Testiluokka `TestLZW` luotiin, ja siihen määriteltiin testitapaus `test_compress_decompress`, joka testaa tiedoston pakkaamisen ja purkamisen.
- Lisäksi testattiin testitapauksilla `test_non_existent_input_file_compress` ja `test_non_existent_input_file_decompress` pakkaus- ja purkausoperaatioiden käyttäytymistä olemattomien syötetiedostojen tapauksessa.
- `test_compress_data`: Testaa tiedoston pakkaamisen LZW-algoritmilla antamalla dataa "ABC".
- `test_compress_data_false_condition`: Testaa, että tiedoston pakkaaminen LZW-algoritmilla ei onnistu odotetusti antamalla dataa "ABCD" epäedullisessa tilanteessa.

Testattiin perusteellisesti LZW-pakkausta - ja purkua eri skenaarioissa varmistaaksemme niiden luotettavuuden.

Varmistimme, että sekä pakkaus- että purkutoiminnot säilyttävät alkuperäisten tietojen eheyden, kun niitä sovelletaan tiedostoihin. Tämä tarkoitti esimerkkitiedoston pakkaamista ja sen purkamista ja sen varmistamista, että tuloksena olevat tiedot vastaavat alkuperäistä sisältöä.
Tutkittiin myös, miten moduulit käsittelevät olemattomia syötetiedostoja pakkaamisen ja purkamisen aikana. Molemmissa tapauksissa moduulien pitäisi aiheuttaa FileNotFoundError-poikkeus ilman kaatumista, mikä onnistuttiin tarkistamaan.
Lisäksi arvioimme tietojen pakkauksen tarkkuutta ja varmistimme, että moduulit pakkaavat merkkijonot oikein. Vahvistimme moduulien tarkkuuden antamalla esimerkkitietojonoja ja vertaamalla tuloksena saatua pakattua dataa odotettuun tulosteeseen.


Translated with DeepL.com (free version)
## Syötteet
- Testit suoritettiin käyttämällä esimerkkitekstitiedostoa (`test.txt`), joka sisältää luonnollista tekstiä ja on kooltaan 1.1MB.

## Tulokset
- Testi suoritettiin onnistuneesti.
- Alkuperäinen tiedosto ja purettu tiedosto ovat identtiset.
- Pakkaus- ja purkamistoiminnot toimivat oikein.
- Ei havaittu virheitä tai poikkeamia.

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
  - `test_frequency_dictionary`: Testaa frekvenssitaulukon luominen.
  - `test_make_nodes_helper`: Testaa solmujen luonti apumetodilla.
  - `test_pad_encoded_sequence`: Testaa koodatun sekvenssin täydentäminen.
  - `test_output_binary`: Testaa koodatun sekvenssin muuntaminen binäärimuotoon.
  - `test_cut_padding`: Testaa täytteen poistaminen koodatusta sekvenssistä.
  - `test_decode_content`: Testaa sisällön purkaminen.

Huffman-pakkausalgoritmin toimintaa on testattu perusteellisesti yksikkötesteillä. Ensinnäkin on varmistettu, että pakkaus- ja purkutoiminnot suoritetaan oikein tiedostoilla, ja että alkuperäinen tiedosto säilyy muuttumattomana purkamisen jälkeen. Testit kattavat myös taajuussanakirjan muodostamisen erilaisilla syötteillä, kuten tyhjällä merkkijonolla, yhdellä merkillä sekä useilla merkeillä, mukaan lukien erikoismerkit ja välilyönnit.

Lisäksi on varmistettu solmujen vertailun ja oikean toiminnan toimivan odotetusti. Kekorakenteen rakentamisen ja solmujen yhdistämisen Huffman-pakkauksen aikana on myös varmistettu toimivan oikein. Testit varmistavat, että solmut muodostetaan oikein Huffman-pakkauksen aikana ja että tekstin koodaus tuottaa odotetun koodatun sekvenssin.

Muut testit keskittyvät binaarilähdön, täytetyn sekvenssin leikkauksen ja sisällön purkamisen oikeellisuuteen. Näiden testien avulla varmistetaan, että pakkaus- ja purkutoiminnot toimivat moitteettomasti ja että lopputulos on odotetunlainen.

Yksikkötesteillä on kattavasti varmistettu, että HuffmanCoding-sovellus toimii oikein erilaisissa tilanteissa ja syötteissä, ja että se täyttää odotetut toiminnalliset vaatimukset.

## Syötteet
- Testejä on suoritettu käyttämällä esimerkkitekstitiedostoa (`test.txt`), joka sisältää luonnollista tekstiä ja on kooltaan 1.1MB.

## Tulokset
- Testi suoritettiin onnistuneesti.
- Alkuperäinen tiedosto ja purettu tiedosto ovat identtiset.
- Pakkaus- ja purkamistoiminnot toimivat oikein.
- Ei havaittu virheitä tai poikkeamia.


# Lisätestaus file_utils-moduulille

## Testattu toiminnallisuus
Tiedostojen käsittelyyn liittyvien apufunktioiden testaus.

## Miten testaus tehtiin
- Testit suoritettiin automaattisilla yksikkötesteillä käyttäen Pythonin unittest-kirjastoa.
- Testiluokka `TestFileUtilis` luotiin, ja siihen määriteltiin seuraavat testitapaukset:
  - `test_is_txt_file`: Testaa, tunnistetaanko tekstitiedostot oikein.
  - `test_get_file_size`: Testaa, saadaanko tiedoston koko oikein.
  - `test_list_files`: Testaa, saadaanko tiedostot listattua oikein tietyltä hakemistolta ja tietyllä tiedostopäätteellä.
  - `test_delete_files_in_folder`: Testaa, poistetaanko tiedostot kansioista oikein.

## Syötteet
- Testit suoritettiin luomalla tilapäisiä tekstitiedostoja ja binääritiedostoja, jotka poistettiin testien jälkeen.
- Testit käyttivät esimerkkitekstitiedostoa (`test.txt`) ja esimerkkibinääritiedostoa (`test.bin`).

## Tulokset
- Kaikki testit suoritettiin onnistuneesti.
- Testit varmistivat, että apufunktiot toimivat oikein ja palauttavat odotetut tulokset.

# Lisätestaus käyttöliittymäfunktioille

## Testattu toiminnallisuus
Käyttöliittymäfunktioiden näyttämisen ja tulostamisen testaus.

## Miten testaus tehtiin
- Testit suoritettiin automaattisilla yksikkötesteillä käyttäen Pythonin unittest-kirjastoa.
- Testiluokka `TestDisplayFunctions` luotiin, ja siihen määriteltiin seuraavat testitapaukset:
  - `test_display_file_lists`: Testaa tiedostolistojen näyttämistä käyttöliittymässä eri skenaarioissa.
  - `test_display_compression_stats`: Testaa pakkaustilastojen näyttämistä käyttöliittymässä.
  - `test_display_decompression_stats`: Testaa purkamistilastojen näyttämistä käyttöliittymässä.

## Syötteet
- Testit käyttivät (`mocks`) ja ohjelman käyttämien funktioiden korvauksia (`patches`) varmistaakseen, että tulostukset ovat odotettuja eri tilanteissa.

## Tulokset
- Kaikki testit suoritettiin onnistuneesti.
- Testit varmistivat, että käyttöliittymäfunktiot toimivat oikein ja näyttävät odotetut tulokset.
- Kukin funktio testattiin erikseen varmistaen, että ne toimivat oikein eri syötteillä ja tilanteissa.





# Testien toistettavuus
- Kaikki testit voidaan toistaa suorittamalla kometno `poetry run invoke test`.
- Testit luovat väliaikaisia tiedostoja (`compressed_test.bin` ja `decompressed_test_file.txt`), jotka poistetaan testien jälkeen `tearDown`-metodissa.


# Empiirisen testauksen tulokset graafisessa muodossa
- Empiiristä testausta ei ole suoritettu. Yksikkötestit kattavat käyttöliittymäfunktioiden toiminnallisuuden varmistaen, että ne toimivat oikein eri tilanteissa.