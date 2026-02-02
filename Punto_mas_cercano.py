import math
def calc_dist(cajeros,origen):
    x2=cajeros[0]
    y2=cajeros[1]
    x1=origen[0]
    y1=origen[1]
    distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distancia

def dist_mas_cerca(origen,cajeros):#el origen es la coordenada del usuario
    mas_cerca= 999999999
    for n in range(len(cajeros)):
        dist_actual=calc_dist(cajeros[n],origen)
        if (dist_actual < mas_cerca):
            poss=n
            mas_cerca=dist_actual
    return poss,mas_cerca

def Crea_cajeros():
    poligono = []
    vertices=int(input("Cuantos Cajeros vas a crear? "))
    for n in range(vertices):
        entrada = input(f"Cajero {n + 1}: - Ingresa X y Y separados por coma: ")
        coordenadas = tuple(int(i.strip()) for i in entrada.split(","))
        poligono.append(coordenadas)
    return poligono

def imprime_cajeros(cajeros):
    print("Los cajeros disponibles en la region son los siguientes:")
    for n in range(len(cajeros)):
        print(f"Cajero{n+1}: {cajeros[n]} " )

def main():
    cajeros=Crea_cajeros()
    imprime_cajeros(cajeros)
    entrada = input("Ingresa las coordenadas X y Y separadas por una coma: ")
    usuario = [int(n) for n in entrada.split(",")]
    poss,dist=  dist_mas_cerca(usuario,cajeros)
    print(f"El cajero mas cercano es el {poss+1} a una distancia de {dist:.2f} metros ")
main()