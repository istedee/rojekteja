# coding=utf-8
import random
import time
import webbrowser
import haravasto

tila = {
    "ruudukko": [],
    "peliruudukko": [],
    "liput": [],
    "miinat": [],
    "aloitus": [],
    "klikit": 0,
    "tappio": True,
    "aika_aloitus": 0,
    "aika_lopetus": 0
}


def kentan_ulottuvuudet():
    """Funktio pyytää pelaajaa asettamaan kentän korkeuden, leveyden ja miinojen lukumäärän."""
    print("Määritä kentän leveys, korkeus ja miinojen lukumäärä.")
    while True:
        try:
            leveys = int(input("Anna kentän leveys (1-45): "))
            korkeus = int(input("Anna kentän korkeus(1-25): "))
            lukumaara = int(input("Anna miinojen lukumäärä: "))
            if leveys < 1 or korkeus < 1 or lukumaara >= leveys * korkeus:
                print("Kenttä on liian pieni tai miinoja on enemmän kuin ruutuja.\n")
            else:
                return korkeus, leveys, lukumaara
        except ValueError:
            print("Syötä arvot kokonaislukuina\n")


def tee_ruudukko():
    """
    Luo saaduilla arvoilla kaksi ruudukkoa. Toinen on peliruudukko, joka piirretään
    ja jota pelaaja klikkailee. Toinen ruudukko pysyy piilossa
    ja siihen asetetaan kaikki miinat ja numerot.Kun pelaaja klikkaa peliruudukkoa,
    niin klikattu peliruutu vaihdetaan ruudukon ruuduksi.
    Tässä funktiossa myös aloitetaan ajanotto.
    """
    ruudukko = []
    korkeus, leveys, lukumaara = kentan_ulottuvuudet()
    for rivi in range(leveys):
        ruudukko.append([])
        for sarake in range(korkeus):
            ruudukko[-1].append(" ")
    tila["ruudukko"] = ruudukko
    peliruudukko = []
    for rivi in range(leveys):
        peliruudukko.append([])
        for sarake in range(korkeus):
            peliruudukko[-1].append(" ")
    tila["peliruudukko"] = peliruudukko
    miinoita(ruudukko, lukumaara)
    numeroi_ruudut(ruudukko)
    tila["aika_aloitus"] = time.time()
    print()
    print()
    print("Hiiren vasen painike aukaisee ruutuja ja oikea painike asettaa lipun tai poistaa sen.\n"
          "VOITAT PELIN, kun olet merkannut kaikki miinat asianmukaisella tavalla.\n"
          "Jos avaat ruudun jossa on miina, HÄVIÄT PELIN.")
    print()
    print()


def miinoita(ruudukko, lukumaara):
    """
    Asettaa kentällä n kpl miinoja satunnaisiin paikkoihin.
    """
    miinat = []
    i = 0
    while lukumaara > i:
        valittu_x = random.randint(0, len(ruudukko[0]) - 1)
        valittu_y = random.randint(0, len(ruudukko) - 1)
        if ruudukko[valittu_y][valittu_x] == " ":
            ruudukko[valittu_y][valittu_x] = "x"
            miinat.append((valittu_x, valittu_y))
            i += 1
    tila["miinat"] = miinat
    tila["ruudukko"] = ruudukko


def numeroi_ruudut(ruudukko):
    """
    Muuttaa ruutujen arvot vastaamaan viereisten miinojen määrää.
    """
    for rivinro, rivi in enumerate(ruudukko):
        for sarakenro, sarake in enumerate(rivi):
            if sarake != "x":
                ruudukko[rivinro][sarakenro] = str(naapurilaskin(sarakenro, rivinro))
    tila["ruudukko"] = ruudukko


def naapurilaskin(x, y):
    """
    laskee valitun ruudun ympärillä olevat miinat
    ja palauttaa niiden arvon kokonaislukuna.
    """
    leveys = len(tila["ruudukko"][0])
    korkeus = len(tila["ruudukko"])
    naapurit = 0
    for n in range(y - 1, y + 2):
        for m in range(x - 1, x + 2):
            if 0 <= n < korkeus:
                if 0 <= m < leveys:
                    naapuri = tila["ruudukko"][n][m]
                    if naapuri == "x":
                        naapurit += 1
    return naapurit


def tulvataytto(x, y):
    """
    Merkitsee tuntemattomat alueet turvalliseksi siten, että
    täyttö aloitetaan annetusta x, y -pisteestä.
    """
    tulva = [(x, y)]
    while tulva:
        x, y = tulva.pop()
        tila["peliruudukko"][x][y] = tila["ruudukko"][x][y]
        tila["liput"].clear()
        for i in (
                (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1), (x + 1, y + 1),
                (x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)
        ):
            n = i[0]
            m = i[1]
            if 0 <= n < len(tila["peliruudukko"]) and 0 <= m < len(tila["peliruudukko"][0]):
                if tila["ruudukko"][n][m] == "0" and tila["peliruudukko"][n][m] == " " and \
                        tila["peliruudukko"][n][m] != "f":
                    tulva.append((n, m))
                elif tila["peliruudukko"][n][m] == "f" and tila["ruudukko"][n][m] == "0":
                    tulva.append((n, m))
                elif tila["ruudukko"][n][m] != "x" or tila["peliruudukko"][n][m] == "f":
                    tila["peliruudukko"][n][m] = tila["ruudukko"][n][m]
                else:
                    tila["peliruudukko"][x][y] = tila["ruudukko"][x][y]


