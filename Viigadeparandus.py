from math import * #Vale seadistus

print("Ruudu karakteristikud")
a=float(input("Sisesta ruudu külje pikkus => ")) #sisestada float
S=a**2
print("Ruudu pindala",round(S,1))
P=4*a
print("ruudu ümbermõõt", round(P,1)) #panna teise kohta jutumärk
di=a*sqrt(2)
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") #üks sulg kustasin ära
b=float(input("Sisesta ristküliku 1. külje pikkus => "))
c=float(input("Sisesta ristküliku 2. külje pikkus => "))
S=b*c
print("Ristküliku pindala", round(S,1))
P=2*(b+c)
print("Ristküliku ümbermõõt", round(P,1))
di=sqrt(b*2+c*2)
print("Ristküliku diagonaal", round(di,1))
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => "))#üks sulg kustasin ära
d=2*r
print("Ringi läbimõõt",round(d,1)) #sisestada round,1
S=pi*r**2 # see () sümbol muutub see *
print("Ringi pindala", round(S,2)) #sisestada round, 2
C=2*pi*r #sisestada korrutamine
print("Ringjoone pikkus", round(C,2)) #lisan üks sulg
