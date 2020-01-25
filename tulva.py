import haravasto

def piirra_kentta():
    """
    Käsittelijäfunktio, joka piirtää kaksiulotteisena listana kuvatun miinakentän
    ruudut näkyviin peli-ikkunaan. Funktiota kutsutaan aina kun pelimoottori pyytää
    ruudun näkymän päivitystä.
    """
    haravasto.tyhjaa_ikkuna()
    haravasto.piirra_tausta()
    haravasto.aloita_ruutujen_piirto()
    for ruutu_y, ruutu in enumerate(planeetta):
        y_koodi = ruutu_y * 40
        for ruutu_x, avain in enumerate(ruutu):
            x_koodi = ruutu_x * 40
            haravasto.lisaa_piirrettava_ruutu(avain, x_koodi, y_koodi)

    haravasto.piirra_ruudut()

def tulvataytto(planeetta, x, y):
    """
    Merkitsee planeetalla olevat tuntemattomat alueet turvalliseksi siten, että
    täyttö aloitetaan annetusta x, y -pisteestä.
    """
    tulva = [(x, y)]
    if planeetta[y][x] == "x":
        return
    while tulva:
        x, y = tulva.pop()
        planeetta[y][x] = "0"
        for i in ((x-1, y-1), (x+1, y-1), (x-1, y+1), (x+1, y+1), (x-1, y), (x, y-1), (x+1, y), (x, y+1)):
            n = i[0]
            m = i[1]
            if n < 0 or n > len(planeetta[0])-1 or m < 0 or m > len(planeetta)-1:
                    continue
            else:
                if planeetta[m][n] == " ":
                    tulva.append((n, m))
def main(planeetta):
    haravasto.lataa_kuvat("spritet")
    haravasto.luo_ikkuna(len(planeetta[0]) * 40, len(planeetta) * 40)
    haravasto.aseta_piirto_kasittelija(piirra_kentta)
    haravasto.aloita()
planeetta = [
    [" ", " ", " ", "x", " ", " ", " ", " ", " ", " ", " ", "x", " "],
    [" ", " ", "x", "x", " ", " ", " ", "x", " ", " ", " ", "x", " "],
    [" ", " ", "x", " ", " ", " ", " ", "x", " ", " ", "x", "x", " "],
    ["x", " ", "x", "x", "x", " ", " ", "x", " ", "x", " ", " ", " "],
    ["x", " ", "x", "x", " ", " ", " ", " ", "x", " ", "x", " ", " "],
    [" ", " ", "x", " ", " ", " ", " ", " ", " ", "x", " ", " ", " "]
]
tulvataytto(planeetta, 0, 0)
main(planeetta)