def ruudun_avaus(x, y):
    """
    Avaa ruudun.
    """
    tila["peliruudukko"][x][y] = tila["ruudukko"][x][y]
    if tila["peliruudukko"][x][y] != "f":
        if tila["peliruudukko"][x][y] == "0":
            tulvataytto(x, y)
    piirra_kentta()


def liputa(x, y):
    """
    liputtaa ruudun.
    """
    if tila["peliruudukko"][x][y] == " ":
        tila["peliruudukko"][x][y] = "f"
        tila["liput"].append((y, x))
        piirra_kentta()
    elif tila["peliruudukko"][x][y] == "f":
        tila["peliruudukko"][x][y] = " "
        tila["liput"].remove((y, x))
    piirra_kentta()


def havio():
    """
    Häviää pelin, lopettaa ajanoton ja kirjaa tulokset.
    """
    tila["peliruudukko"] = tila["ruudukko"]
    piirra_kentta()
    tila["aika_lopetus"] = time.time()
    tila["tappio"] = True
    kirjaa_tulokset()
    print("                        PELISI ON PÄÄTTYNYT! \n"
          "                           HÄVISIT PELIN!\n"
          "                         SULJE PELI-IKKUNA \n "
          "                       JA PALAA TERMINAALIIN")
    haravasto.lopeta()


def voitto():
    """
    Voittaa pelin, lopettaa ajanoton ja kirjaa tulokset.
    """
    if set(tila["liput"]) == set(tila["miinat"]):
        piirra_kentta()
        tila["aika_lopetus"] = time.time()
        tila["tappio"] = False
        kirjaa_tulokset()
        print("                            VOITIT PELIN\n"
              "                         SULJE PELI-IKKUNA \n "
              "                        JA PALAA TERMINAALIIN")
        haravasto.lopeta()


def kirjaa_tulokset():
    """
    Tallentaa pelin tiedot ja tulokset tekstitiedostoon.
    :return:
    """
    with open("tulokset.txt", "a+") as data:
        if tila["tappio"]:
            tulos = "Häviö"
        else:
            tulos = "Voitto"
        data.write(
            "{tulos}, {paivamaara}, kulunut aika: {tiem:02} minuuttia,\n"
            "klikkausten määrä: {lkm}, kentän koko {kanta}x{korkeus}, miinojen lkm: {miinat}\n"
            " \n"
                .format(
                tulos=tulos,
                paivamaara=time.ctime(),
                tiem=round((tila["aika_lopetus"] - tila["aika_aloitus"]) / 60, 2),
                lkm=tila["klikit"],
                kanta=len(tila["ruudukko"]),
                korkeus=len(tila["ruudukko"][0]),
                miinat=len(tila["miinat"]))
        )


def tulokset():
    """
    Avaa tulokset.
    """
    webbrowser.open("tulokset.txt")


def piirra_kentta():
    """
    Käsittelijäfunktio, joka piirtää kaksiulotteisena listana kuvatun miinakentän
    ruudut näkyviin peli-ikkunaan. Funktiota kutsutaan aina kun pelimoottori pyytää
    ruudun näkymän päivitystä.
    """
    haravasto.tyhjaa_ikkuna()
    haravasto.piirra_tausta()
    haravasto.aloita_ruutujen_piirto()
    for ruutu_x in range(len(tila["ruudukko"])):
        x_leveys = ruutu_x * 40
        for ruutu_y in range(len(tila["ruudukko"][0])):
            y_leveys = ruutu_y * 40
            haravasto.lisaa_piirrettava_ruutu(tila["peliruudukko"][ruutu_x][ruutu_y],
                                              x_leveys, y_leveys)
    haravasto.piirra_ruudut()


def kasittele_hiiri(x, y, hiiren_painike, nappain):
    """
    Käsitteleen hiiren ja laskee jokaisen ruudun avauksen, jotka tallennetaan pelin päätyttyä.
    """
    x = int(x / 40)
    y = int(y / 40)
    if hiiren_painike == haravasto.HIIRI_VASEN and tila["peliruudukko"][x][y] == " ":
        tila["klikit"] += 1
        ruudun_avaus(x, y)
        if tila["peliruudukko"][x][y] == "x":
            havio()
    elif hiiren_painike == haravasto.HIIRI_OIKEA:
        liputa(x, y)
        voitto()


def pelaa():
    """
    Aloittaa pelin.
    """
    tila["liput"] = []
    tila["ruudukko"] = []
    tila["klikit"] = 0
    tee_ruudukko()
    haravasto.lataa_kuvat("spritet")
    haravasto.luo_ikkuna(len(tila["ruudukko"] * 40), len(tila["ruudukko"][0] * 40))
    haravasto.aseta_piirto_kasittelija(piirra_kentta)
    haravasto.aseta_hiiri_kasittelija(kasittele_hiiri)
    haravasto.aloita()


print("¤¤¤-----------------------MIINANTALLAAJA-----------------------¤¤¤\n"
      "                        TERVETULOA PELAAJA                   ")


def main():
    while True:
        print()
        print()
        print("                             (P)elaa")
        print("                             (T)ulokset")
        print("                             (L)opeta")
        print()
        valinta = input("                           Tee valintasi: ").strip().lower()
        if valinta in ("p", "pelaa"):
            pelaa()
        elif valinta in ("t", "tulokset"):
            tulokset()
        elif valinta in ("l", "lopeta"):
            print("                                HEI!")
            time.sleep(.6)
            print("                                HEI!")
            break
        else:
            print("Valitsemaasi toimintoa ei ole olemassa")


if __name__ == "__main__":
    main()
