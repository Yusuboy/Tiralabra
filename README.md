# Tiralabra-pakkaus- ja purkualgoritmit
![Githhub Actions](https://github.com/Yusuboy/Tiralabra/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/Yusuboy/Tiralabra/graph/badge.svg?token=Bpb3yvC4bp)](https://codecov.io/gh/Yusuboy/Tiralabra)

## Dokumentaatio
- [Määrittelydokumentti](https://github.com/Yusuboy/Tiralabra/blob/main/Dokumentaatio/M%C3%A4%C3%A4rittelydokumentti.md)
- [Toteutusdokumentti](https://github.com/Yusuboy/Tiralabra/blob/main/Dokumentaatio/Toteutusdokumentti.md)
- [Testausdokumentti](https://github.com/Yusuboy/Tiralabra/blob/main/Dokumentaatio/Testausdokumentti.md)
- [Käyttöohje](https://github.com/Yusuboy/Tiralabra/blob/main/Dokumentaatio/K%C3%A4ytt%C3%B6ohje.md)

## Viikkoraportit
- [Viikkoraportti 1](https://github.com/Yusuboy/Tiralabra/blob/main/Dokumentaatio/Viikkoraportit/Viikko1.md)

- [Viikkoraportti 2](https://github.com/Yusuboy/Tiralabra/blob/main/Dokumentaatio/Viikkoraportit/Viikko2.md)

- [Viikkoraportti 3](https://github.com/Yusuboy/Tiralabra/blob/main/Dokumentaatio/Viikkoraportit/viikko3.md)


## **Ohjelman suorittaminen**

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
