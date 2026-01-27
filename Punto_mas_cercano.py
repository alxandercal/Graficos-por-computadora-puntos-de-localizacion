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
    for n in range(10):
        dist_actual=calc_dist(cajeros[n],origen)
        if (dist_actual < mas_cerca):
            poss=n
            mas_cerca=dist_actual
    return poss

def main():
    cajeros=( (10,10),(50,10),(90,10),(10,50),(50,50),(90,50),(10,90),(50,90),(80,80),(90,90)   )
    entrada = input("Ingresa las coordenadas X y Y separadas por una coma: ")
    usuario = [int(n) for n in entrada.split(",")]
    cercano=  dist_mas_cerca(usuario,cajeros)
    print("El cajero mas cercano es el ",cercano+1)

main()