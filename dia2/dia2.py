import re

def parseGame (line):
    #(Game \d:){1}(( \d \w*,)+( \d \w*;))*( \d \w*,)+
    aux = str.split(line, ':')
    return aux

def getGameNumber(text):
    return re.search('(\d)', text).group(0)

def parseRounds(line):
    return str.split(line, ';')
    
def parseBolas(text):
    list = str.split(text, ',')
    bolas = {}
    for tipo in list:
        aux = re.search('(\d) (blue|green|red)', tipo.lstrip())
        bolas.update({ int(aux.group(1)) : aux.group(2)})
    return bolas

#Open input
filename = '/home/manu/Documentos/dev/adventofcode2023/dia2/input_test.txt'
with open(filename) as file:
    lines = [line.rstrip() for line in file]
#Just test the input
for line in lines:
    print(line)

#Make things
result = 0
# Red, Green, Blue
requisitos = [12, 13, 14]

## Convertir la entrada en algo manejable

lista_juegos = []

for line in lines:
    game = parseGame(line)
    game_number = getGameNumber(game[0])
    list_rounds = []
    for round in parseRounds(game[1]):
        list_rounds.append(parseBolas(round))
    lista_juegos.append(list_rounds)

#print(lista_juegos)

for juego in lista_juegos:
    for ronda in juego:
        pass



#Print result
#print(result)

