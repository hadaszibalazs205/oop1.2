'''
1.2 Feladat
Készíts egy programot, amelyben van egy Negyzet nevű osztály. Attribútuma legyen az oldal hossza. 
A metódus ne a kerület- illetve a területértékkel térjen vissza, hanem maga gondoskodjon ezen értékek kiírásáról egy egész mondatos formában.
'''

class Negyzet:
    def __init__(self, oldal_hossz=(1)):
        self.old_hossz = oldal_hossz
        

    def info(oldal_hossz):
        print(f'A negyzet terulete:{oldal_hossz} hosszusagu, kerülete:{oldal_hossz} egység')

negyzet1 = Negyzet(5)
negyzet1.info()