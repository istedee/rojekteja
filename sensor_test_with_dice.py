#!/usr/bin/python3
"""
    Tämä ohjelma testaa SenseHAT:n eri sensoreita.
    Sensehatin joystickkiä käyttämällä ohjelma piirtää HAT:n LED-matrixille
    lämpötilan, ilmankosteuden ja ilmanpaineen. Lisäksi ohjelmalla voi myös
    heittää noppaa ja tarkistaa tarkan päivämäärän. Ohjelma piirtää
    käynnistyessä alkeellisen, mutta selkeän valikon, joka näyttää mahdolliset
    painallukset, joita joystickillä voi tehdä;
    joystickkiä voi painaa neljään eri suuntaan ja painaa keskelle
"""
import time as t
from sense_hat import SenseHat
import sys
from random import randint
class values:
    s = SenseHat()
    c = s.clear()
    t = t.ctime()
    x = (50, 0, 50)
    b = (0, 0, 50)
    d = (0, 0, 0)
    w = (100, 100, 100)
    temp = str(round(s.get_temperature(), 1))
    hum = str(round(s.get_humidity(), 1))
    pres = str(round(s.get_pressure()))
p1 = values
menu_pixels = [
    p1.b, p1.b, p1.b, p1.w, p1.w, p1.b, p1.b, p1.b,
    p1.b, p1.b, p1.b, p1.b, p1.b, p1.b, p1.b, p1.b,
    p1.b, p1.b, p1.b, p1.b, p1.b, p1.b, p1.b, p1.b,
    p1.w, p1.b, p1.b, p1.w, p1.w, p1.b, p1.b, p1.w,
    p1.w, p1.b, p1.b, p1.w, p1.w, p1.b, p1.b, p1.w,
    p1.b, p1.b, p1.b, p1.b, p1.b, p1.b, p1.b, p1.b,
    p1.b, p1.b, p1.b, p1.b, p1.b, p1.b, p1.b, p1.b,
    p1.b, p1.b, p1.b, p1.w, p1.w, p1.b, p1.b, p1.b,
    ]

def main():    
    p1.c
    while True:
        p1.s.set_pixels(menu_pixels)
        p1.s.low_light = True
        for event in p1.s.stick.get_events():
            if event.action == "pressed":
                if event.direction == "middle":
                    p1.s.show_message(p1.t, 0.05, p1.b)
                elif event.direction == "left":
                    p1.s.show_message(p1.temp + " C", 0.05, p1.b)
                elif event.direction == "right":
                    p1.s.show_message(p1.hum + " %", 0.05, p1.b)
                elif event.direction == "up":
                    p1.s.show_message(p1.pres + " mbar", 0.05, p1.b)
                elif event.direction == "down":
                    for i in range(30):
                        p1.s.show_letter(str(randint(1, 6)), p1.b)
                        t.sleep(0.05)
                t.sleep(1)
                p1.c

main()