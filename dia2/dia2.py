import re

class Ronda:
    red = 0
    blue = 0
    green = 0
    def __init__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b
class Juego:
    juegos = []

#Open input
filename = './input_test.txt'
with open(filename) as file:
    lines = [line.rstrip() for line in file]
#Just test the input
for line in lines:
    print(line)

#Make things
result = 0

## Convertir la entrada en algo manejable

lista_juegos = []

# ronda1 = Ronda(2,3,5)
# ronda2 = Ronda(1,15,3)
# juego = [ronda1, ronda2]
# lista_juegos.append(juego)
# print(lista_juegos)

for line in lines:
    for c in 



#Print result
#print(result)

def parseGame (line):
#(Game \d:){1}(( \d \w*,)+( \d \w*;))*( \d \w*,)+
    re.
