import math
def calc_dist(punto,origen): #punto es el cajero
    x2=punto[0]
    y2=punto[1]
    x1=origen[0]
    y1=origen[1]
    distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distancia


def main():
    cajeros=( (10,10),(50,10),(90,10),(10,50),(50,50),(90,50),(10,90),(50,90),(80,80),(90,90)   )
    entrada = input("Ingresa las coordenadas X y Y separadas por una coma: ")
    usuario = [float(n) for n in entrada.split(",")]
    print(calc_dist(cajeros[0],usuario))

main()