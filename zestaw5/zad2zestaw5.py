from math import gcd


class Q:

    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik

    def skracanie(self):
        nwd = gcd(self.licznik, self.mianownik)
        return Q(self.licznik//nwd, self.mianownik//nwd)

    def __add__(self, other):
        licz = self.licznik*other.mianownik + other.licznik*self.mianownik
        mian = self.mianownik*other.mianownik
        return Q(licz, mian).skracanie()

    def __sub__(self, other):
        licz = self.licznik*other.mianownik - other.licznik*self.mianownik
        mian = self.mianownik*other.mianownik
        return Q(licz, mian).skracanie()
    
    def __mul__(self, other):
        licz = self.licznik*other.licznik
        mian = self.mianownik*other.mianownik
        return Q(licz, mian).skracanie()

    def __truediv__(self, other):
        licz = self.licznik*other.mianownik
        mian = self.mianownik*other.licznik
        return Q(licz, mian).skracanie()

    def __floordiv__(self, other):
        licz = self.licznik*other.mianownik
        mian = self.mianownik*other.licznik
        return Q(licz//mian, licz//mian).skracanie()

    def __pow__(self.other):
        

    def __str__(self):
        return f"{self.licznik}/{self.mianownik}"

if __name__=="__main__":

    l1, m1, w1, l2, m2, w2 = input().split()
    l1 = int(l1); m1 = int(m1); l2 = int(l2); m2 = int(m2); w1 = int(w1); w2 = int(w2)
    q1 = Q(l1, m1)
    q2 = Q(l2, m2)
    print(w1//w2)