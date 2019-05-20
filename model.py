import random

STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
NAPACNA_CRKA = '-'
PONOVLJENA_CRKA = '0'
ZMAGA = 'W'
PORAZ = 'L'

class Igra:
    def __init__ (self, geslo, crke = None):
        self.geslo = geslo
        self.crke = [] if crke == None else crke
    
    def napacne_crke(self):
        ugibane_crke = []
        for crka in self.crke:
            if crka == self.geslo:
                ugibane_crke.append(crka)
        return ugibane_crke
    
    def pravilne_crke(self):
        ugibane_crke_pravilne = []
        for crka in self.crke:
            if crka == self.geslo:
                ugibane_crke_pravilne.append(crka)
        return ugibane_crke_pravilne
    
    def  stevilo_napak(self):
        return len(self.napacne_crke())
       
    def zmaga(self):
        for crka in self.geslo:
            if crka not in self.crke:
                return False
            else:
                return True

    def poraz(self):
        if self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK:
            return PORAZ

    def pravilni_del_gesla(self):
        nova_beseda = ''
        for crka in self.geslo:
            if crka in self.crke:
                nova_beseda += '_ ' 
        return nova_beseda
    
    def nepravilni_ugibi(self):
        niz_nepravilnih_crk = ''
        for crka in self.napacne_crke():
            niz_nepravilnih_crk += crka
        return niz_nepravilnih_crk

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        elif crka not in self.geslo:
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA
        else:
            if self.zmaga():
                return ZMAGA
            else: 
                return PRAVILNA_CRKA

bazen_besed = []
with open('besede.txt', 'r', encoding='utf-8') as d:
    for vrstica in d:
        bazen_besed.append(vrstica.upper().strip())

def nova_igra():
    return Igra(random.choice(bazen_besed))


ZACETEK = nova_spemenljivka
class Vislice:
    def __init__(self, igra):
        self.igra = {}

    def prost_id_igre(self):
        if self.igra == {}:
            return 0
        else:
            return max(self.igra.keys()) + 1
        
    def nova_igra(self):
        id_igre = self.prost_id_igre()
        igra = nova_igra()
        self.igra[id_igre] = (igra, ZACETEK)
        return id_igre
    
    def ugibaj(self, id_igre, crka):
        igra, _ = self.igra[id_igre][0]
        poskus = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, poskus)

